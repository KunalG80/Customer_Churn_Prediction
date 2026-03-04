import pandas as pd

def fix_numeric_types(pipeline, df):

    preprocess = pipeline.named_steps["preprocess"]

    num_cols = []

    for name, transformer, cols in preprocess.transformers_:
        if name == "num":
            num_cols = cols

    df = df.copy()

    for col in num_cols:

        if col in df.columns:

            df[col] = (
                df[col]
                .astype(str)
                .str.replace(" ", "")
            )

            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            )

    return df