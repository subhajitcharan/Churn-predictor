from pathlib import Path
import joblib
model_path=Path(__file__).resolve().parent / "model.pkl"
scaler_path=Path(__file__).resolve().parent/"scaler.pkl"
def load_model():
    return joblib.load(model_path)
def load_scaler():
    return joblib.load(scaler_path)
