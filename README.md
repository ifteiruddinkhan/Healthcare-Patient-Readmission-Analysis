# 🏥 Healthcare Operational & Patient Readmission Risk Analytics

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-SQLite_3-003B57?logo=sqlite&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-Dashboard-F2C811?logo=powerbi&logoColor=black)
![Domain](https://img.shields.io/badge/Domain-Healthcare_%26_HealthTech-red)

An end-to-end data engineering and business intelligence project focused on analyzing **30-Day Hospital Readmissions**, **Average Length of Stay (ALOS)**, and clinical diagnosis risk factors using Electronic Health Record (EHR) clinical data.

---

## 🎯 Problem Statement & Strategic Outcome

### 🔴 The Business & Clinical Problem
Under regulatory frameworks such as the **Hospital Readmissions Reduction Program (HRRP)**, healthcare systems face severe financial penalties and lost revenue when patients are unexpectedly readmitted within 30 days of discharge. 

Hospitals struggle to proactively identify which patients are at high risk because Electronic Health Record (EHR) data is notoriously messy, unstructured, and fragmented across diagnosis codes (ICD-9), historical stay lengths, and past emergency visits. Without automated risk stratification, clinical teams cannot allocate post-discharge follow-up resources effectively.

### 🟢 The Solution & Strategic Outcome
This project delivers an automated, end-to-end data analytics pipeline (Python + SQL + Power BI) that transforms raw EHR data into actionable clinical intelligence.

* **Financial & Regulatory Outcome:** Enables health systems to target high-risk patient cohorts, potentially reducing 30-day readmissions by **10–15%** through automated post-discharge outreach—directly mitigating HRRP financial penalties.
* **Operational Efficiency:** Pinpoints discharge bottlenecks (such as patients with an Average Length of Stay $>7$ days) and arms clinical managers with an interactive Power BI drill-down tool to optimize bed capacity and post-care scheduling.
* **Data Infrastructure Value:** Establishes a standardized data pipeline that automatically cleans messy ICD-9 diagnosis codes and ranks patient risk levels using advanced SQL window functions.

---
## 💡 Executive Summary & Strategic Insights

* **30-Day Readmission Rate:** **~11.2%** of total analyzed patient encounters resulted in a readmission within 30 days.
* **Primary Clinical Drivers:** **Circulatory Diseases** (Heart Failure, Hypertension) and **Diabetes** accounted for the largest volume of 30-day readmissions.
* **Operational Bottlenecks:** Patients with an **Average Length of Stay (ALOS) > 7 days** exhibit a **40% higher probability** of readmission compared to short-stay patients.
* **High-Risk Cohort:** Patients with $\ge 2$ inpatient visits in the preceding year represent the highest-risk group, making them prime candidates for automated post-discharge outreach programs.

---

## 🏗 Data Pipeline Architecture

```text
+-----------------------+      +-------------------------+      +--------------------+      +--------------------+
| Raw EHR Data          | ---> | Python Wrangling        | ---> | SQLite Database    | ---> | Power BI Dashboard |
| (diabetes.csv)        |      | ICD-9 Code Mapping      |      | Window Functions   |      | Interactive KPIs   |
+-----------------------+      +-------------------------+      +--------------------+      +--------------------+
