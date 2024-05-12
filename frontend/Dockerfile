FROM python:3.10

ARG DOC2VEC_DNS_ARG
ARG PORT_ARG

ENV DOC2VEC_DNS=${DOC2VEC_DNS_ARG}
ENV PORT=${PORT_ARG}

COPY frontend/__init__.py /frontend/__init__.py
COPY frontend/MyApp.py /frontend/MyApp.py
COPY frontend/requirements.txt /frontend/requirements.txt

RUN pip3 install -r /frontend/requirements.txt

EXPOSE 8501

CMD ["streamlit", "run","--server.port", "8501", "/frontend/MyApp.py"]