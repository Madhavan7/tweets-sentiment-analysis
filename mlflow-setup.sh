VARIABLE=$(docker ps -q --filter "name=mlflow-tracking-server")

if [ -n "$VARIABLE" ]; 
then 
  echo "container is going to stop" 
  docker stop mlflow-tracking-server 
  docker rm mlflow-tracking-server 
fi 

docker pull $IMAGE 
docker run -d --name mlflow-tracking-server -p 5000:5000 $IMAGE
exit 0