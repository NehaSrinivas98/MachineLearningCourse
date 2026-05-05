import argparse
import mlflow
import mlflow.sklearn
from mlflow.data import from_pandas

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# -----------------------------
# Step 0: Parse CLI arguments
# -----------------------------
parser = argparse.ArgumentParser()

parser.add_argument("--n_estimators", type=int, required=True)
parser.add_argument("--max_depth", type=int, required=True)

args = parser.parse_args()

# -----------------------------
# Step 1: Dataset
# -----------------------------
data = pd.DataFrame({
    "experience": [1, 2, 3, 4, 5, 6, 7, 8],
    "salary": [30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
})

X = data[["experience"]]
y = data["salary"]

dataset = from_pandas(data, source="sample_data")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# -----------------------------
# Step 2: MLflow setup
# -----------------------------
mlflow.set_experiment("cli-mlflow-demo")

with mlflow.start_run():

    # Log dataset
    mlflow.log_input(dataset, context="training")

    # Log parameters from CLI
    mlflow.log_param("n_estimators", args.n_estimators)
    mlflow.log_param("max_depth", args.max_depth)

    # -----------------------------
    # Step 3: Train model
    # -----------------------------
    model = RandomForestRegressor(
        n_estimators=args.n_estimators,
        max_depth=args.max_depth
    )

    model.fit(X_train, y_train)

    # -----------------------------
    # Step 4: Evaluate
    # -----------------------------
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)

    mlflow.log_metric("mse", mse)

    # Log model
    mlflow.sklearn.log_model(model, "model")

    print(f"Params: n_estimators={args.n_estimators}, max_depth={args.max_depth}")
    print(f"MSE: {mse}")