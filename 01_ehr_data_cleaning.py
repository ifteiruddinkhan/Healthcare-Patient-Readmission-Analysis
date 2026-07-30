import pandas as pd
import numpy as np

# 1. Load Dataset
df = pd.read_csv(r"C:\Users\SkyTech\Downloads\diabetes.csv\diabetes.csv")

# 2. Clean missing indicators ('?')
df.replace('?', np.nan, inplace=True)

# 3. Standardize Binary Target: 30-Day Readmission Flag
# Original values: '<30', '>30', 'NO'
df['readmitted_30d'] = np.where(df['readmitted'] == '<30', 1, 0)
df['is_readmitted_any'] = np.where(df['readmitted'] != 'NO', 1, 0)

# 4. Map ICD-9 Codes to Primary Clinical Diagnosis Groups
def map_icd9(code):
    if pd.isna(code):
        return 'Other / Unknown'
    # Check if code is numeric
    try:
        val = float(code)
        if (val >= 390 and val <= 459) or val == 785:
            return 'Circulatory (Heart Failure/Hypertension)'
        elif (val >= 460 and val <= 519) or val == 786:
            return 'Respiratory'
        elif (val >= 520 and val <= 579) or val == 787:
            return 'Digestive'
        elif np.floor(val) == 250:
            return 'Diabetes'
        elif val >= 800 and val <= 999:
            return 'Injury / Trauma'
        elif val >= 710 and val <= 739:
            return 'Musculoskeletal'
        elif (val >= 580 and val <= 629) or val == 788:
            return 'Genitourinary'
        elif val >= 140 and val <= 239:
            return 'Neoplasms (Cancer)'
        else:
            return 'Other Clinical Category'
    except ValueError:
        return 'Other / External'

df['primary_diagnosis_group'] = df['diag_1'].apply(map_icd9)

# 5. Extract Average Length of Stay (ALOS) metric
df['length_of_stay_days'] = df['time_in_hospital'].astype(int)

# 6. Export cleaned dataset for SQL and Power BI
df.to_csv("cleaned_healthcare_ehr.csv", index=False)
print("EHR Data Wrangling Complete. Exported to 'cleaned_healthcare_ehr.csv'.")