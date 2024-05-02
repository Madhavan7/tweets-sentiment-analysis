VARIABLE=$(docker ps -a --filter "name=mlflow-tracking-server")

if [ -n "$VARIABLE" ]; 
then 
  echo "container is going to stop" 
  docker stop mlflow-tracking-server 
  docker rm mlflow-tracking-server 
fi 

aws ecr get-login-password --region $REGION | docker login --username AWS --password-stdin $ECR_PASSWORD
docker pull $IMAGE 
docker run  -dit --name mlflow-tracking-server -p 5000:5000 $IMAGE