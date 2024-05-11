FROM python:3.10

ARG TRACKING_SERVER_HOST_ARG
ARG PORT_ARG

ENV TRACKING_SERVER_HOST=${TRACKING_SERVER_HOST_ARG}
ENV PORT=${PORT_ARG}

WORKDIR /code

COPY doc2vec/requirements.txt /doc2vec/requirements.txt
COPY doc2vec/__init__.py /doc2vec/__init__.py
COPY doc2vec/model.py /doc2vec/model.py
COPY doc2vec/main.py /doc2vec/main.py

RUN  pip3 install -r /doc2vec/requirements.txt

EXPOSE 80

CMD ["fastapi", "run", "/doc2vec/main.py", "--port", "80"]
