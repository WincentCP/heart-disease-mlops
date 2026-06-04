import os
import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
import mlflow
import mlflow.sklearn

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n_estimators", type=int, default=100)
    parser.add_argument("--max_depth", type=int, default=5)
    args = parser.parse_args()
    
    # MLProject executes inside conda or locally. Set tracking URI if not configured.
    if not mlflow.is_tracking_uri_set():
        mlflow.set_tracking_uri("http://localhost:5000")
    
    with mlflow.start_run() as run:
        # Load dataset
        script_dir = os.path.dirname(os.path.abspath(__file__))
        data_path = os.path.join(script_dir, 'namadataset_preprocessing', 'heart_preprocessed.csv')
        
        df = pd.read_csv(data_path)
        X = df.drop(columns=['target'])
        y = df['target']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Log parameters
        mlflow.log_param("n_estimators", args.n_estimators)
        mlflow.log_param("max_depth", args.max_depth)
        
        # Train model
        model = RandomForestClassifier(n_estimators=args.n_estimators, max_depth=args.max_depth, random_state=42)
        model.fit(X_train, y_train)
        
        # Predictions and evaluations
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        
        # Log metrics
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("f1_score", f1)
        
        # Save model
        mlflow.sklearn.log_model(model, "model")
        print(f"Workflow-CI run complete. Test Acc: {accuracy:.4f}, F1: {f1:.4f}")

if __name__ == '__main__':
    main()
