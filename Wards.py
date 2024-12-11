import patient
import Doctors


class Ward:
    def __init__(self, speciality: str, capacity: int):
        """
        Initializes a Ward instance with a speciality and capacity.

        Args:
            speciality (str): The speciality of the ward.
            capacity (int): The number of patients the ward can hold.
        """
        self.speciality = speciality
        self.capacity = capacity
        self.patients = []
        self.doctors = []
        self.rooms = []

    def add_patient(self, patient: patient.Patient):
        """
        Adds a patient to the ward.

        Args:
            patient (patient.Patient): The patient to add.

        Returns:
            bool: True if the patient was added, False if the ward is full.
        """
        if len(self.patients) < self.capacity:
            self.patients.append(patient)
            self.capacity -= 1
            return True
        return False

    def add_doctor(self, doctor: Doctors.Doctor):
        """
        Adds a doctor to the ward.

        Args:
            doctor (Doctors.Doctor): The doctor to add.
        """
        self.doctors.append(doctor)

    def remove_patient(self, patient: patient.Patient):
        """
        Removes a patient from the ward.

        Args:
            patient (patient.Patient): The patient to remove.
        """
        self.patients.remove(patient)
        self.capacity += 1

    def treatment(self, patient: patient.Patient, doctors: list[Doctors.Doctor]):
        """
        Treats a patient with a doctor.

        Args:
            patient (patient.Patient): The patient to treat.
            doctors (Doctors.Doctor): The doctors to treat the patient with.
        """