import random
from RandomGenerators import Age_Generator, generate_diagnosis_time, generate_patient_arrival_times
from medical_data import DISEASES
import uuid

class Patient:
    def __init__(self, age, gender, disease=None, diagnosis_result=None, hospital_days=0, survival_prob=1.0, arrival_time=0):
        self._id = uuid.uuid4()
        self._age = age
        self._gender = gender
        self.disease = disease  # Słownik szczegółów choroby
        self.hospital_days = hospital_days
        self.survival_prob = survival_prob
        self.diagnosis_result = diagnosis_result
        self.arrival_time = arrival_time
        if self.disease is None:
            self.assign_random_disease()
        self.diagnosis_time = self.generate_diagnosis_time()

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
        self.disease = {
            "name": disease_name,
            "details": disease_details
        }

    def update_diagnosis_result(self, result):
        self.diagnosis_result = result

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
    def __init__(self, mean_interval=10, num_patients=5):
        """
        Patients_Queue class is responsible for managing a queue of patients.

        Attributes:
            queue (list): A list of Patient objects
            mean_interval (float): The mean interval (in minutes) between patient arrivals
            num_patients (int): Number of patients to generate
        """
        self.queue = []
        self.mean_interval = mean_interval  # Średni interwał czasu między przybyciem pacjentów
        self.num_patients = num_patients  # Liczba pacjentów do wygenerowania
        self.arrival_times = generate_patient_arrival_times(self.mean_interval,
                                                            self.num_patients)  # Generowanie czasów przybycia pacjentów

    def add_patient(self, patient=None):
        if patient is None:
            patient = Patient(Age_Generator(), random.choice(["male", "female"]))

        # Przypisanie wygenerowanego czasu przybycia do pacjenta
        if len(self.queue) < len(self.arrival_times):  # Sprawdzamy, czy mamy więcej pacjentów do dodania
            patient.arrival_time = self.arrival_times[len(self.queue)]  # Przypisujemy czas przybycia z listy
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
        self.queue.sort(key=lambda x: x.arrival_time)


# patients_queue = Patients_Queue(mean_interval=10, num_patients=5)
#
# patients_queue.print_queue()
#
# patients_queue.fill_queue(5)
#
# patients_queue.print_queue()
