# Automated Healthcare Appointment & No-Show Data Pipeline

## 📌 Project Overview

The **Automated Healthcare Appointment & No-Show Data Pipeline** is a Data Engineering project designed to process and analyze hospital appointment and cancellation data.

The system automatically ingests raw hospital booking records, cleans and transforms the data, removes duplicate entries, standardizes date and time formats, and calculates useful metrics such as appointment lead time.

The processed data is stored in a structured relational database containing **Patients, Doctors, and Appointments** tables. The system also categorizes appointments into **Completed, Cancelled, and No-Show** statuses, enabling hospitals to identify cancellation patterns, high-risk departments, and improve healthcare capacity management.

---

## 🎯 Problem Statement

Hospital appointment no-shows and sudden cancellations can result in unused clinical slots, inefficient resource utilization, and operational bottlenecks.

Raw appointment data is often inconsistent, duplicated, or stored in different formats, making it difficult for healthcare organizations to perform reliable analysis.

This project aims to develop an automated data engineering pipeline that cleans, transforms, and organizes hospital appointment data into a structured database. The processed data can then be used to analyze cancellation and no-show trends and support better hospital resource and capacity management.

---

## 📝 Abstract

Hospital no-shows and sudden appointment cancellations significantly drain healthcare resources, create operational bottlenecks, and leave expensive clinical slots empty. Research such as Cayirli & Veral (2006) and Dantas et al. (2018) indicates that appointment misses can follow predictable patterns associated with factors such as booking lead time.

The **Automated Healthcare Appointment & No-Show Data Pipeline** addresses this problem by developing a robust and automated Data Engineering pipeline. The system ingests raw transactional booking data, removes duplicate records, handles missing values, standardizes inconsistent temporal formats, and calculates important metrics such as the lead time between booking and appointment dates.

The cleaned data is transformed into a structured relational database containing **Patients, Doctors, and Appointments** tables. The pipeline also categorizes appointment records into **Completed, Cancelled, and No-Show** statuses, providing an analysis-ready platform for tracking monthly cancellation trends, identifying high-risk departments, and improving hospital capacity management.

---

## 👥 Team Members

| **S. No.** | **University ID** | **Name**          |
| ---------: | ----------------- | ----------------- |
|          1 | 2420030014        | V SANJAY BHAARGAV |
|          2 | 2420030368        | P RAHUL           |
|          3 | 2420030573        | M.V.S AASRITH     |

### 👨‍🏫 Supervisor

**N. SHIRISHA**

---

## 🛠️ Tools & Technologies

* **Python 3.8+**
* **Pandas**
* **PyMySQL**
* **SQLAlchemy**
* **MySQL / PostgreSQL**
* **CSV / JSON**
* **Git & GitHub**

---

## 🏗️ Project Structure

```text
Automated-Healthcare-Appointment-No-Show-Data-Pipeline/
│
├── data/                 # Raw and processed hospital appointment data
├── src/                  # Python ETL and data processing scripts
├── database/             # Database schema and SQL scripts
├── reports/              # Analytical reports and generated results
├── docs/                 # Project documentation
├── run_pipeline.py       # Main ETL pipeline execution script
└── README.md             # Project information and instructions
```

---

## ⚙️ System Workflow

```text
Raw Hospital Booking Data
          ↓
Data Ingestion
          ↓
Data Cleaning
          ↓
Duplicate Removal
          ↓
Date & Time Standardization
          ↓
Lead-Time Calculation
          ↓
Data Transformation
          ↓
Relational Database
(Patients / Doctors / Appointments)
          ↓
Appointment Status Classification
          ↓
Completed / Cancelled / No-Show
          ↓
Trend Analysis & Reports
```

---

## 🏛️ System Architecture

The project follows a **4-layer technical architecture** designed for efficient healthcare data processing:

### 1. Data Ingestion Layer

Imports raw and unstructured hospital booking records from sources such as **CSV and JSON** files.

### 2. Data Transformation Layer

Uses Python-based ETL scripts to handle missing values, remove duplicate records, standardize date formats, and calculate appointment lead-time metrics.

### 3. Storage Layer

Stores the cleaned and structured data in a relational database such as **MySQL or PostgreSQL**. The database contains organized and indexed tables for patients, doctors, and appointments.

### 4. Analytical Output Layer

Provides structured appointment status information categorized into **Completed, Cancelled, and No-Show**, allowing the data to be used for trend analysis and hospital capacity planning.

---

## 🚀 Setup & Execution

### Prerequisites

Make sure the following are installed on your system:

* Python 3.8 or above
* MySQL or PostgreSQL
* Git

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <project-directory-name>
```

### 2. Configure Environment & Database

Create a database named:

```text
hospital_analytics
```

Update the database configuration in the project with your local:

* Host
* Username
* Password
* Database name

### 3. Install Required Libraries

```bash
pip install pandas pymysql SQLAlchemy
```

### 4. Run the Pipeline

Execute the primary ETL pipeline:

```bash
python run_pipeline.py
```

The pipeline will ingest the raw data, clean and transform the records, calculate required metrics, and load the processed data into the structured database tables.

---

## 📊 Expected Outcome

The system is expected to:

* Ingest raw hospital appointment data.
* Remove duplicate appointment records.
* Handle missing and inconsistent data.
* Standardize date and time formats.
* Calculate appointment booking lead time.
* Store cleaned data in a structured relational database.
* Categorize appointments as **Completed, Cancelled, or No-Show**.
* Analyze monthly cancellation and no-show trends.
* Identify high-risk hospital departments.
* Support better hospital capacity and resource management.

---

## 📈 Current Phase Status

**Current Phase:** **Review-2 Complete**

### Phase Progress

* ✅ Project topic and domain finalized
* ✅ Abstract definition completed
* ✅ Domain introduction completed
* ✅ Literature survey mapping completed
* ✅ Cayirli & Veral (2006) literature reference reviewed
* ✅ Dantas et al. (2018) literature reference reviewed
* ✅ System architecture mapped
* ✅ Data pipeline workflow mapped
* ✅ Review-1 presentation uploaded
* ✅ Review-2 presentation uploaded
* ⬜ Database schema implementation
* ⬜ Mock data pipeline validation
* ⬜ Automated analytical report generation
* ⬜ Final testing
* ⬜ Final documentation

### Next Phase Goals — Review-3

* Deploy the complete database schema definition scripts.
* Execute mock data pipeline validation testing.
* Generate automated analytical reports for hospital department trends.

---

## 🔖 Project Phase Tags

The repository will use the following tags for project reviews:

* `review-1`
* `review-2`
* `review-3`
* `final`

---

## 🔐 Repository Guidelines

* Each team member will contribute using their own GitHub account.
* Meaningful commits should be maintained throughout the project.
* Team members should regularly push their completed work to the repository.
* No passwords, API keys, database credentials, or confidential healthcare data should be uploaded.
* Raw and processed datasets should be organized properly within the project structure.
* Database credentials should be kept outside publicly committed source code.
* Review presentations and project documentation should be maintained in the repository.
* The repository will be retained until final project evaluation.
