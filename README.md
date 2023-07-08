# MLOPS Project / Youtube Spotify Trending

## 1. Problem description
YouTube and Spotify have been recognized as the most frequently visited platforms globally, serving as primary channels through which individuals not only amass wealth but also cultivate widespread fame. A "trending" status on these platforms is often viewed as the pinnacle of achievement for content creators, indicating that their content has gained significant popularity within a certain time frame. To achieve this status, it is crucial to understand the variables that can influence this outcome. This understanding can subsequently guide a systematic plan for trending.

In this advanced machine learning model, we intend to examine two principal factors: the number of viewers and licensing agreements. The choice of these two variables is not arbitrary. The number of viewers directly signifies the popularity of the content, while licensing deals could potentially broaden the reach of the content, hence leading to increased viewership and likelihood of trending.

We hypothesize that licensed content may generate a wider audience, which in turn, influences the trending status of the content. However, it is important to note that these factors are just a fraction of a larger set of parameters that could impact a content's trendiness. These other factors might include content quality, content type, publication time, among others. Nevertheless, for the scope of this project, our primary focus is to build a sustainable machine learning model, and hence, we are limiting our study to these two factors.

<img src="https://github.com/Irf4n-Muhammad/MLOPS-Project-Youtube-Trending/assets/121205860/f135a391-46fb-45a6-bc10-368d4f87b07b" alt="your image description" width="500" height="300">

It is imperative to highlight the need for regular maintenance and testing of this machine learning model. This is crucial to ensure its robustness and reliability, especially given that user behavior and consumption patterns on platforms like YouTube and Spotify are dynamic and can change rapidly. Regular monitoring and testing will allow us to identify any anomalies, adapt to pattern shifts, and ensure that the predictive model remains reliable and trustworthy.

Further, to manage the sustainability of our machine learning model, we will incorporate practices such as model validation, updating the training data, and employing a robust monitoring system to track the model's performance over time. This sustainable machine learning environment will enable the model to remain sensitive to emerging trends, thereby allowing it to maintain its accuracy in predicting trending status based on viewer numbers and licensing agreements. By this method, we are not just establishing a one-time solution but building a resilient, evolving model that can adapt to the ever-changing digital landscape.

Dataset source:

https://www.kaggle.com/datasets/salvatorerastelli/spotify-and-youtube


## 2. Cloud
For this project, we will use AWS cloud to intergrate our model for storing and transforming the model. But before that, we need to set up the terraform to set up the setting for our AWS Cloud, but this section will assume that we have finished using terraform.

### 2.1 Use IAM

### 2.1.1 Create the Root:
1. Use your gmail to create the root account
2. You gonna use this as main account that will be integrated to many user account

### 2.1.2 Create the User:
1. Open the IAM features and click user
2. Create the new user
3. Make your username
4. Create new group and click the policy that we need (AWSS3FullService, AdministratorAccess)
5. Create the user
6. You will find the AWS key and also the AWS secret key. Don't forget to copy your AWS secret key and your key because it will be important for aws configuration. Also, download the csv file.
7. Logout from root account and connect to the user account using AccountID and password
8. Now, your user account was set up

### 2.2 Using AWS S3 (Storing Model)
1. Open the s3 features
2. Create the new bucket
3. Write your s3 bucket name. Make it authentic which show what this bucket related to
4. Choose the timezone that close to your livinghood.
5. Create the bucket and your bucket is ready

### 2.3 Create the RDS Database (Storing Model)
1. Open the RDS features
2. Create the databse
3. Choose PostgreSQL and choose free tier
4. Make your DB name on 'DB Instance Identifier'
5. Write master username (I write mlflow)
6. Click auto generate password
7. Leave the instance configuration, Storage, Connectivity if you just need free tier
8. Click additional configuration to make the database:
   
   <img width="566" alt="image" src="https://github.com/Irf4n-Muhammad/MLOPS-Project-Youtube-Trending/assets/121205860/eb5efac0-9cc4-4762-83a2-382ba2ad9c98">
10. Create the database and it is ready
11. View the credentials setting, so you will find the master username and password. Please copy that:
    
    <img width="913" alt="image" src="https://github.com/Irf4n-Muhammad/MLOPS-Project-Youtube-Trending/assets/121205860/476ae47a-bf59-4c3c-b02a-67573718cbc5">
13. Go to the security section:
    
    <img width="183" alt="image" src="https://github.com/Irf4n-Muhammad/MLOPS-Project-Youtube-Trending/assets/121205860/1a61a9df-ebc8-494f-b5ee-ebe6703b405e">
15. Edit the inbound rules:
    
    <img width="707" alt="image" src="https://github.com/Irf4n-Muhammad/MLOPS-Project-Youtube-Trending/assets/121205860/da8da7fa-7767-4469-97af-65e005fe4415">
17. Set the inbound rules:
    
    <img width="845" alt="image" src="https://github.com/Irf4n-Muhammad/MLOPS-Project-Youtube-Trending/assets/121205860/b8789f57-4b5f-4325-b592-b85c0fbda9ce">

19. Your database is ready

### 2.4 Create EC2 Virtual Machine:
1. Open EC2
2. Create new instances
3. Choose Amazon and instances type
4. Create the new key pair and save that on your computer
5. Create EC2
6. Then, click the instances ID and click connect and click ssh client
7. Copy the long SSH link and we will use that to running our machine
8. Create the Host configuration that aim to our instances
9. Running the VM and download the needed package with requirements.txt file

## 3. Experiment Tracking and Model Registry
### 3.1 Mlflow (Experiment Tracking):
1. Create conda that specifically for mlflow
2. Running the mlflow ui command :
   ```bash
   mlflow ui --backend-store-uri 'db_type:///path_to_db'
   ```
3. Copy the localhost link
   ```bash
   localhost:5000
   ```
4. Open the new terminal and running jupyter notebook on the mlflow conda
5. In the youtube-trending-prediction.ipynb has explained everything about how it work and connect to the Mlflow
6. In the Mlflow, we can see the metrics, log, artifact and the diagram of our result

### 3.2 Model Registry:
1. We can control and manage our model into certain condition (Staging, Production, and Archieve
2. The explanation how it works is explained in youtube-trending-prediction.ipynb


## 4. Workflow Orchestration
In this section, we will use prefect as our orchestration tool. We will deploy and run our model in prefect.

1. Script the file from jupyter notebook
   ```bash
   jupyter nbconvert --to script <name.ipynb>
   ```
3. Create the anaconda for prefect
   ```bash
   conda create -n <name> bash
   conda activate <name>
   ```
4. Run the prefect server
   ```bash
   prefect server start
   ```
   Copy the localhost link
   ```bash
   localhost:8080
   ```
5. Initiliaze the prefect project
   ```bash
   prefect project init
   ```
   It will generate the file (deployment.yaml and prefect.yaml)
6. Create workpool in the prefect UI
7. Deploy the model into the prefect
   ```bash
   prefect deploy <path to the model>:main_flow -n <model_name> -p <workpool_name>
   ```
8. Running the worker network
   ```bash
   prefect worker start
   ```
9. Open the prefect UI and find the flows. Click quick run
10. You will see the data generated in our terminal
    
    <img width="814" alt="image" src="https://github.com/Irf4n-Muhammad/MLOPS-Project-Youtube-Trending/assets/121205860/e252d515-d6a8-4fbe-b5ea-8c16a946a675">


## 5. Model deployment
In this section, we will deploy our model from mlflow through web service and connect to the AWS S3 as the server so we can independently running our model without relying on our local server which most likely will shutdown and affect our running model. 

1. Firstly we try to edit our last python file to be only running the model intead training the model
2. You can see on the 'web-service-deployment' for the full python file.
3. There are several features that have to be put on the python file to be connected to the AWS S3

```python
MLFLOW_TRACKING_URI = 'http://127.0.0.1:5000'
RUN_ID = os.getenv('RUN_ID')
# export RUN_ID='0baad4b2afeb41b48e1469722bd12fda'

mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
logged_model = f's3://mlflow-artifacts-remote-zoomcamp/1/{RUN_ID}/artifacts/model'
model = mlflow.pyfunc.load_model(logged_model)
```

4. Some function that we will use to run our model which we can edit and will not affect the current model
```python
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
```
5. The main function to arrange the sequence of used function
```python
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
```
6. Connect to the port:
```python
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
```
7. Running the server
```bash
pipenv shell
export RUN_ID=<Your ID>
python predict.py
```
8. Run the result in the different terminal
```bash
python test.py
```

## 6.Model monitoring
In monitoring, we will check the quality of our model using several indicators. We will leverage some tools such as jupyter notebook, grafana, and adminer. We will produce the dummy metrics that we will use to test our model.

1. Set up the environment by creating the conda env and downloading the requirements package, also create the docker-compose file and build it
2. Open the jupyter notebook and try to create the documentation, for the full process, read the file by yourself
3. Create the dummy python file to produce and send the dummy metrics
4. See the updated data in the adminer by connecting to the localhost
   
   ```bash
   localhost:8080
   ```
6. You can create the visualization diagram using grafana
   
   ```bash
   localhost:3000
   ```
7. Create the dummy quality test python following the same idea as the previous one to create the visualization diagrams



Reproducibility

Best practices
 There are unit tests (1 point)
 There is an integration test (1 point)
 Linter and/or code formatter are used (1 point)
 There's a Makefile (1 point)
 There are pre-commit hooks (1 point)
 There's a CI/CD pipeline (2 points)
