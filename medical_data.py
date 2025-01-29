import numpy as np
from RandomGenerators import generate_operation_time, generate_time_normal


DISEASES = {
    # Cardiology
    "heart_attack": {
        "department": "Cardiology",
        "mean_diagnosis_time": 45,
        "mean_operation_time": generate_time_normal(6),
        "operation_time": generate_operation_time(6),  # Generowanie czasu operacji
        "hospitalization_time": generate_time_normal(7),
        "probability": 0.4
    },
    "arrhythmia": {
        "department": "Cardiology",
        "mean_diagnosis_time": 30,
        "mean_operation_time": generate_time_normal(4),
        "operation_time": generate_operation_time(4),
        "hospitalization_time": generate_time_normal(5),
        "probability": 0.7
    },
    "angina": {
        "department": "Cardiology",
        "mean_diagnosis_time": 40,
        "mean_operation_time": None,
        "operation_time": None,  # Brak operacji
        "hospitalization_time": generate_time_normal(3),
        "probability": 0.9
    },
    # Neurology
    "stroke": {
        "department": "Neurology",
        "mean_diagnosis_time": 60,
        "mean_operation_time": None,
        "operation_time": None,  # Brak operacji
        "hospitalization_time": generate_time_normal(10),
        "probability": 0.5
    },
    "brain_tumor": {
        "department": "Neurology",
        "mean_diagnosis_time": 120,
        "mean_operation_time": generate_time_normal(10),
        "operation_time": generate_operation_time(10),
        "hospitalization_time": generate_time_normal(14),
        "probability": 0.3
    },
    # Orthopedics
    "fracture": {
        "department": "Orthopedics",
        "mean_diagnosis_time": 30,
        "mean_operation_time": generate_time_normal(2),
        "operation_time": generate_operation_time(2),
        "hospitalization_time": generate_time_normal(5),
        "probability": 0.9
    },
    "joint_replacement": {
        "department": "Orthopedics",
        "mean_diagnosis_time": 40,
        "mean_operation_time": generate_time_normal(3),
        "operation_time": generate_operation_time(3),
        "hospitalization_time": generate_time_normal(7),
        "probability": 0.9
    }
}


DEPARTMENTS = ["Cardiology", "Neurology", "Orthopedics"]