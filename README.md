# MLOPS Project / Youtube Spotify Trending

## 1. Problem description
YouTube and Spotify have been recognized as the most frequently visited platforms globally, serving as primary channels through which individuals not only amass wealth but also cultivate widespread fame. A "trending" status on these platforms is often viewed as the pinnacle of achievement for content creators, indicating that their content has gained significant popularity within a certain time frame. To achieve this status, it is crucial to understand the variables that can influence this outcome. This understanding can subsequently guide a systematic plan for trending.

In this advanced machine learning model, we intend to examine two principal factors: the number of viewers and licensing agreements. The choice of these two variables is not arbitrary. The number of viewers directly signifies the popularity of the content, while licensing deals could potentially broaden the reach of the content, hence leading to increased viewership and the likelihood of trending.

We hypothesize that licensed content may generate a wider audience, which in turn, influences the trending status of the content. However, it is important to note that these factors are just a fraction of a larger set of parameters that could impact a content's trendiness. These other factors might include content quality, content type, and publication time, among others. Nevertheless, for the scope of this project, our primary focus is to build a sustainable machine learning model, and hence, we are limiting our study to these two factors.

<img src="https://github.com/Irf4n-Muhammad/MLOPS-Project-Youtube-Trending/assets/121205860/f135a391-46fb-45a6-bc10-368d4f87b07b" alt="your image description" width="500" height="300">

It is imperative to highlight the need for regular maintenance and testing of this machine learning model. This is crucial to ensure its robustness and reliability, especially given that user behavior and consumption patterns on platforms like YouTube and Spotify are dynamic and can change rapidly. Regular monitoring and testing will allow us to identify any anomalies, adapt to pattern shifts, and ensure that the predictive model remains reliable and trustworthy.

Further, to manage the sustainability of our machine learning model, we will incorporate practices such as model validation, updating the training data, and employing a robust monitoring system to track the model's performance over time. This sustainable machine learning environment will enable the model to remain sensitive to emerging trends, thereby allowing it to maintain its accuracy in predicting trending status based on viewer numbers and licensing agreements. By this method, we are not just establishing a one-time solution but building a resilient, evolving model that can adapt to the ever-changing digital landscape.

Dataset source:

https://www.kaggle.com/datasets/salvatorerastelli/spotify-and-youtube

Pipeline flow:





## 2. Cloud
For this project, we will use AWS Cloud to integrate our model for storing and transforming the model. But before that, we need to set up the terraform to set up the setting for our AWS Cloud, but this section will assume that we have finished using Terraform.

### 2.1 Use IAM

### 2.1.1 Create the Root:
1. Use your gmail to create the root account
2. You gonna use this as main account that will be integrated to many user account

### 2.1.2 Create the User:
1. Open the IAM features and click user
2. Create the new user
3. Make your username
4. Create a new group and click the policy that we need (AWSS3FullService, AdministratorAccess)
5. Create the user
6. You will find the AWS key and also the AWS secret key. Don't forget to copy your AWS secret key and your key because it will be important for aws configuration. Also, download the CSV file.
7. Logout from the root account and connect to the user account using AccountID and password
8. Now, your user account was set up

### 2.2 Using AWS S3 (Storing Model)
1. Open the s3 features
2. Create the new bucket
3. Write your s3 bucket name. Make it authentic which shows what this bucket related to
4. Choose the timezone that is close to your living hood.
5. Create the bucket and your bucket is ready

### 2.3 Create the RDS Database (Storing Model)
1. Open the RDS features
2. Create the database
3. Choose PostgreSQL and choose the free tier
4. Make your DB name on 'DB Instance Identifier
5. Write master username (I write mlflow)
6. Click auto-generate password
7. Leave the instance configuration, Storage, and Connectivity if you just need free tier
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
7. Copy the long SSH link and we will use that to run our machine
8. Create the Host configuration that aims to our instances
9. Running the VM and download the needed package with the requirements.txt file

## 3. Experiment Tracking and Model Registry
### 3.1 Mlflow (Experiment Tracking):
1. Create conda that is specifically for mlflow
2. Running the mlflow ui command :
   ```bash
   mlflow ui --backend-store-uri 'db_type:///path_to_db'
   ```
3. Copy the localhost link
   ```bash
   localhost:5000
   ```
4. Open the new terminal and run jupyter notebook on the mlflow conda
5. In the [youtube-trending-prediction.ipynb](https://github.com/Irf4n-Muhammad/MLOPS-Project-Youtube-Trending/blob/main/experiment_tracking/youtube-trending-prediction.ipynb) has explained everything about how it works and connect to the Mlflow
6. In the Mlflow, we can see the metrics, log, artifact and diagram of our result

### 3.2 Model Registry:
1. We can control and manage our model in certain conditions (Staging, Production, and Archive)
2. The explanation of how it works is explained in youtube-trending-prediction.ipynb


## 4. Workflow Orchestration
In this section, we will use Prefect as our orchestration tool. We will deploy and run our model in Prefect.

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
   It will generate the file ([deployment.yaml](https://github.com/Irf4n-Muhammad/MLOPS-Project-Youtube-Trending/blob/main/workflow_orchestration/deployment.yaml) and [prefect.yaml](https://github.com/Irf4n-Muhammad/MLOPS-Project-Youtube-Trending/blob/main/workflow_orchestration/prefect.yaml))
6. Create workpool in the Prefect UI
7. Deploy the model into the Prefect
   ```bash
   prefect deploy <path to the model>:main_flow -n <model_name> -p <workpool_name>
   ```
8. Running the worker network
   ```bash
   prefect worker start
   ```
9. Open the Prefect UI and find the flows. Click quick run
10. You will see the data generated in our terminal
    
    <img width="814" alt="image" src="https://github.com/Irf4n-Muhammad/MLOPS-Project-Youtube-Trending/assets/121205860/e252d515-d6a8-4fbe-b5ea-8c16a946a675">


## 5. Model deployment
### 5.2 Web-Service Deployment:
In this section, we will deploy our model from mlflow through web service and connect to the AWS S3 as the server so we can independently running our model without relying on our local server which most likely will shutdown and affect our running model. 

1. Firstly we try to edit our last python file to be only running the model intead training the model
2. You can see on the [web-service-deployment](https://github.com/Irf4n-Muhammad/MLOPS-Project-Youtube-Trending/tree/main/web-service-deployment) for the full python file.
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
### 5.2 Streaming Deployment:
Streaming will send the real-time data that can be extracted at the same time, so it can be processed directly and can be used to develop our machine learning model. This idea will use kinesis to handle streaming data and lambda to process and transform the data. Then, we will connect it with web-service deployment in the workflow.

1. Firstly, we have to set up the lambda and the kinesis in our system by following the instruction in the amazon website
2. Create the role to allow the lambda permission ( name: lambda-kinesis-role ) and add permission ( AWSLambdaKinesisExectuionRole )
3. Open the function (in lambda section) and create new function and set the lambda role that'has been created
4. Afterwards, we can move our function from predict.py into the lambda function and we can make it to be simple for testing and it will be developed along the time.
5. Also click the test button and fill in the event JSON that will be the input for testing
6. After it's running, the log file will come out and we can see the success message or error
7. Create the data stream, so we can run it on the terminal
8. Create trigger near to kinesis and choose kinesis as our trigger configuration
9. AFter the trigger is enabled, then we can run this command in the terminal:
    ```bash
    KINESIS_STREAM_INPUT=trending_events
      aws kinesis put-record \
    --stream-name ${KINESIS_STREAM_INPUT} \
    --partition-key 1 \
    --data "Hello, this is a test."
    ```
10.  Then, we can check the log cloudwatch configuration to see the streaming data
11.  We develop it again and we can add this command in the terminal
    
    ```bash
    aws kinesis put-record \
    --stream-name ${KINESIS_STREAM_INPUT} \
    --partition-key 1 \
    --data '{
    "ride" : {
    'Likes': 50000000,
    'Views': 70000000,
    'Licensed': 'Yes',
    },
    "ride_id": 123 
    }'
    ```
12. If we open the cloudwatch, we will find the records of our streaming data in json form
    ```json
      {
          "Records": [
      {
                  "kinesis": {
                      "kinesisSchemaVersion": "1.0",
                      "partitionKey": "1",
                      "sequenceNumber": "49630081666084879290581185630324770398608704880802529282",
                      "data": "ewogICAgICAgICJyaWRlIjogewogICAgICAgICAgICAiUFVMb2NhdGlvbklEIjogMTMwLAogICAgICAgICAgICAiRE9Mb2NhdGlvbklEIjogMjA1LAogICAgICAgICAgICAidHJpcF9kaXN0YW5jZSI6IDMuNjYKICAgICAgICB9LCAKICAgICAgICAicmlkZV9pZCI6IDI1NgogICAgfQ==",
                      "approximateArrivalTimestamp": 1654161514.132
                  },
                  "eventSource": "aws:kinesis",
                  "eventVersion": "1.0",
                  "eventID": "shardId-000000000000:49630081666084879290581185630324770398608704880802529282",
                  "eventName": "aws:kinesis:record",
                  "invokeIdentityArn": "arn:aws:iam::XXXXXXXXX:role/lambda-kinesis-role",
                  "awsRegion": "eu-west-1",
                  "eventSourceARN": "arn:aws:kinesis:eu-west-1:XXXXXXXXX:stream/ride_events"
              }
          ]
      }
      ```
13. We want to extract the 'data' and decode so that we will get the humanreadable data
14. Then, we use the kinesis.put_record to set up the kinesis using kinesis client (we will add the it in the environment variable)
15. Add the policy 'put_records'
16. We tryin to listen to the new stream by using shard iterator
    ```bash
      KINESIS_STREAM_OUTPUT='ride_predictions'
      SHARD='shardId-000000000000'
      
      SHARD_ITERATOR=$(aws kinesis \
          get-shard-iterator \
              --shard-id ${SHARD} \
              --shard-iterator-type TRIM_HORIZON \
              --stream-name ${KINESIS_STREAM_OUTPUT} \
              --query 'ShardIterator' \
      )
      
      RESULT=$(aws kinesis get-records --shard-iterator $SHARD_ITERATOR)
      
      echo ${RESULT} | jq -r '.Records[0].Data' | base64 --decode
      ``` 
18. Run the test
    ```bash
      export PREDICTIONS_STREAM_NAME="ride_predictions"
      export RUN_ID="e1efc53e9bd149078b0c12aeaa6365df"
      export TEST_RUN="True"
      
      python test.py
      ```
19. Then, we make the new python file (lambda_function.py) and package all the lambda function in it.
20. Also, we set up the dockerFile so we can run it in our virtual environment
    
    ```bash
      docker run -it --rm \
          -p 8080:8080 \
          -e PREDICTIONS_STREAM_NAME="ride_predictions" \
          -e RUN_ID="e1efc53e9bd149078b0c12aeaa6365df" \
          -e TEST_RUN="True" \
          -v c:/Users/alexe/.aws:/root/.aws \
          stream-model-duration:v1
      ```
22. Afterwards, we use the ECR to run the image in AWS

    Creating an ECR repo
    ```bash
      aws ecr create-repository --repository-name duration-model
      ```

    Logging in
    ```bash
      $(aws ecr get-login --no-include-email)
      ```
23. We run the remote image command in the terminal and it will take a time to download and send the model from our AWS S3
    
    ```bash
      REMOTE_URI="387546586013.dkr.ecr.eu-west-1.amazonaws.com/duration-model"
      REMOTE_TAG="v1"
      REMOTE_IMAGE=${REMOTE_URI}:${REMOTE_TAG}
      
      LOCAL_IMAGE="stream-model-duration:v1"
      docker tag ${LOCAL_IMAGE} ${REMOTE_IMAGE}
      docker push ${REMOTE_IMAGE}
      ```
24. Then, we create the function and delete the last function (to avoid the lambda will deploy both function)
25. Add environment variable (PREDICTIONS_STREAM_NAME and RUN_ID)
26. Then, we create the policy for our s3 as services, so we will set all list and read permission. Prepare the s3 bucket's name to be set up on our policy
27. Gives more time for processing so we will increase the droptime (3 second at first)
28. Use the shard iterator again to specifies the position which start reading the stream

## 6.Model monitoring

### 6.1 Dummy Monitoring and Data Quality Monitoring
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
7. Create the dummy quality test Python following the same idea as the previous one to create the visualization diagrams
8. Make sure to save your Grafana dashboard so it will not disappear after you cut the connection off. 

### 6.2 Test Suites and Reports
This method will show us the report in the comfy model which we can read it clearly and neatly. You can easily check several indicator that will assess the quality of our model.

<img width="819" alt="image" src="https://github.com/Irf4n-Muhammad/MLOPS-Project-Youtube-Trending/assets/121205860/35d4ad1b-0f19-440a-950e-fe4a389287f7">

We can also generate the JSON file data and retrieve the needed information by aiming for the right location in JSON file.

<img width="828" alt="image" src="https://github.com/Irf4n-Muhammad/MLOPS-Project-Youtube-Trending/assets/121205860/a1ad86ef-9eb0-4519-8cba-6985c8051c2b">



## 8. Best practices

- [x] There are unit tests (1 point)
- [x] There is an integration test (1 point)
- [x] Linter and/or code formatter are used (1 point)
- [x] There's a Makefile (1 point)
- [x] There are pre-commit hooks (1 point)
- [x] There's a CI/CD pipeline (2 points)

### 8.1 Unit Tests
So we gonna test our function in running model file by using the pytest and we will see if the result is as expected

1. Set up the model.py to store our function for machine learning model to predict our case
2. Create the tests folder and create model_test.py as our test file that link to the model.py
3. Now, set the terminal to prepare the pytest
4. Download the pipenv shell
   
    ```bash
    pipenv shell
    ```
6. Type PS1="> "
   
    ```bash
    PS1="> "
    ```
7. Type which pytest
   
   ```bash
    which pytest
    ```
8. CLick CTRL P + Shift
9. Select python interpreter, click unit test and click tests folder
10. Now, on the model.py, write all function that need for our machine learning
11. On the model_test type all the function and the variable as our test model
12. If we use lambda in our workflow, the create lambda_function to test the lambda
13. Create the Dockerfile
    
    ```bash
    docker build -t stream-model-duration:v2 .
    ```
14. Write the test_docker to test the activeness of our Dockerfile
15. Now you can run the test for all function using tests

    ```bash
    pipenv run pytests tests/
    ```

### 8.2 Integration Test:
So in this test we will try to use the docker-compose to running the test and check for the quality of our model

1. Prepare the test_docker.py
2. Put the expected response on that file to be comparing with the actual response from event kinesis records
3. We will use assert to compare both result
4. Now create the docker-compose.yaml to set up the environment, so we will activate all of that using docker-compose command
5. Also, we create the run.sh to put everything about the response of our test
6. To activate the test first run the docker compose
   
   ```bash
   docker-compose up
   ```
7. Acitvate the run.sh afterward in the same terminal or test_docker.py to check the docker activation using different terminal
   
   ```bash
   ./run.sh
   ```

   ```bash
   pipenv run python test_docker.py
   ```
    
### 8.6 CI/CD Pipeline
So in this case we will use GitHub to execute the CI/CD pipeline. If you wonder what the pipeline looks like, you can scroll up to the early page and you will find the pipeline image.

### 8.6.1 Continuous Integration Workflow
- Automate sections from tests: Env setup, Unit test, Integration test, Terraform plan
- Create a CI workflow to trigger on pull-request to develop branch
- Execute demo

1. Create the ci-tests.yaml to make the sequence of the pipeline
2. Write all the pipeline like with the format like terraform
3. Create prod.tfvars to store our variable for the pipeline
4. Know we try to push the origin into the github
5. Type this to commit
   ```bash
   git add .
   git commit -m "CI/CD pipeline commit"
   git push origin <branch>
   ```
6. Open the github setting and put the credentials for AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY
7. Create the pull request
8. Check the action and open test in the ci-test.yaml
9. If it succeed then you did it

### 8.6.2 Continuous Deployment

