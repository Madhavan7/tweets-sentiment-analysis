# tweets-sentiment-analysis

Problem: The challenge is to perform sentiment analysis on a dataset obtained from kaggle. The dataset consisted of 10,237 tweets, and each tweet was given a label "Positive", "Negative" or "Neutral". There was 3472, 3757, and 3053 positive, negative and neutral tweets respectively.

The model used was a modified doc2vec model - a fully connected layer was added to the doc2vec model to get the predictions. The Gensim and Pytorch libraries were used for creating the model


# Deployment Architecture

Model training was done on a Sagemaker notebook instance. An Mlflow tracking server container was hosted on ECS, and this ECS service was used to track run metrics, metadata and artifacts of all the experiments in the sagemaker notebook. For this, it was connected to a Postgres database on RDS(to track metrics), and an S3 bucket to store artifacts. A Flask app container was used to serve the model as an api, and a Streamlit container was used to serve the frontend. Both containers were hosted on an ECS cluster

![wcd-project-diagram-Page-2 drawio](https://github.com/Madhavan7/tweets-sentiment-analysis/assets/59711147/64bcf18d-a1ca-4e1c-9161-b46075a98c29)

