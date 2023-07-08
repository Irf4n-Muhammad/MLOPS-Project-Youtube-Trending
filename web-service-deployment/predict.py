import pickle
import mlflow
from mlflow.tracking import MlflowClient
from flask import Flask, request, jsonify
import os

MLFLOW_TRACKING_URI = 'http://127.0.0.1:5000'
RUN_ID = os.getenv('RUN_ID')
# export RUN_ID='0baad4b2afeb41b48e1469722bd12fda'

mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
logged_model = f's3://mlflow-artifacts-remote-zoomcamp/1/{RUN_ID}/artifacts/model'
model = mlflow.pyfunc.load_model(logged_model)

def prepare_features(ride):
    features = {}
    features['Licensed'] = ride['Licensed']
    features['Views'] = ride['Views']
    features['Likes'] = ride['Likes']
    
    return features


def predict(features):
    preds = model.predict(features)
    pred_value = float(preds[0])
    return pred_value if pred_value > 1 else 1


app = Flask('trending-prediction')

@app.route('/predict', methods=['POST'])
def predict_endpoint():
    ride = request.get_json()
    
    features = prepare_features(ride)
    pred = predict(features)
    
    result = {
        'Trending Rank': pred,
        'model_version': RUN_ID
    }
    
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
