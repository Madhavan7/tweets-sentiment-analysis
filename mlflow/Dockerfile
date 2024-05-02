FROM python:3.10

ARG DB_NAME_ARG
ARG DB_PASSWORD_ARG
ARG DB_ENDPOINT_ARG
ARG DB_USER_ARG
ARG S3_BUCKET_NAME_ARG

ENV DB_NAME_ARG=DB_NAME
ENV DB_PASSWORD=DB_PASSWORD_ARG
ENV DB_ENDPOINT=DB_ENDPOINT_ARG
ENV DB_USER=DB_USER_ARG
ENV S3_BUCKET_NAME=S3_BUCKET_NAME_ARG

COPY requirements.txt /

RUN pip install -r /requirements.txt

CMD ["mlflow", "server", "-h", "0.0.0.0", "-p", "5000", "--backend-store-uri", "postgresql://${DB_USER}:${DB_PASSWORD}@${DB_ENDPOINT}:5432/${DB_NAME}", "--default-artifact-root", "s3://${S3_BUCKET_NAME}"]