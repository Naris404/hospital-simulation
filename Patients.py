import random
from RandomGenerators import Age_Generator
from medical_data import DISEASES
import uuid

class Patient:
    def __init__(self, age, gender, disease=None, diagnosis_result=None, hospital_days=0, survival_prob=1.0):
        self._id = uuid.uuid4()
        self._age = age
        self._gender = gender
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
            f"Age: {self._age}, Gender: {self._gender}, Disease: {disease_info}, Diagnosis Result: {self.diagnosis_result}"
        )

class Patients_Queue:
    def __init__(self):
        """
        Patients_Queue class is responsible for managing a queue of patients.

        Attributes:
            queue (list): A list of Patient objects
        """
        self.queue = []

    def add_patient(self, patient = None):
        if patient is None:
            patient = Patient(Age_Generator(), random.choice(["male", "female"]))
        self.queue.append(patient)
        self.queue[-1].assign_random_disease()

    def pop_patient(self):
        return self.queue.pop(0)

    def remove_patient(self, patient):
        self.queue.remove(patient)

    def print_queue(self):
        for patient in self.queue:
            print(patient.__str__())
        print('\n', "-" * 125, '\n', sep='')

    def fill_queue(self, n):
        for _ in range(n):
            self.add_patient()

    def sort(self):
        self.queue.sort(key=lambda x: x.hospital_days)                      #change to coming time