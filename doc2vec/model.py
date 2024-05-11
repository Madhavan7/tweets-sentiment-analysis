import os

# import mlflow.artifacts
# import mlflow.pyfunc
import mlflow
import torch
from torch import Tensor
from gensim.utils import simple_preprocess

TRACKING_SERVER_HOST = os.environ.get('TRACKING_SERVER_HOST')
PORT = os.environ.get('PORT')

mlflow.set_tracking_uri(f"http://{TRACKING_SERVER_HOST}:{PORT}")
print(TRACKING_SERVER_HOST)
class Doc2VecModel:

  def __init__(self, model_version = 3) -> None:
    self.model_version = model_version
    self.id2label = {0:"Positive", 1:"Neutral", 2:"Negative"}

    self.embedding_model_uri = f"models:/doc2vec_doc_embedding/{self.model_version}"
    self.embedding_model = mlflow.pyfunc.load_model(model_uri=self.embedding_model_uri)

    self.classification_model_uri = f"models:/doc2vec_classification/{self.model_version}"
    self.classification_model = mlflow.pytorch.load_model(model_uri=self.classification_model_uri)

  def predict(self, tweet):
    #returns a pytorch tensor with the predictions
    data = Tensor(self.embedding_model.predict(data=simple_preprocess(tweet)))
    data = data.unsqueeze(0)
    self.classification_model.eval()
    with torch.no_grad():
      predictions = self.classification_model(data)[0]
      predictions = torch.argmax(predictions.to('cpu'))
      predictions = int(predictions.item())
    predictions = self.id2label[predictions]
    return predictions

  def set_dependencies(self):
    mlflow.artifacts.download_artifacts(artifact_uri=f"{self.embedding_model_uri}/requirements.txt", dst_path = "doc2vec/embedding_requirements")
    mlflow.artifacts.download_artifacts(artifact_uri=f"{self.classification_model_uri}/requirements.txt", dst_path = "doc2vec/classification_requirements")

if __name__ == '__main__':
  model = Doc2VecModel(3)
  print(model.predict("this is a tweet"))
  print(model.predict("i am very sad"))
  print(model.predict("I love my life"))
  model.set_dependencies()
