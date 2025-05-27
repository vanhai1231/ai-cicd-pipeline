import mlflow
import random

mlflow.set_experiment("demo-ai-cicd")

with mlflow.start_run():
    acc = random.uniform(0.7, 0.95)
    mlflow.log_metric("accuracy", acc)
    print("Accuracy logged:", acc)
