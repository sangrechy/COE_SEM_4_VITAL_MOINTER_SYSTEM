def fusion_engine(
    ecg_class,
    stress_class,
    heart_rate,
    spo2,
    temperature,
    motion
):

    alerts = []

    ecg_map = {
        0: "NORMAL",
        1: "PVC",
        2: "PAC",
        3: "LBBB",
        4: "RBBB",
        5: "OTHER_ABNORMAL"
    }

    alerts.append(ecg_map[ecg_class])

    stress_map = {
        0: "BASELINE",
        1: "STRESS",
        2: "AMUSEMENT",
        3: "MEDITATION"
    }

    alerts.append(stress_map[stress_class])

    if heart_rate > 100:
        alerts.append("TACHYCARDIA")
    elif heart_rate < 60:
        alerts.append("BRADYCARDIA")

    if spo2 < 90:
        alerts.append("LOW_SPO2")

    if temperature > 37.5:
        alerts.append("FEVER_ALERT")

    if motion > 1.5:
        alerts.append("PHYSICAL_ACTIVITY")

    if stress_class == 3 and heart_rate < 80:
        alerts.append("RECOVERY_STATE")

    if ecg_class != 0:
        alerts.append("ARRHYTHMIA_RISK")

    if heart_rate > 100 and stress_class == 1:
        alerts.append("ELEVATED_CARDIAC_LOAD")

    if stress_class == 1:
        alerts.append("AUTONOMIC_STRESS_RESPONSE")

    if stress_class == 1 and motion < 0.5:
        alerts.append("FATIGUE_RISK")

    if (
        stress_class == 1
        and heart_rate > 120
        and motion > 1.5
    ):
        alerts.append("OVEREXERTION_RISK")

    if spo2 < 88:
        alerts.append("HYPOXIA_RISK")

    if temperature > 38.5:
        alerts.append("HYPERTHERMIA_RISK")

    if (
        ecg_class != 0
        or spo2 < 90
        or temperature > 37.5
    ):
        alerts.append("HEALTH_MONITORING_ALERT")

    return alerts


if __name__ == "__main__":

    result = fusion_engine(
        ecg_class=1,
        stress_class=1,
        heart_rate=125,
        spo2=87,
        temperature=38.8,
        motion=2.0
    )

    print(result)
