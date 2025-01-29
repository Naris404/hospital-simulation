import Patients
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
        self.doctors_special = []
        self.rooms = {'rooms': capacity // 10, 'available': capacity // 10}
        self.waiting_patients = []

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
        self.doctors_special.append(doctor)

    def remove_patient(self, patient: Patients.Patient):
        """
        Removes a patient from the ward.

        Args:
            patient (Patients.Patient): The patient to remove.
        """
        try:
            self.patients.remove(patient)
            self.capacity += 1
        except:
            return False
        return True

    def treatment(self, patient: Patients.Patient):
        """
        Treats a patient with a doctor.

        Args:
            patient (Patients.Patient): The patient to treat.
        """
        free_doctor = None
        free_room = None
        for doctor in self.doctors_special:
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
            return True
        else:
            return False