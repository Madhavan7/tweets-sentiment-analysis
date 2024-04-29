FROM ubuntu/mlflow:2.1.1_1.0-22.04

ARG DB_USER_ARG
ARG DB_PASSWORD_ARG
ARG DB_ENDPOINT_ARG
ARG DB_NAME_ARG
ARG S3_BUCKET_NAME_ARG

ENV DB_USER=${DB_USER_ARG}
ENV DB_PASSWORD=${DB_PASSWORD_ARG}
ENV DB_ENDPOINT=${DB_ENDPOINT_ARG}
ENV DB_NAME=${DB_NAME_ARG}
ENV S3_BUCKET_NAME=${S3_BUCKET_NAME_ARG}

RUN apt update && \ 
         pip3 install boto3 \
         pip3 install psycopg2-binary==2.9.9

CMD ["mlflow", "server", "-h", "0.0.0.0", "-p", "5000", "--backend-store-uri", "postgresql://${DB_USER}:${DB_PASSWORD}@${DB_ENDPOINT}:5432/${DB_NAME}", "--default-artifact-root", "${S3_BUCKET_NAME}", "--serve-artifacts"]