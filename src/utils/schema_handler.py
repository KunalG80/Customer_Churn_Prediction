import pandas as pd
import joblib

def align_schema(df):

    model = joblib.load("models/churn_model.pkl")

    expected = model.named_steps[
        "preprocess"
    ].feature_names_in_

    for col in expected:
        if col not in df.columns:
            df[col] = "Unknown"

    df = df[expected]

    return df