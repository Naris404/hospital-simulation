import Wards
import patient
from medical_data import DISEASES
import Ambulance


class Hospital:
    def __init__(self):
        """
        Initializes a Hospital instance with an empty list of wards.
        """
        self.wards = []  # Lista wszystkich oddziałów w szpitalu

    def add_ward(self, ward: Wards.Ward):
        """
        Adds a Ward to the hospital.
        Args:
            ward (Wards.Ward): The Ward to be added.
        """
        self.wards.append(ward)

    def assign_patient_to_ward(self, patient: patient.Patient):
        """
        Assign a patient to the correct ward based on their diagnosed disease.

        Args:
            patient (patient.Patient): The patient to be assigned.
        """
        # Korzystamy z diagnozy lekarza
        disease = patient.diagnosis_result['name']  # Choroba zdiagnozowana przez lekarza

        # Pobieramy specjalizację oddziału z DISEASES
        assigned_ward_speciality = DISEASES.get(disease, {}).get("department", None)

        if assigned_ward_speciality:
            # Szukamy oddziału o odpowiedniej specjalizacji
            for ward in self.wards:
                if ward.speciality == assigned_ward_speciality:
                    # Próbujemy dodać pacjenta do znalezionego oddziału
                    if ward.add_patient(patient):
                        print(f"Patient assigned to {assigned_ward_speciality} ward.")
                        return True
                    else:
                        print(f"Failed to assign patient to {assigned_ward_speciality} ward, ward is full.")
                        return False
        else:
            print(f"Error: No ward found for disease {disease}.")
            return False
