import Patients
import Doctors


class Room:
    def __init__(self, is_available: bool = True):
        self.is_available = is_available
        self.end_of_treatment = None

    def occupied(self):
        self.is_available = False

    def free(self):
        self.is_available = True


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
        self.rooms = [Room() for _ in range(capacity // 10)]

    def add_patient(self, patient: Patients.Patient):
        """
        Adds a patient to the ward.

        Args:
            patient (Patients.Patient): The patient to add.

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

    def remove_patient(self, patient: Patients.Patient):
        """
        Removes a patient from the ward.

        Args:
            patient (Patients.Patient): The patient to remove.
        """
        self.patients.remove(patient)
        self.capacity += 1

    def treatment(self, patient: Patients.Patient, current_time):
        """
        Treats a patient with a doctor.

        Args:
            patient (Patients.Patient): The patient to treat.
        """
        free_doctor = None
        free_room = None
        for doctor in self.doctors:
            if doctor.available:
                free_doctor = doctor
                break

        for room in self.rooms:
            if room.is_available:
                free_room = room
                break

        if free_doctor != None and free_room != None:
            free_room.occupied()
            free_doctor.treat(patient)
            free_room.end_of_treatment = current_time + patient.diagnosis_result['name']['details']['operation_time']
            return True
        else:
            return False