import numpy as np
from RandomGenerators import generate_operation_time

def generate_operation_time(mean_time):
    """
    Generuje realistyczny czas operacji na podstawie rozkładu trójkątnego.

    Args:
        mean_time (float): Średni czas operacji (w godzinach).

    Returns:
        float: Wygenerowany czas operacji w godzinach.
    """
    if mean_time is None:
        return None
    min_time = mean_time * 0.75  # Minimalny czas: 75% średniego czasu
    max_time = mean_time * 1.25  # Maksymalny czas: 125% średniego czasu
    return np.random.triangular(min_time, mean_time, max_time)


DISEASES = {
    # Cardiology
    "heart_attack": {
        "department": "Cardiology",
        "mean_diagnosis_time": 45,
        "mean_operation_time": 6,
        "operation_time": generate_operation_time(6),  # Generowanie czasu operacji
        "hospitalization_time": 7,
        "probability": 0.25
    },
    "arrhythmia": {
        "department": "Cardiology",
        "mean_diagnosis_time": 30,
        "mean_operation_time": 4,
        "operation_time": generate_operation_time(4),
        "hospitalization_time": 5,
        "probability": 0.15
    },
    "angina": {
        "department": "Cardiology",
        "mean_diagnosis_time": 40,
        "mean_operation_time": None,
        "operation_time": None,  # Brak operacji
        "hospitalization_time": 3,
        "probability": 0.2
    },
    # Neurology
    "stroke": {
        "department": "Neurology",
        "mean_diagnosis_time": 60,
        "mean_operation_time": None,
        "operation_time": None,  # Brak operacji
        "hospitalization_time": 10,
        "probability": 0.3
    },
    "brain_tumor": {
        "department": "Neurology",
        "mean_diagnosis_time": 120,
        "mean_operation_time": 10,
        "operation_time": generate_operation_time(10),
        "hospitalization_time": 14,
        "probability": 0.1
    },
    # Orthopedics
    "fracture": {
        "department": "Orthopedics",
        "mean_diagnosis_time": 30,
        "mean_operation_time": 2,
        "operation_time": generate_operation_time(2),
        "hospitalization_time": 5,
        "probability": 0.25
    },
    "joint_replacement": {
        "department": "Orthopedics",
        "mean_diagnosis_time": 40,
        "mean_operation_time": 3,
        "operation_time": generate_operation_time(3),
        "hospitalization_time": 7,
        "probability": 0.2
    }
}


DEPARTMENTS = ["Cardiology", "Neurology", "Orthopedics"]

