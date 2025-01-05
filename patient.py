import random
from medical_data import DISEASES


class Patient:
    def __init__(self, age, gender, disease=None, diagnosis_result=None, hospital_days=0, survival_prob=1.0):
        self.age = age
        self.gender = gender
        self.disease = disease  # Słownik szczegółów choroby
        self.hospital_days = hospital_days
        self.survival_prob = survival_prob
        self.diagnosis_result = diagnosis_result

    def assign_random_disease(self):
        diseases = list(DISEASES.keys())
        probabilities = [DISEASES[d]["probability"] for d in diseases]

        selected_disease = random.choices(diseases, probabilities, k=1)[0]
        self.update_disease(selected_disease, DISEASES[selected_disease])

    def update_disease(self, disease_name, disease_details):
        self.disease = {
            "name": disease_name,
            "details": disease_details
        }

    def update_diagnosis_result(self, result):
        self.diagnosis_result = result

    def __str__(self):
        disease_info = (
            f"{self.disease['name']} "
            f"(Diagnosis: {self.disease['details']['diagnosis_time']}h, "
            f"Operation: {self.disease['details']['operation_time']}h, "
            f"Hospitalization: {self.disease['details']['hospitalization_time']}d)"
            if self.disease else "None"
        )
        return (
            f"Age: {self.age}, Gender: {self.gender}, Disease: {disease_info}, Diagnosis Result: {self.diagnosis_result}"
        )
