import numpy as np
import uuid
from medical_data import DISEASES
import Patients


class Doctor:
    def __init__(self, specialization: str, worktime: int):
        """
        Initializes a Doctor instance with a specialization and worktime.
        """
        self._id = uuid.uuid4()
        self.specialization = specialization
        self.worktime = worktime
        self.available = True

    def occupied(self):
        self.available = False

    def free(self):
        self.available = True

    def treat(self, patient: Patients.Patient):
        self.occupied()
        prob = DISEASES[patient.disease['name']]['probability']
        # change of survival probability based on the correctness of diagnosis
        try:
            if patient.diagnosis_result == patient.disease['name']:
                if patient.survival_prob * 1.2 >= 1:
                    patient.survival_prob = 1
                else:
                    patient.survival_prob *= 1.2
                # patient.survival_prob *= min(1, 1 + prob - np.random.normal(prob, 0.1))
            else:
                patient.survival_prob *= 0.8
        except:
            return False
        return True

    def diagnose_patient(self, patient, diseases, scale_correct=0.8, scale_incorrect=2.0):
        """
        Diagnoses a patient using probabilities based on an exponential distribution.

        Returns:
            str: The diagnosed disease name.
        """
        if self.available:
            self.available = False
            true_disease = patient.disease["name"]
            department = patient.disease["details"]["department"]

            relevant_diseases = {
                d: diseases[d] for d in diseases if diseases[d]["department"] == department
            }

            disease_names = list(relevant_diseases.keys())
            weights = [
                np.random.exponential(scale_correct if d == true_disease else scale_incorrect)
                for d in disease_names
            ]

            probabilities = [w / sum(weights) for w in weights]

            diagnosed_disease = np.random.choice(disease_names, p=probabilities)

            patient.update_diagnosis_result(diagnosed_disease)
            return True
        else:
            return False

    def __str__(self):
        return f"ID: {self._id}, Specialization: {self.specialization}, Worktime: {self.worktime}, Available: {self.available}"