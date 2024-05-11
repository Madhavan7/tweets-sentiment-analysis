from fastapi import FastAPI
from typing import Annotated
from pydantic import BaseModel
from doc2vec.model import Doc2VecModel

model = Doc2VecModel(3)

app = FastAPI()

class Text(BaseModel):
  text:str

@app.post("/sentiment/")
def get_prediction(text : Text):
  text_dict = text.model_dump()
  prediction = model.predict(text_dict["text"])
  print(text_dict["text"])
  return {'prediction': prediction}
