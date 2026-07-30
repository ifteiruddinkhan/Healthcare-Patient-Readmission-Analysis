import sqlite3
import pandas as pd

df = pd.read_csv("cleaned_healthcare_ehr.csv")
conn = sqlite3.connect("healthcare_analytics.db")
df.to_sql("patient_encounters", conn, if_exists="replace", index=False)

print("--- SQL QUERY 1: 30-Day Readmission Rate & ALOS by Diagnosis Group ---")
q1 = """
SELECT 
    primary_diagnosis_group,
    COUNT(encounter_id) AS total_encounters,
    ROUND(AVG(length_of_stay_days), 2) AS avg_length_of_stay_days,
    SUM(readmitted_30d) AS readmission_30d_count,
    ROUND((CAST(SUM(readmitted_30d) AS FLOAT) / COUNT(encounter_id)) * 100, 2) AS readmission_30d_rate_pct
FROM patient_encounters
GROUP BY primary_diagnosis_group
HAVING COUNT(encounter_id) > 500
ORDER BY readmission_30d_rate_pct DESC;
"""
print(pd.read_sql_query(q1, conn))

print("\n--- SQL QUERY 2: High-Risk Patient Identification (Multiple Inpatient Visits) ---")
q2 = """
WITH Patient_History AS (
    SELECT 
        patient_nbr,
        age,
        primary_diagnosis_group,
        number_inpatient,
        number_emergency,
        readmitted_30d,
        DENSE_RANK() OVER (ORDER BY number_inpatient DESC) as risk_rank
    FROM patient_encounters
)
SELECT 
    age,
    primary_diagnosis_group,
    COUNT(patient_nbr) AS total_patients,
    SUM(number_inpatient) AS total_past_inpatient_visits,
    ROUND(AVG(readmitted_30d) * 100, 2) AS readmission_rate_pct
FROM Patient_History
WHERE number_inpatient > 1
GROUP BY age, primary_diagnosis_group
ORDER BY readmission_rate_pct DESC
LIMIT 5;
"""
print(pd.read_sql_query(q2, conn))

conn.close()