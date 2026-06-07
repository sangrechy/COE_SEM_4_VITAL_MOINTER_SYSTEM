import sys

IS_STREAMLIT = (
    "streamlit" in str(sys.modules)
)

cases = [
    {
        "status": "Healthy State",
        "ecg": "NORMAL",
        "stress": "BASELINE",
        "hr": 72,
        "spo2": 98,
        "temp": 36.7,
        "risk": "LOW",
        "alerts": ["No Abnormalities Detected"]
    },
    {
        "status": "Stress Response Detected",
        "ecg": "NORMAL",
        "stress": "STRESS",
        "hr": 108,
        "spo2": 97,
        "temp": 36.9,
        "risk": "MEDIUM",
        "alerts": [
            "Tachycardia",
            "Elevated Cardiac Load",
            "Autonomic Stress Response"
        ]
    },
    {
        "status": "Cardiac Rhythm Abnormality",
        "ecg": "PVC",
        "stress": "BASELINE",
        "hr": 82,
        "spo2": 98,
        "temp": 36.8,
        "risk": "MEDIUM",
        "alerts": ["Arrhythmia Risk"]
    },
    {
        "status": "Recovery State",
        "ecg": "NORMAL",
        "stress": "MEDITATION",
        "hr": 65,
        "spo2": 99,
        "temp": 36.5,
        "risk": "LOW",
        "alerts": ["Recovery State"]
    },
    {
        "status": "High Cardiac Risk Event",
        "ecg": "PVC",
        "stress": "STRESS",
        "hr": 128,
        "spo2": 88,
        "temp": 38.4,
        "risk": "HIGH",
        "alerts": [
            "Arrhythmia Risk",
            "Tachycardia",
            "Low SpO2",
            "Fever Alert",
            "Elevated Cardiac Load"
        ]
    }
]

if IS_STREAMLIT:

    import streamlit as st

    st.set_page_config(
        page_title="AI Health Monitoring Demo",
        layout="wide"
    )

    st.title("AI Health Monitoring Demo")

    selected = st.selectbox(
        "Select Case",
        list(range(len(cases))),
        format_func=lambda x: cases[x]["status"]
    )

    case = cases[selected]

    st.header("PATIENT STATUS")
    st.success(case["status"])

    st.subheader("ECG FINDING")
    st.write(case["ecg"])

    st.subheader("STRESS STATE")
    st.write(case["stress"])

    st.subheader("VITALS")
    st.write(f"Heart Rate : {case['hr']} BPM")
    st.write(f"SpO₂ : {case['spo2']} %")
    st.write(f"Temperature : {case['temp']} °C")

    st.subheader("ALERTS")

    for alert in case["alerts"]:
        st.warning(alert)

    st.subheader("RISK LEVEL")
    st.write(case["risk"])

else:

    for case in cases:

        print("\n" + "=" * 60)

        print("PATIENT STATUS")
        print("--------------")
        print(case["status"])

        print("\nECG FINDING")
        print("-----------")
        print(case["ecg"])

        print("\nSTRESS STATE")
        print("------------")
        print(case["stress"])

        print("\nVITALS")
        print("------")
        print(f"Heart Rate : {case['hr']} BPM")
        print(f"SpO2       : {case['spo2']} %")
        print(f"Temperature: {case['temp']} °C")

        print("\nALERTS")
        print("------")

        for alert in case["alerts"]:
            print(f"✓ {alert}")

        print("\nRISK LEVEL")
        print("----------")
        print(case["risk"])

    print("\n" + "=" * 60)
