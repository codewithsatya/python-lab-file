# A fitness coach wants to analyze the BMI 
# of a group of people to assess their health 
# status. The data includes the name, age, 
# weight (kg), and height (m) of each 
# person. The coach wants: 
# To calculate BMI for each person. 
# To categorize each person based on their 
# BMI. 
# To get a summary of how many people fall 
# into each category. 
def calculate_bmi(weight, height):
    return weight / (height ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 24.9 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"


# Sample group data
people = [
    {"name": "Amit", "age": 25, "weight": 60, "height": 1.70},
    {"name": "Rahul", "age": 30, "weight": 75, "height": 1.65},
    {"name": "Priya", "age": 22, "weight": 50, "height": 1.60},
    {"name": "Sita", "age": 28, "weight": 90, "height": 1.72},
]


summary = {"Underweight": 0, "Normal": 0, "Overweight": 0, "Obese": 0}

print("\nBMI Report\n")

for person in people:
    bmi = calculate_bmi(person["weight"], person["height"])
    category = bmi_category(bmi)

    summary[category] += 1

    print(f"Name: {person['name']}, Age: {person['age']}")


#  numerologist wants a tool to help 
# analyze the numerology number of 
# people's names. Each alphabet is assigned 
# a number, and the sum of these numbers, 
# reduced to a single digit (unless it's a 
# master number like 11 or 22), is 
# considered their Name Number. 
# The numerologist wants: 
# To input names. 
# To calculate their numerology number. 
# To match the number to a basic 
# personality meaning. 
# To process multiple names and generate a 
# report.
def letter_value(ch):
    ch = ch.upper()
    if 'A' <= ch <= 'Z':
        return (ord(ch) - ord('A')) % 9 + 1
    return 0  # for spaces or other characters


def reduce_number(num):
    # Preserve master numbers 11 and 22
    if num in (11, 22):
        return num

    # Reduce until single digit
    while num > 9:
        num = sum(int(d) for d in str(num))
    return num


def get_numerology_number(name):
    total = sum(letter_value(ch) for ch in name)
    
    # Check for master numbers before reducing
    if total == 11 or total == 22:
        return total
    else:
        return reduce_number(total)


# Basic personality meanings for each number:
meanings = {
    1: "Leader, independent, strong personality.",
    2: "Diplomatic, peaceful, cooperative.",
    3: "Creative, expressive, joyful.",
    4: "Practical, disciplined, hardworking.",
    5: "Adventurous, freedom-loving, energetic.",
    6: "Caring, responsible, nurturing.",
    7: "Spiritual, analytical, deep thinker.",
    8: "Ambitious, powerful, success-oriented.",
    9: "Compassionate, humanitarian, emotional.",
    11: "Visionary, intuitive, spiritually gifted (Master Number).",
    22: "Master builder, powerful achiever (Master Number)."
}

def numerology_report():
    print("=== Numerology Name Analyzer ===")
    
    names = []
    n = int(input("How many names do you want to analyze? "))

    for i in range(n):
        name = input(f"Enter name {i+1}: ")
        names.append(name)

    print("\n=== Numerology Report ===\n")

    for name in names:
        num = get_numerology_number(name)
        meaning = meanings.get(num, "No meaning found.")

        print(f"Name: {name}")
        print(f"Numerology Number: {num}")
        print(f"Personality Meaning: {meaning}\n")


numerology_report()

# Develop a system that tracks air pollution levels (such as PM2.5, PM10, CO2) in different regions of a city. The system should: Collect pollution data from sensors deployed in various regions. Store and organize pollution data efficiently. Perform analysis to identify areas with the highest pollution levels over time.
def collect_data(region, pm25, pm10, co2):
    reading = {"PM2.5": pm25, "PM10": pm10, "CO2": co2}

    # Add region if not present
    if region not in pollution_data:
        pollution_data[region] = []

    pollution_data[region].append(reading)


# Step 3: Analyze pollution levels
def analyze_pollution():
    region_scores = {}

    for region, records in pollution_data.items():
        total_pm25 = sum(r["PM2.5"] for r in records)
        total_pm10 = sum(r["PM10"] for r in records)
        total_co2  = sum(r["CO2"] for r in records)

        # Pollution score = weighted sum (simple model)
        score = total_pm25 + total_pm10 + (total_co2 / 10)
        region_scores[region] = score

    # Find region with maximum pollution
    highest_region = max(region_scores, key=region_scores.get)

    print("\n--- Pollution Analysis Report ---")
    for region, score in region_scores.items():
        print(f"{region}: Score = {score:.2f}")

    print(f"\nRegion with highest pollution over time: **{highest_region}**")


# Step 4: Sample Data Collection (simulate sensor readings)
collect_data("Central", 55, 100, 450)
collect_data("Central", 60, 110, 470)
collect_data("North", 30, 50, 380)
collect_data("North", 35, 45, 390)
collect_data("Industrial", 90, 150, 600)
collect_data("Industrial", 95, 155, 620)

# Step 5: Generate Report
analyze_pollution()


# calculate the income tax for a person with 
# investments in mutual funds, NPS, Shares, 
# House Loan Interest, Fixed Deposits,  
# ULIP, Insurance, National Saving 
# Certificate and PPF, as per the latest 
# guidelines. 
def compute_taxable_income(
    salary_income=0,
    interest_income=0,
    other_income=0,
    home_loan_interest=0,
    investments_80c=0,
    nps_self_contribution=0,
    choose_new_regime=False
):
    """
    Compute taxable income based on inputs.
    - investments_80c: sum of PPF, NSC, tax-saving FD, ELSS/ULIPs (premiums), home-loan principal (but interest separate)
    - nps_self_contribution: amount put in NPS by self (eligible for 80CCD(1B))
    - home_loan_interest: interest paid (if house property is let-out and eligible — only under old regime; for self-occupied property deduction rules differ)
    - choose_new_regime: boolean, if True uses new regime (fewer deductions), else old regime.
    """
    gross_income = salary_income + interest_income + other_income
    deduction = 0

    if not choose_new_regime:
        # Old regime: allow 80C + 80CCD(1B) + home loan interest (subject to limits/rules)
        max_80c = 150000
        deduction += min(investments_80c, max_80c)
        deduction += nps_self_contribution  # up to 50,000 — you may validate before calling
        # Home loan interest deduction: if applicable, else 0
        deduction += home_loan_interest

    # Else new regime → no deductions (except maybe standard deduction etc.)

    taxable_income = gross_income - deduction
    taxable_income = max(taxable_income, 0)
    return taxable_income


def compute_tax_liability(taxable_income):
    """
    Simplified slab-based tax for FY 2025-26 under old and new regimes.
    Use whichever slab you prefer; here we'll show both.
    """
    # Old regime slabs (for example; may vary)
    def old_tax(income):
        tax = 0
        slabs = [(250000, 0), (500000, 0.05), (1000000, 0.20), (float('inf'), 0.30)]
        prev = 0
        for limit, rate in slabs:
            if income > prev:
                taxable = min(income, limit) - prev
                tax += taxable * rate
                prev = limit
            else:
                break
        return tax

    # New regime slabs FY 2025 (example)
    def new_tax(income):
        tax = 0
        slabs = [(400000, 0), (800000, 0.05), (1200000, 0.10), (1600000, 0.15),
                 (2000000, 0.20), (2400000, 0.25), (float('inf'), 0.30)]
        prev = 0
        for limit, rate in slabs:
            if income > prev:
                taxable = min(income, limit) - prev
                tax += taxable * rate
                prev = limit
            else:
                break
        return tax

    tax_old = old_tax(taxable_income)
    tax_new = new_tax(taxable_income)
    return tax_old, tax_new


if __name__ == "__main__":
    # Example usage
    salary = 1200000   # ₹ 12 lakh
    interest = 50000   # interest from FD, savings, etc.
    other = 20000      # any other income
    home_int = 150000  # home loan interest paid
    inv_80c = 140000   # PPF + ELSS + NSC etc.
    nps = 40000        # NPS self contribution

    # Choose whether you want old or new regime
    taxable_old = compute_taxable_income(
        salary, interest, other,
        home_loan_interest=home_int,
        investments_80c=inv_80c,
        nps_self_contribution=nps,
        choose_new_regime=False
    )
    tax_old, tax_new_dummy = compute_tax_liability(taxable_old)
    print("Old regime → Taxable income:", taxable_old, "Tax:", tax_old)

    # Or if you pick new regime:
    taxable_new = compute_taxable_income(
        salary, interest, other,
        choose_new_regime=True
    )
    tax_dummy, tax_new = compute_tax_liability(taxable_new)
    print("New regime → Taxable income:", taxable_new, "Tax:", tax_new)


# Detects anomalies in banking transactions 
# using clustering and pattern recognition 
# algorithms. 
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt


np.random.seed(42)

# Normal transactions
num_normal = 200
amount_normal = np.random.normal(100, 20, num_normal)
time_normal =  np.random.uniform(0, 24, num_normal)
location_normal = np.random.randint(1, 20, num_normal)

# Anomalous transactions
num_anomaly = 10
amount_anomaly = np.random.normal(1000, 100, num_anomaly)
time_anomaly = np.random.uniform(0, 24, num_anomaly)
location_anomaly = np.random.randint(1, 20, num_anomaly)


amounts = np.concatenate([amount_normal, amount_anomaly])
times = np.concatenate([time_normal, time_anomaly])
locations = np.concatenate([location_normal, location_anomaly])

transactions = pd.DataFrame({
    "amount": amounts,
    "time_of_day": times,
    "location_id": locations
})


scaler = StandardScaler()
X_scaled = scaler.fit_transform(transactions)


iso_forest = IsolationForest(contamination=0.05, random_state=42)
transactions['anomaly_iso'] = iso_forest.fit_predict(X_scaled)

dbscan = DBSCAN(eps=1.5, min_samples=5)
transactions['cluster'] = dbscan.fit_predict(X_scaled)

print("Anomalies detected by Isolation Forest:")
print(transactions[transactions['anomaly_iso'] == -1])

print("\nAnomalies detected by DBSCAN (cluster = -1):")
print(transactions[transactions['cluster'] == -1])

plt.figure(figsize=(10,6))
plt.scatter(transactions['time_of_day'], transactions['amount'],
            c=transactions['anomaly_iso'].map({1: 'blue', -1: 'red'}),
            alpha=0.6)
plt.xlabel("Time of Day (hours)")
plt.ylabel("Transaction Amount")
plt.title("Banking Transactions - Anomaly Detection (Red = Anomaly)")
plt.show()

# A health monitoring system that tracks 
# vitals (BP, sugar, heart rate), medication 
# schedule, and alerts caregivers. 
import datetime


patients = {
    "Patient1": {
        "BP": {"systolic": 120, "diastolic": 80},
        "sugar": 90,
        "heart_rate": 72,
        "medications": {
            "Morning": {"name": "MedA", "taken": False},
            "Evening": {"name": "MedB", "taken": False}
        },
        "caregiver": "caregiver1@example.com"
    },
    "Patient2": {
        "BP": {"systolic": 140, "diastolic": 90},
        "sugar": 150,
        "heart_rate": 85,
        "medications": {
            "Morning": {"name": "MedC", "taken": False},
            "Evening": {"name": "MedD", "taken": False}
        },
        "caregiver": "caregiver2@example.com"
    }
}


vital_limits = {
    "BP": {"systolic": (90, 140), "diastolic": (60, 90)},
    "sugar": (70, 140),  # mg/dL
    "heart_rate": (60, 100)  # bpm
}


def check_vitals(patient_name, patient_data):
    alerts = []

    # Check BP
    sys_min, sys_max = vital_limits["BP"]["systolic"]
    dia_min, dia_max = vital_limits["BP"]["diastolic"]
    sys = patient_data["BP"]["systolic"]
    dia = patient_data["BP"]["diastolic"]
    if not (sys_min <= sys <= sys_max) or not (dia_min <= dia <= dia_max):
        alerts.append(f"Abnormal BP: {sys}/{dia} mmHg")

    # Check sugar
    sugar_min, sugar_max = vital_limits["sugar"]
    sugar = patient_data["sugar"]
    if not (sugar_min <= sugar <= sugar_max):
        alerts.append(f"Abnormal blood sugar: {sugar} mg/dL")

    # Check heart rate
    hr_min, hr_max = vital_limits["heart_rate"]
    hr = patient_data["heart_rate"]

# Monitors water quality (pH, turbidity, 
# temperature, TDS) in real time and flags 
# contamination events. 
import random
import time

safe_limits = {
    "pH": (6.5, 8.5),         
    "turbidity": (0, 5),      
    "temperature": (0, 35),   
    "TDS": (0, 500)           
}


def get_water_readings():
    return {
        "pH": round(random.uniform(5.5, 9.0), 2),
        "turbidity": round(random.uniform(0, 10), 2),
        "temperature": round(random.uniform(0, 40), 1),
        "TDS": round(random.uniform(100, 700), 1)
    }
def check_contamination(readings):
    alerts = []
    for param, value in readings.items():
        min_val, max_val = safe_limits[param]
        if not (min_val <= value <= max_val):
            alerts.append(f"{param} = {value} (OUT OF RANGE)")
    return alerts


def monitor_water(interval_sec=5, iterations=10):
    print("Starting Real-Time Water Quality Monitoring...\n")
    for i in range(iterations):
        readings = get_water_readings()
        print(f"Reading {i+1}: {readings}")
        
        alerts = check_contamination(readings)
        if alerts:
            print("ALERT: Contamination Detected!")
            for alert in alerts:
                print(" -", alert)
        else:
            print("All parameters within safe limits.")
        
        print("-" * 50)
        time.sleep(interval_sec)  

monitor_water()
