import streamlit as st
import pandas as pd
from pymongo import MongoClient
import plotly.express as px

MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "hospital_appointment_db"

st.set_page_config(
    page_title="Hospital Appointment Analytics",
    page_icon="🏥",
    layout="wide"
)

st.title("Hospital Appointment Data Pipeline")
st.caption("NoSQL-based hospital appointment analytics")

@st.cache_data(ttl=30)
def load_data():
    client = MongoClient(
        MONGO_URI,
        serverSelectionTimeoutMS=3000
    )
    client.admin.command("ping")

    db = client[DB_NAME]
    records = list(
        db["appointments"].find({}, {"_id": 0})
    )

    client.close()
    return pd.DataFrame(records)

try:
    df = load_data()
except Exception:
    st.error(
        "MongoDB connection failed. Start MongoDB and run "
        "`python pipeline.py` before opening the dashboard."
    )
    st.stop()

if df.empty:
    st.warning("No appointment records found. Run pipeline.py first.")
    st.stop()

if "appointment_date" in df.columns:
    df["appointment_date"] = pd.to_datetime(
        df["appointment_date"], errors="coerce"
    )

# Sidebar filters
st.sidebar.header("Dashboard Filters")

filtered = df.copy()

if "department" in df.columns:
    departments = sorted(
        df["department"].dropna().unique().tolist()
    )
    selected_departments = st.sidebar.multiselect(
        "Department",
        departments,
        default=departments
    )
    filtered = filtered[
        filtered["department"].isin(selected_departments)
    ]

if "status" in df.columns:
    statuses = sorted(
        df["status"].dropna().unique().tolist()
    )
    selected_statuses = st.sidebar.multiselect(
        "Appointment Status",
        statuses,
        default=statuses
    )
    filtered = filtered[
        filtered["status"].isin(selected_statuses)
    ]

# KPI cards
c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Appointments", len(filtered))

if "status" in filtered.columns:
    c2.metric(
        "Completed",
        int((filtered["status"] == "Completed").sum())
    )
    c3.metric(
        "Cancelled",
        int((filtered["status"] == "Cancelled").sum())
    )
    c4.metric(
        "No-Show",
        int((filtered["status"] == "No-Show").sum())
    )

st.divider()

# Status + department
left, right = st.columns(2)

with left:
    if "status" in filtered.columns:
        status_count = (
            filtered["status"]
            .value_counts()
            .reset_index()
        )
        status_count.columns = ["Status", "Count"]

        fig = px.pie(
            status_count,
            names="Status",
            values="Count",
            title="Appointment Status Distribution"
        )
        st.plotly_chart(
            fig,
            use_container_width=True
        )

with right:
    if "department" in filtered.columns:
        dept_count = (
            filtered["department"]
            .value_counts()
            .reset_index()
        )
        dept_count.columns = ["Department", "Count"]

        fig = px.bar(
            dept_count,
            x="Department",
            y="Count",
            title="Appointments by Department"
        )
        st.plotly_chart(
            fig,
            use_container_width=True
        )

# Monthly + doctor
left, right = st.columns(2)

with left:
    if "appointment_month" in filtered.columns:
        monthly = (
            filtered["appointment_month"]
            .value_counts()
            .sort_index()
            .reset_index()
        )
        monthly.columns = ["Month", "Appointments"]

        fig = px.line(
            monthly,
            x="Month",
            y="Appointments",
            markers=True,
            title="Monthly Appointment Trend"
        )
        st.plotly_chart(
            fig,
            use_container_width=True
        )

with right:
    if "doctor_name" in filtered.columns:
        doctors = (
            filtered["doctor_name"]
            .value_counts()
            .head(10)
            .reset_index()
        )
        doctors.columns = ["Doctor", "Appointments"]

        fig = px.bar(
            doctors,
            x="Appointments",
            y="Doctor",
            orientation="h",
            title="Top Doctors by Appointment Count"
        )
        st.plotly_chart(
            fig,
            use_container_width=True
        )

st.subheader("Processed Appointment Records")
st.dataframe(
    filtered,
    use_container_width=True,
    hide_index=True
)
