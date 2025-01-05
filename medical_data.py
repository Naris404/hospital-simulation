
DISEASES = {
    # Cardiology
    "heart_attack": {
        "department": "Cardiology",
        "diagnosis_time": 2,
        "operation_time": 5,
        "hospitalization_time": 7,
        "probability": 0.3  # 30% szans wśród pacjentów kardiologicznych
    },
    "arrhythmia": {
        "department": "Cardiology",
        "diagnosis_time": 3,
        "operation_time": 4,
        "hospitalization_time": 5,
        "probability": 0.2  # 20%
    },

    # Neurology
    "stroke": {
        "department": "Neurology",
        "diagnosis_time": 4,
        "operation_time": None,
        "hospitalization_time": 10,
        "probability": 0.25  # 25% szans wśród pacjentów neurologicznych
    },
    "epilepsy": {
        "department": "Neurology",
        "diagnosis_time": 2,
        "operation_time": None,
        "hospitalization_time": 5,
        "probability": 0.15  # 15%
    },

    # Orthopedics
    "fracture": {
        "department": "Orthopedics",
        "diagnosis_time": 1,
        "operation_time": 3,
        "hospitalization_time": 7,
        "probability": 0.2  # 20% szans wśród pacjentów ortopedycznych
    },
    "spinal_injury": {
        "department": "Orthopedics",
        "diagnosis_time": 5,
        "operation_time": 8,
        "hospitalization_time": 14,
        "probability": 0.1  # 10%
    }
}
