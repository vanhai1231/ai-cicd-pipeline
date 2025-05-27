import mlflow

# Lấy danh sách runs theo accuracy giảm dần
runs = mlflow.search_runs(experiment_ids=["0"], order_by=["metrics.accuracy DESC"])
best_run = runs.iloc[0]
print("AI Agent chọn model tốt nhất:")
print("Run ID:", best_run.run_id)
print("Accuracy:", best_run.metrics["accuracy"])

# Ghi vào file nếu cần
with open("model_to_deploy.txt", "w") as f:
    f.write(best_run.run_id)
