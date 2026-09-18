import os
import pandas as pd
from pymongo import MongoClient, ASCENDING

MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "hospital_appointment_db"
DATA_DIR = "data"

def load_raw_data():
    """Data ingestion: read available CSV and JSON files."""
    frames = []

    csv_path = os.path.join(DATA_DIR, "appointments.csv")
    json_path = os.path.join(DATA_DIR, "appointments.json")

    if os.path.exists(csv_path):
        frames.append(pd.read_csv(csv_path))

    if os.path.exists(json_path):
        frames.append(pd.read_json(json_path))

    if not frames:
        raise FileNotFoundError(
            "No input file found. Add appointments.csv or appointments.json to data/"
        )

    return pd.concat(frames, ignore_index=True)

def clean_data(df):
    """Remove duplicates, handle missing values and clean fields."""
    df = df.copy()

    # Standardise column names
    df.columns = [
        c.strip().lower().replace(" ", "_") for c in df.columns
    ]

    # Remove exact duplicates
    df = df.drop_duplicates()

    # Remove duplicate appointment IDs
    if "appointment_id" in df.columns:
        df = df.drop_duplicates(subset=["appointment_id"])

    # Text fields
    text_columns = [
        "patient_name", "gender", "doctor_name", "department", "status"
    ]

    for col in text_columns:
        if col in df.columns:
            df[col] = (
                df[col]
                .fillna("Unknown")
                .astype(str)
                .str.strip()
            )

    # Numeric field
    if "age" in df.columns:
        df["age"] = pd.to_numeric(df["age"], errors="coerce")
        if df["age"].notna().any():
            df["age"] = df["age"].fillna(df["age"].median())
        else:
            df["age"] = df["age"].fillna(0)

    # Date fields
    for col in ["booking_date", "appointment_date"]:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    # Appointment date is essential
    if "appointment_date" in df.columns:
        df = df.dropna(subset=["appointment_date"])

    # Standardise appointment status
    if "status" in df.columns:
        status_map = {
            "completed": "Completed",
            "complete": "Completed",
            "cancelled": "Cancelled",
            "canceled": "Cancelled",
            "no-show": "No-Show",
            "no show": "No-Show",
            "noshow": "No-Show"
        }

        lower_status = df["status"].str.lower()
        df["status"] = (
            lower_status.map(status_map)
            .fillna(df["status"].str.title())
        )

    return df

def feature_engineering(df):
    """Create analytical features."""
    df = df.copy()

    if "booking_date" in df.columns and "appointment_date" in df.columns:
        df["lead_time"] = (
            df["appointment_date"] - df["booking_date"]
        ).dt.days

    if "appointment_date" in df.columns:
        df["appointment_month"] = (
            df["appointment_date"].dt.strftime("%Y-%m")
        )
        df["appointment_day"] = (
            df["appointment_date"].dt.day_name()
        )

    if "appointment_time" in df.columns:
        df["appointment_time"] = (
            df["appointment_time"].fillna("Unknown").astype(str)
        )

    return df

def convert_to_mongodb_records(df):
    """Convert DataFrame rows into MongoDB-compatible documents."""
    records_df = df.copy()

    for col in records_df.columns:
        if pd.api.types.is_datetime64_any_dtype(records_df[col]):
            records_df[col] = records_df[col].dt.strftime("%Y-%m-%d")

    records_df = records_df.where(pd.notna(records_df), None)

    return records_df.to_dict(orient="records")

def store_in_mongodb(df):
    """Load transformed data into MongoDB NoSQL collections."""
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)

    # Test connection
    client.admin.command("ping")

    db = client[DB_NAME]

    appointments = db["appointments"]
    patients = db["patients"]
    doctors = db["doctors"]

    # Replace old appointment dataset for repeatable demonstrations
    appointments.delete_many({})

    appointment_records = convert_to_mongodb_records(df)

    if appointment_records:
        appointments.insert_many(appointment_records)

    # Patient collection
    if "patient_id" in df.columns:
        patient_columns = [
            c for c in [
                "patient_id", "patient_name", "age", "gender"
            ] if c in df.columns
        ]

        patient_df = (
            df[patient_columns]
            .drop_duplicates(subset=["patient_id"])
        )

        patients.delete_many({})

        patient_records = convert_to_mongodb_records(patient_df)
        if patient_records:
            patients.insert_many(patient_records)

    # Doctor collection
    if "doctor_id" in df.columns:
        doctor_columns = [
            c for c in [
                "doctor_id", "doctor_name", "department"
            ] if c in df.columns
        ]

        doctor_df = (
            df[doctor_columns]
            .drop_duplicates(subset=["doctor_id"])
        )

        doctors.delete_many({})

        doctor_records = convert_to_mongodb_records(doctor_df)
        if doctor_records:
            doctors.insert_many(doctor_records)

    # NoSQL indexes
    appointments.create_index(
        [("appointment_id", ASCENDING)], unique=True
    )
    appointments.create_index([("status", ASCENDING)])
    appointments.create_index(
        [("department", ASCENDING), ("status", ASCENDING)]
    )

    client.close()

def run_pipeline():
    print("1. Loading raw data...")
    raw = load_raw_data()
    print(f"   Raw records: {len(raw)}")

    print("2. Cleaning data...")
    cleaned = clean_data(raw)
    print(f"   Records after cleaning: {len(cleaned)}")

    print("3. Creating features...")
    transformed = feature_engineering(cleaned)

    print("4. Saving cleaned data...")
    output_path = os.path.join(DATA_DIR, "cleaned_appointments.csv")
    transformed.to_csv(output_path, index=False)

    print("5. Loading data into MongoDB...")
    store_in_mongodb(transformed)

    print("\nPipeline completed successfully.")
    print(f"MongoDB database: {DB_NAME}")
    print("Collections: appointments, patients, doctors")
    print(f"Cleaned file: {output_path}")

if __name__ == "__main__":
    run_pipeline()
