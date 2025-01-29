import numpy as np
from RandomGenerators import generate_operation_time, generate_time_normal


DISEASES = {
    # Cardiology
    "heart_attack": {
        "department": "Cardiology",
        "mean_diagnosis_time": 45,
        "mean_operation_time": 360,
        "hospitalization_time": 10080,
        "probability": 0.90
    },
    "arrhythmia": {
        "department": "Cardiology",
        "mean_diagnosis_time": 30,
        "mean_operation_time": 240,
        "hospitalization_time": 7200,
        "probability": 0.95
    },
    "angina": {
        "department": "Cardiology",
        "mean_diagnosis_time": 40,
        "mean_operation_time": None,
        "hospitalization_time": 4320,
        "probability": 0.99
    },
    # Neurology
    "stroke": {
        "department": "Neurology",
        "mean_diagnosis_time": 60,
        "mean_operation_time": None,
        "hospitalization_time": 14400,
        "probability": 0.75
    },
    "brain_tumor": {
        "department": "Neurology",
        "mean_diagnosis_time": 120,
        "mean_operation_time": 600,
        "hospitalization_time": 20160,
        "probability": 0.36
    },
    # Orthopedics
    "fracture": {
        "department": "Orthopedics",
        "mean_diagnosis_time": 30,
        "mean_operation_time": 120,
        "hospitalization_time": 7200,
        "probability": 0.99
    },
    "joint_replacement": {
        "department": "Orthopedics",
        "mean_diagnosis_time": 40,
        "mean_operation_time": 180,
        "hospitalization_time": 10080,
        "probability": 0.98
    }
}



DEPARTMENTS = ["Cardiology", "Neurology", "Orthopedics"]