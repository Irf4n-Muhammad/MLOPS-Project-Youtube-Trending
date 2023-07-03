# MLOPS Project / Youtube Spotify Trending

## 1.Problem description
YouTube and Spotify have been recognized as the most frequently visited platforms globally, serving as primary channels through which individuals not only amass wealth but also cultivate widespread fame. A "trending" status on these platforms is often viewed as the pinnacle of achievement for content creators, indicating that their content has gained significant popularity within a certain time frame. To achieve this status, it is crucial to understand the variables that can influence this outcome. This understanding can subsequently guide a systematic plan for trending.

In this advanced machine learning model, we intend to examine two principal factors: the number of viewers and licensing agreements. The choice of these two variables is not arbitrary. The number of viewers directly signifies the popularity of the content, while licensing deals could potentially broaden the reach of the content, hence leading to increased viewership and likelihood of trending.

We hypothesize that licensed content may generate a wider audience, which in turn, influences the trending status of the content. However, it is important to note that these factors are just a fraction of a larger set of parameters that could impact a content's trendiness. These other factors might include content quality, content type, publication time, among others. Nevertheless, for the scope of this project, our primary focus is to build a sustainable machine learning model, and hence, we are limiting our study to these two factors.

It is imperative to highlight the need for regular maintenance and testing of this machine learning model. This is crucial to ensure its robustness and reliability, especially given that user behavior and consumption patterns on platforms like YouTube and Spotify are dynamic and can change rapidly. Regular monitoring and testing will allow us to identify any anomalies, adapt to pattern shifts, and ensure that the predictive model remains reliable and trustworthy.

Further, to manage the sustainability of our machine learning model, we will incorporate practices such as model validation, updating the training data, and employing a robust monitoring system to track the model's performance over time. This sustainable machine learning environment will enable the model to remain sensitive to emerging trends, thereby allowing it to maintain its accuracy in predicting trending status based on viewer numbers and licensing agreements. By this method, we are not just establishing a one-time solution but building a resilient, evolving model that can adapt to the ever-changing digital landscape.


## 2. Cloud
For this project, we will use AWS cloud to intergrate our model for storing and transforming the model. But before that, we need to set up the terraform to set up the setting for our AWS Cloud, but this section will assume that we have finished using terraform.

### Create the Root:
1. Use your gmail to create the root account
2. You gonna use this as main account that will be integrated to many user account

### Create the User:
1. Open the IAM features and click user
2. Create the new user
3. Make your username
4. Create new group and click the policy that we need (AWSS3FullService, AdministratorAccess)
5. Create the user
6. You will find the AWS key and also the AWS secret key. Don't forget to copy your AWS secret key and your key because it will be important for aws configuration. Also, download the csv file.
7. Logout from root account and connect to the user account using AccountID and password
8. Now, your user account was set up

### - Using AWS S3 (Storing Model)
1. Open the s3 features
2. Create the new bucket
3. Write your s3 bucket name. Make it authentic which show what this bucket related to
4. Choose the timezone that close to your livinghood.
5. Create the bucket and your bucket is ready

### - Create the RDS Database (Storing Model)
1. Open the RDS features
2. Create the databse
3. Choose PostgreSQL and choose free tier
4. Mkae your DB name on 'DB Instance Identifier'
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

19. 




Experiment tracking and model registry

Workflow orchestration

Model deployment

Model monitoring

Reproducibility

Best practices
 There are unit tests (1 point)
 There is an integration test (1 point)
 Linter and/or code formatter are used (1 point)
 There's a Makefile (1 point)
 There are pre-commit hooks (1 point)
 There's a CI/CD pipeline (2 points)
