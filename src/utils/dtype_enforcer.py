import pandas as pd


def enforce_training_dtypes(uploaded, trained):

    for col in trained.columns:

        if col not in uploaded.columns:
            continue

        if trained[col].dtype in ["float64", "int64"]:

            uploaded[col] = (
                uploaded[col]
                .astype(str)
                .str.replace(r"[^\d\.]", "", regex=True)
            )

            uploaded[col] = pd.to_numeric(
                uploaded[col],
                errors="coerce"
            )

        else:
            uploaded[col] = uploaded[col].astype(str)

    return uploaded