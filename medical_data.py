
DISEASES = {
    # Cardiology
    "heart_attack": {
        "department": "Cardiology",
        "mean_diagnosis_time": 15,  # Średni czas diagnozy dla zawału serca (w minutach)
        "operation_time": 5,
        "hospitalization_time": 7,
        "probability": 0.3
    },
    "arrhythmia": {
        "department": "Cardiology",
        "mean_diagnosis_time": 20,  # Średni czas diagnozy dla arytmii (w minutach)
        "operation_time": 4,
        "hospitalization_time": 5,
        "probability": 0.2
    },

    # Neurology
    "stroke": {
        "department": "Neurology",
        "mean_diagnosis_time": 30,  # Średni czas diagnozy dla udaru (w minutach)
        "operation_time": None,
        "hospitalization_time": 10,
        "probability": 0.25
    },
    "epilepsy": {
        "department": "Neurology",
        "mean_diagnosis_time": 15,  # Średni czas diagnozy dla padaczki (w minutach)
        "operation_time": None,
        "hospitalization_time": 5,
        "probability": 0.15
    },

    # Orthopedics
    "fracture": {
        "department": "Orthopedics",
        "mean_diagnosis_time": 10,  # Średni czas diagnozy dla złamań (w minutach)
        "operation_time": 3,
        "hospitalization_time": 7,
        "probability": 0.2
    },
    "spinal_injury": {
        "department": "Orthopedics",
        "mean_diagnosis_time": 25,  # Średni czas diagnozy dla urazów kręgosłupa (w minutach)
        "operation_time": 8,
        "hospitalization_time": 14,
        "probability": 0.1
    }
}


DEPARTMENTS = ["Cardiology", "Neurology", "Orthopedics"]