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

    def diagnose_patient(self, patient, diseases, scale_correct=0.8, scale_incorrect=2.0):
        """
        Diagnoses a patient using probabilities based on an exponential distribution.
        Returns:
            str: The diagnosed disease name.
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

            patient.update_diagnosis_result({"name": diagnosed_disease, "details": diseases[diagnosed_disease]})
            return True
        else:
            return False

    def treat(self, patient: Patients.Patient):
        if self.available:
            self.occupied()
            return True
        return False
    
    def check_status(self, patient: Patients.Patient): # add it to status events connected to treatment event
        # if patient.hospital_days > DISEASES[patient.disease['name']]['hospitalization_time'] or patient.survival_prob < DISEASES[patient.disease['name']]['probability']:
        #     return patient.get_diagnosis([self]) # rediagnose patient, because he doesn't get better
        # return True
        if patient.diagnosis_result['name'] == patient.disease['name']:
            return True
        return False


    def __str__(self):
        return f"ID: {self._id}, Specialization: {self.specialization}, Worktime: {self.worktime}, Available: {self.available}"