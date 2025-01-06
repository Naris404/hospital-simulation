import numpy as np
import uuid

class Doctor:
    def __init__(self, specialization: str, worktime: int):
        """
        Initializes a Doctor instance with a specialization and worktime.
        """
        self._id =uuid.uuid4()
        self.specialization = specialization
        self.worktime = worktime
        self.available = True

    def action(self):
        if self.available:
            self.available = False
            return True
        else:
            return False

    def rest(self):
        self.available = True

    def diagnose_patient(self, patient, diseases, scale_correct=0.5, scale_incorrect=2.0):
        """
        Diagnoses a patient using probabilities based on an exponential distribution.

        Args:
            patient (Patient): The patient to diagnose.
            diseases (dict): A dictionary of all diseases available in the hospital.
            scale_correct (float): Scale parameter for the correct diagnosis probability.
            scale_incorrect (float): Scale parameter for incorrect diagnosis probabilities.

        Returns:
            str: The diagnosed disease name.
        """
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
        return diagnosed_disease

    def __str__(self):
        return f"ID: {self._id}, Specialization: {self.specialization}, Worktime: {self.worktime}, Available: {self.available}"