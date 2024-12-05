SYMPTOMS = [
    ("headache", 0.25),
    ("fever", 0.20),
    ("cough", 0.15),
    ("fatigue", 0.10),
    ("nausea", 0.08),
    ("dizziness", 0.06),
    ("chest pain", 0.05),
    ("rash", 0.04),
    ("shortness of breath", 0.03),
    ("vision loss", 0.02),
    ("numbness", 0.01)
]

DISEASES = {
    "common cold": ["cough", "fever", "fatigue"],
    "flu": ["fever", "fatigue", "cough", "headache", "sore throat"],
    "pneumonia": ["fever", "cough", "shortness of breath", "chest pain"],
    "migraine": ["headache", "nausea", "dizziness"],
    "stroke": ["headache", "numbness", "vision loss", "dizziness"],
    "heart attack": ["chest pain", "shortness of breath", "fatigue"]
}