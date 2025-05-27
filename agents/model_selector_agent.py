import mlflow

runs = mlflow.search_runs(experiment_ids=["0"], order_by=["metrics.accuracy DESC"])

if runs.empty:
    print("Không tìm thấy bất kỳ run nào trong MLflow.")
    exit(1)

best_run = runs.iloc[0]
print("AI Agent chọn model tốt nhất:")
print("Run ID:", best_run.run_id)
print("Accuracy:", best_run.metrics["accuracy"])

with open("model_to_deploy.txt", "w") as f:
    f.write(best_run.run_id)
