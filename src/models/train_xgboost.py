from xgboost import XGBClassifier
import numpy as np

def train_xgboost(X_train, y_train):

    pos = np.sum(y_train == 1)
    neg = np.sum(y_train == 0)

    scale_pos_weight = neg / pos if pos > 0 else 1.0

    model = XGBClassifier(
        n_estimators=200,
        max_depth=4,
        learning_rate=0.05,
        subsample=0.8,
        colsample_bytree=0.8,
        scale_pos_weight=scale_pos_weight,
        eval_metric="logloss",
        random_state=42,
        use_label_encoder=False
    )

    model.fit(X_train, y_train)
    return model