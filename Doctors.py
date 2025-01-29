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
        if self.available:
            self.occupied()
            return True
        return False
    
    def check_status(self, patient: Patients.Patient): # add it to status events connected to treatment event
        if patient.hospital_days > DISEASES[patient.disease['name']]['hospitalization_time']:
            patient.get_diagnosis() # rediagnose patient, because he doesn't get better


    def __str__(self):
        return f"ID: {self._id}, Specialization: {self.specialization}, Worktime: {self.worktime}, Available: {self.available}"