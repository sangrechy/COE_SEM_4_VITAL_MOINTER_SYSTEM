cases = [

{
    "CASE": "Healthy Individual",
    "HR": 72,
    "SpO2": 98,
    "Temp": 36.7,
    "Motion": 0.2,
    "ECG": "NORMAL",
    "Stress": "BASELINE",
    "Risk": "LOW"
},

{
    "CASE": "Stress Response",
    "HR": 108,
    "SpO2": 97,
    "Temp": 36.9,
    "Motion": 0.4,
    "ECG": "NORMAL",
    "Stress": "STRESS",
    "Risk": "MEDIUM"
},

{
    "CASE": "PVC Detection",
    "HR": 82,
    "SpO2": 98,
    "Temp": 36.8,
    "Motion": 0.3,
    "ECG": "PVC",
    "Stress": "BASELINE",
    "Risk": "MEDIUM"
},

{
    "CASE": "Recovery State",
    "HR": 65,
    "SpO2": 99,
    "Temp": 36.5,
    "Motion": 0.1,
    "ECG": "NORMAL",
    "Stress": "MEDITATION",
    "Risk": "LOW"
},

{
    "CASE": "High Cardiac Risk Event",
    "HR": 128,
    "SpO2": 88,
    "Temp": 38.4,
    "Motion": 1.8,
    "ECG": "PVC",
    "Stress": "STRESS",
    "Risk": "HIGH"
}

]

for c in cases:

    print("\n" + "="*50)

    print("CASE:", c["CASE"])

    print("\nINPUTS")
    print("Heart Rate :", c["HR"], "BPM")
    print("SpO2       :", c["SpO2"], "%")
    print("Temperature:", c["Temp"], "°C")
    print("Motion     :", c["Motion"])
    print("ECG Class  :", c["ECG"])

    print("\nOUTPUTS")
    print("ECG Finding :", c["ECG"])
    print("Stress State:", c["Stress"])
    print("Risk Level  :", c["Risk"])

print("\n" + "="*50)

