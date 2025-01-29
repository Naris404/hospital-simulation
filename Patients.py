import random
from sys import path_importer_cache

# from Tools.scripts.findnocoding import needs_declaration
from numpy.f2py.cfuncs import needs

from RandomGenerators import Age_Generator, generate_diagnosis_time, generate_patient_arrival_times
from medical_data import DISEASES
import uuid


class Patient:
    def __init__(self, age, gender, disease=None, diagnosis_result=None, hospital_days=0, survival_prob=1.0,
                 arrival_time=0):
        self._id = uuid.uuid4()
        self._age = age
        self._gender = gender
        self.disease = disease  # Słownik szczegółów choroby
        self.hospital_days = hospital_days
        self.survival_prob = survival_prob
        self.diagnosis_result = diagnosis_result
        self.arrival_time = arrival_time
        self.doctors = []  # Doctors assigned to the patient (diagnosing, treating, etc.)
        if self.disease is None:
            self.assign_random_disease()
        self.diagnosis_time = None
        self.hospitalization_time = None
        self.operation_time = None
        self.needs_treatment = False
        self.to_get_discharge = False

    def assign_random_disease(self):
        diseases = list(DISEASES.keys())
        probabilities = [DISEASES[d]["probability"] for d in diseases]

        selected_disease = random.choices(diseases, probabilities, k=1)[0]
        self.update_disease(selected_disease, DISEASES[selected_disease])

    def generate_diagnosis_time(self):
        """
        Generates diagnosis time from external function.
        """
        return generate_diagnosis_time(self.disease['name'])

    def update_disease(self, disease_name, disease_details):
        try:
            self.disease = {
                "name": disease_name,
                "details": disease_details
            }
        except:
            return False
        return True

    def update_diagnosis_result(self, result):
        try:
            self.diagnosis_result = result
        except:
            return False
        return True

    def get_diagnosis(self, doctors):
        for doctor in doctors:
            if doctor.diagnose_patient(self, DISEASES):
                self.doctors.append(doctor)
                if self.diagnosis_result['details']['operation_time'] != None:
                    self.needs_treatment = True
                return True
        return False

    def get_treatment(self, ward):
        if self.needs_treatment:
            if ward.rooms['available'] > 0 and self.diagnosis_result['details']['operation_time'] != None:
                for doctor in ward.doctors_special:
                    if doctor.available:
                        self.doctors.append(doctor)
                        doctor.occupied()
                        ward.rooms['available'] -= 1
                        prob = DISEASES[self.disease['name']]['probability']
                        # change of survival probability based on the correctness of diagnosis
                        if self.diagnosis_result == self.disease['name']:
                            if self.survival_prob * 1.2 >= 1:
                                self.survival_prob = 1
                            else:
                                self.survival_prob *= 1.2
                            # patient.survival_prob *= min(1, 1 + prob - np.random.normal(prob, 0.1))
                        else:
                            self.survival_prob *= 0.3
                        self.needs_treatment = False
                        return True
        return False

    def discharge(self, ward):
        try:
            ward.patients.remove(self)
            ward.capacity += 1
        except:
            return False
        return True

    def get_assign_to_ward(self, doctor):
        self.diagnosis_time = self.generate_diagnosis_time()
        self.doctors.append(doctor)
        doctor.occupied()

    def end_of_assignment(self, hospital):
            ward = hospital.wards[self.disease['details']['department']]
            ward.waiting_patients.append(self)
            for doctor in self.doctors:
                doctor.free()
            self.doctors = []

    def update_survival_probability(self):
        # Choose rate based on patient's time spent in hospital
        if self.hospital_days > DISEASES[self.disease['name']]['hospitalization_time']:
            a = 0.9
        else:
            a = 0.99
        new_survival_prob = self.survival_prob * a
        if new_survival_prob > 1:
            self.survival_prob = 1
        self.survival_prob = new_survival_prob
        return True


    def __str__(self):
        disease_info = (
            f"{self.disease['name']} "
            f"(Diagnosis: {self.diagnosis_time} minutes, "
            f"Operation: {self.disease['details']['operation_time']}h, "
            f"Hospitalization: {self.disease['details']['hospitalization_time']}d), "
            f"Arrival Time: {self.arrival_time} minutes "
            if self.disease else "None"
        )
        return (
            f"Age: {self._age}, Gender: {self._gender}, Disease: {disease_info}, Diagnosis Result: {self.diagnosis_result}"
        )


class Patients_Queue:
    def __init__(self, mean_interval=10):
        """
        Patients_Queue class is responsible for managing a queue of patients.

        Attributes:
            queue (list): A list of Patient objects
            mean_interval (float): The mean interval (in minutes) between patient arrivals
            num_patients (int): Number of patients to generate
        """
        self.queue = []
        self.mean_interval = mean_interval  # Średni interwał czasu między przybyciem pacjentów

    def add_patient(self, patient=None):
        if patient is None:
            patient = Patient(Age_Generator(), random.choice(["male", "female"]),
                              arrival_time=generate_patient_arrival_times(self.mean_interval, 1)[0])

        self.queue.append(patient)
        self.queue[-1].assign_random_disease()

    def pop_patient(self):
        return self.queue.pop(0)

    def remove_patient(self, patient):
        try:
            self.queue.remove(patient)
        except:
            return False
        return True

    def print_queue(self):
        for patient in self.queue:
            print(patient.__str__())
        print('\n', "-" * 125, '\n', sep='')

    def fill_queue(self, n):
        for _ in range(n):
            self.add_patient()

    def sort(self):
        self.queue.sort(key=lambda x: x.arrival_time)

# patients_queue = Patients_Queue(mean_interval=10, num_patients=5)
#
# patients_queue.print_queue()
#
# patients_queue.fill_queue(5)
#
# patients_queue.print_queue()
