import os
import mlflow

TRACKING_SERVER_HOST = os.environ.get('TRACKING_SERVER_HOST')

mlflow.set_tracking_uri(f"http://{TRACKING_SERVER_HOST}:5000")
print(f"tracking URI: '{mlflow.get_tracking_uri()}'")
def get_run_id_best_model(experiment_name="doc2vec experiment"):
  return mlflow.search_runs(
    experiment_names=[experiment_name],
    max_results=1,
    order_by=["metrics.accuracy DESC"],
  )['run_id'][0]

get_run_id_best_model()