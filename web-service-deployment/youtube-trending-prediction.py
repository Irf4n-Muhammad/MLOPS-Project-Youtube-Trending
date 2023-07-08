import pathlib
import pickle
import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import mean_squared_error
import mlflow
from prefect import flow, task
from datetime import datetime


@task(retries=3, retry_delay_seconds=2)
def read_data(file_path: str) -> pd.DataFrame:
    """Read data into DataFrame"""
    df = pd.read_csv(file_path)
    df = df.reset_index(drop=True)
    df.index = df.index + 1
    df = df.dropna()
    df = df.drop(['Url_spotify', 'Uri'], axis=1)
    
    df['Trending'] = df.shape[0] + 1 - df['Views'].rank()
    df = df.sort_values(by='Trending', ascending=True)
    
    return df


@task
def add_features(
    df_train: pd.DataFrame, df_val: pd.DataFrame
) -> tuple:
    """Add features to the model"""
    categorical = ['Licensed']
    numerical = ['Views', 'Likes']
    
    dv = DictVectorizer()

    train_dicts = df_train[categorical + numerical].to_dict(orient='records')
    X_train = dv.fit_transform(train_dicts)

    val_dicts = df_val[categorical + numerical].to_dict(orient='records')
    X_val = dv.transform(val_dicts)
    
    target = 'Trending'
    y_train = df_train[target].values
    y_val = df_val[target].values
    return X_train, X_val, y_train, y_val, dv


@task(log_prints=True)
def train_best_model(
    X_train, X_val, y_train, y_val, dv
) -> None:
    """Train a model with best hyperparams and write everything out"""
    with mlflow.start_run(experiment_id="0"):
        current_datetime = datetime.now().strftime('%Y-%m-%d_%H:%M:%s')
        
        train = xgb.DMatrix(X_train, label=y_train)
        valid = xgb.DMatrix(X_val, label=y_val)

        best_params = {
            'learning_rate': 0.09585355369315604,
            'max_depth': 30,
            'min_child_weight': 1.060597050922164,
            'objective': 'reg:squarederror',
            'reg_alpha': 0.018060244040060163,
            'reg_lambda': 0.011658731377413597,
            'seed': 42
        }

        mlflow.log_params(best_params)

        booster = xgb.train(
            params=best_params,
            dtrain=train,
            num_boost_round=1000,
            evals=[(valid, 'validation')],
            early_stopping_rounds=50
        )

        y_pred = booster.predict(valid)
        rmse = mean_squared_error(y_val, y_pred, squared=False)
        
        range = y_val.max() - y_val.min()
        mlflow.log_metric("rmse", rmse)
        error_percentage = rmse / range * 100
        mlflow.log_metric("error_percentage", error_percentage)

        pathlib.Path("models").mkdir(exist_ok=True)
        with open(f"models/preprocessor-{current_datetime}.b", "wb") as f_out:
            pickle.dump(dv, f_out)
        mlflow.log_artifact(f"models/preprocessor-{current_datetime}.b", artifact_path="preprocessor")

        mlflow.xgboost.log_model(booster, artifact_path="models_mlflow")
    return None


@flow
def main_flow(file_path: str) -> None:
    """The main training pipeline"""

    # MLflow settings
    mlflow.set_tracking_uri("sqlite:///mlflow.db")
    mlflow.set_experiment("my-experiment-2")

    # Load
    df = read_data(file_path)
    
    # Split
    split_number = int(len(df)/2)
    df_train = df[:split_number]
    df_val = df[split_number:]
    
    # Transform
    X_train, X_val, y_train, y_val, dv = add_features(df_train, df_val)

    # Train
    train_best_model(X_train, X_val, y_train, y_val, dv)


if __name__ == "__main__":
    main_flow("/home/ubuntu/mlops_project/data/spotify-and-youtube/Spotify_Youtube.csv")
