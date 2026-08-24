Automated Healthcare Appointment & No-Show Data Pipeline
👥 Project Team & Governance
Project Title: Automated Healthcare Appointment & No-Show Data Pipeline
Team Members:
V SANJAY BHAARGAV ID:2420030014
P RAHUL           ID:2420030368
M.V.S AASRITH     ID:2420030573
Supervisor: N.SHIRISHA
---
📝 Abstract
Hospital no-shows and sudden appointment cancellations significantly drain healthcare resources, create operational bottlenecks, and leave expensive clinical slots empty. While academic literature (such as Cayirli & Veral, 2006 and Dantas et al., 2018) confirms that these misses follow predictable patterns linked to factors like booking lead times, healthcare facilities lack the clean, automated infrastructure needed to process this data.
This project bridges that gap by engineering a robust, automated Data Engineering pipeline. The system ingests raw, messy transactional booking logs, automatically purges duplicate records, standardizes inconsistent temporal formats, and computes calculated metrics (such as the exact lead time between booking and appointment dates). By transforming chaotic raw files into a structured relational database schema (`Patients`, `Doctors`, `Appointments`), the pipeline provides an analysis-ready platform to track monthly cancellation trends, isolate high-risk departments, and optimize hospital capacity management.
---
🏗️ System Architecture & Data Flow
The project is built on a 4-layer technical architecture designed for efficient data processing:
Data Ingestion Layer: Imports raw, unstructured hospital booking entries (CSV/JSON formats).
Data Transformation Layer: A Python ETL engine running scripts to handle null values, fix date strings, and calculate booking lead-time metrics.
Storage Layer: A clean, optimized relational database (MySQL/PostgreSQL) housing structured and indexed tables.
Analytical Output Layer: Structured data views categorizing appointments into `Completed`, `Cancelled`, and `No-Show` statuses for immediate trend analysis.
---
⚙️ Setup and Execution Instructions
Prerequisites
Ensure you have the following installed on your local machine:
Python 3.8+
A relational database engine (MySQL / PostgreSQL)
Git
1. Clone the Repository
```bash
git clone <your-git-link-here>
cd <project-directory-name>
```
2. Configure Environment & Database
Create a fresh database instance named `hospital_analytics`.
Open the database configuration file (or script setup) and update your local database credentials (host, user, password).
3. Install Dependencies
Install the required data processing packages via pip:
```bash
pip install pandas pymysql SQLAlchemy
```
4. Run the Pipeline Execution Script
Execute the primary ETL script to ingest, clean, transform, and load the raw data into your structured database tables:
```bash
python run_pipeline.py
```
---
📊 Current Phase Status (Review-2)
Phase: Review-2 Complete
Completed Milestones:
Abstract definition and domain introduction finalized.
Literature Survey mapping complete (Cayirli & Veral, 2006; Dantas et al., 2018).
System Architecture and Data Pipeline Workflow mapped out.
Artifacts Uploaded:
Review-1 Presentation Source Slide PDF/PPTX uploaded to repository root.
Review-2 Presentation Source Slide PDF/PPTX uploaded to repository root.
Next Phase Goals (Review-3):
Deploy full database schema definition scripts.
Execute mock data pipeline validation testing.
Generate automated analytic reports for hospital department trends.
