import numpy as np
import uuid
from medical_data import DISEASES
import Patients
from RandomGenerators import generate_hospitalization_time, generate_operation_time


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

    def diagnose_patient(self, patient, diseases, scale_correct=0.8, scale_incorrect=2.0):
        """
        Diagnoses a patient using probabilities based on an exponential distribution.
        Assigns a dynamic hospitalization time.

        Returns:
            bool: True if diagnosis is successful, False otherwise.
        """
        if self.available:
            self.occupied()
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
            diagnosed_disease_details = diseases[diagnosed_disease].copy()

            if diagnosed_disease_details["mean_operation_time"] is not None:
                diagnosed_disease_details["operation_time"] = generate_operation_time(
                    diagnosed_disease_details["mean_operation_time"])
            else:
                diagnosed_disease_details["operation_time"] = None

            hospitalization_time = generate_hospitalization_time(diagnosed_disease_details["hospitalization_time"])
            patient.diagnosis_time = patient.generate_diagnosis_time()

            diagnosed_disease_details["hospitalization_time"] = hospitalization_time
            patient.update_diagnosis_result({
                "name": diagnosed_disease,
                "details": diagnosed_disease_details
            })

            return True
        else:
            return False

    def treat(self, patient: Patients.Patient):
        if self.available:
            self.occupied()
            return True
        return False
    
    def check_status(self, patient: Patients.Patient): # add it to status events connected to treatment event
        if patient.survival_prob < 0.9* DISEASES[patient.disease['name']]['probability']:
            if patient.survival_prob < 0.1:
                patient.dead = True
                return True # Classify as dead
            patient.get_diagnosis([self]) # rediagnose patient, because he doesn't get better
            return False
        return True


    def __str__(self):
        return f"ID: {self._id}, Specialization: {self.specialization}, Worktime: {self.worktime}, Available: {self.available}"