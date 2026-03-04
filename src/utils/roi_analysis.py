def roi_vs_threshold(
    df,
    retention_cost,
    retention_success_rate,
    months_lost
):

    results = []

    for t in [i/10 for i in range(1,9)]:

        subset = df[df["Churn_Probability"] > t]

        if subset.empty:
            continue

        loss = subset["MonthlyCharges"].sum() * months_lost
        saved = (
            subset["MonthlyCharges"].sum()
            * retention_success_rate
            * months_lost
        )

        net = saved - (len(subset) * retention_cost)

        results.append({
            "threshold": t,
            "net_roi": net
        })

    return results