import pandas as pd


def generate_priority(df):

    df = df.copy()

    # -------------------------
    # Status Score
    # -------------------------

    status_scores = {
        "Open": 40,
        "In Progress": 25,
        "Long Term Solution": 20,
        "Completed": 5,
        "Closed": 0
    }

    df["Status_Score"] = (
        df["Status"]
        .map(status_scores)
        .fillna(10)
    )

    # -------------------------
    # Type of roads
    # -------------------------
    road_scores = {
    "Main Road": 20,
    "Major Road": 15,
    "Minor Road": 10,
    "Residential": 5
    }

    df["Road_Score"] = (
    df["Type_of_Ro"]
    .map(road_scores)
    .fillna(8)
    )

    # -------------------------
    # Complaint Age Score
    # -------------------------

    df["Open_Date"] = pd.to_datetime(
        df["Open_Date"],
        errors="coerce"
    )

    today = pd.Timestamp.today()

    df["Days_Open"] = (
        today - df["Open_Date"]
    ).dt.days.fillna(0)

    # Maximum 30 points
    df["Age_Score"] = (
    df["Days_Open"] / 180 * 30
    ).clip(upper=30)

    # -------------------------
    # Estimated Cost
    # -------------------------

    df["Total_Esti"] = pd.to_numeric(
        df["Total_Esti"],
        errors="coerce"
    ).fillna(0)

    # Maximum 30 points
    df["Cost_Score"] = (
    df["Total_Esti"] / 50000 * 30
    ).clip(upper=30)

    # -------------------------
    # Final Priority Index (0-100)
    # -------------------------
    df["Priority Score"] = (
    df["Status_Score"]
    + df["Age_Score"]
    + df["Cost_Score"]
    + df["Road_Score"]
    ).clip(upper=100).round(1)

    
    # -------------------------
    # Recommendation
    # -------------------------

    def recommendation(score):

        if score >= 85:
            return "🔴 Immediate Repair"

        elif score >= 70:
            return "🟠 High Priority"

        elif score >= 50:
            return "🟡 Medium Priority"

        else:
            return "🟢 Low Priority"

    df["Recommendation"] = df["Priority Score"].apply(
        recommendation
    )

    df = df.sort_values(
        "Priority Score",
        ascending=False
    )

    df["Priority Score"] = df["Priority Score"].round(1)

    return df[
        [
            "Ward_Name",
            "Status",
            "Total_Esti",
            "Priority Score",
            "Recommendation"
        ]
    ].head(10)

