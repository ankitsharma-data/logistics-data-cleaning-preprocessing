import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
RAW_FILE = DATA_DIR / "logistics_data.csv"
CLEAN_FILE = DATA_DIR / "logistics_data_cleaned.csv"


def cap_iqr(series: pd.Series) -> pd.Series:
    """Cap extreme values using the IQR rule while retaining observations."""
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return series.clip(lower=lower, upper=upper)


def preprocess() -> pd.DataFrame:
    df = pd.read_csv(RAW_FILE)

    print("Initial shape:", df.shape)
    print("Initial duplicate rows:", df.duplicated().sum())
    print("Missing values before cleaning:\n", df.isna().sum())

    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
    )

    for col in ["origin", "destination", "transport_mode", "status", "traffic", "weather"]:
        df[col] = df[col].astype("string").str.strip().str.title()

    for col in ["shipment_date", "delivery_date"]:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    numeric_cols = ["distance_km", "weight_kg", "inventory_units", "shipping_cost"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(
            df[col].astype("string").str.replace(r"[^0-9.-]", "", regex=True),
            errors="coerce",
        )

    df = df.drop_duplicates(subset=["shipment_id"], keep="first")

    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())

    for col in ["origin", "destination", "transport_mode", "status", "traffic", "weather"]:
        df[col] = df[col].fillna("Unknown")

    df["shipping_duration_days"] = (
        df["delivery_date"] - df["shipment_date"]
    ).dt.days
    df["shipping_duration_days"] = df["shipping_duration_days"].fillna(
        df["shipping_duration_days"].median()
    )

    for col in ["distance_km", "weight_kg", "inventory_units", "shipping_cost", "shipping_duration_days"]:
        df[col] = cap_iqr(df[col])

    df = df.sort_values("shipment_id").reset_index(drop=True)
    df.to_csv(CLEAN_FILE, index=False)

    print("\nCleaned shape:", df.shape)
    print("Duplicate shipment IDs after cleaning:", df["shipment_id"].duplicated().sum())
    print("Missing values after cleaning:\n", df.isna().sum())
    print(f"\nCleaned dataset saved to: {CLEAN_FILE}")

    return df


if __name__ == "__main__":
    preprocess()
