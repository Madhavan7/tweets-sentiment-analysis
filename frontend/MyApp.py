import streamlit as st
import requests
import os

MODEL_DNS = os.environ.get("DOC2VEC_DNS")
PORT = os.environ.get("PORT")

url = f"http://{MODEL_DNS}:{PORT}/sentiment/"
text_input = st.text_input(label="sentiment", max_chars=2500, type="default", label_visibility="hidden")
prediction_title = st.text("Write something to get a prediction")

if text_input:
  payload = {
    "text": text_input
  }
  response = requests.post(url=url, json=payload)
  prediction = response.json()["prediction"]
  st.write(prediction)