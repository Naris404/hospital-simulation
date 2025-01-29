from Patients import Patient
from Hospitals import Hospital
from Doctors import Doctor
from Wards import Ward

def end_of_assignment_patient(patient, hospital):
    patient.end_of_assignment(hospital)


def end_of_diagnosis(hospital, patient):
    hospital.wards[patient.diagnosis_result['details']["department"]].capacity -= 1
    hospital.wards[patient.diagnosis_result['details']["department"]].add_patient(patient)
    for doctor in patient.doctors:
        doctor.free()
    patient.doctors = []


def end_of_treatment(patient, ward, time_events, time):
    ward.rooms['available'] += 1
    for doctor in patient.doctors:
        doctor.free()
    patient.doctors = []
    # if patient.disease['name'] == patient.diagnosis_result['name']:
    #     patient.hospitalization_time = time + patient.diagnosis_result["details"]["hospitalization_time"]
    #     time_events.append([patient.hospitalization_time, discharge_patient, [patient, ward]])
    patient.hospitalization_time = time + patient.diagnosis_result["details"]["hospitalization_time"]
    time_events.append([patient.hospitalization_time, discharge_patient, [patient, ward]])
    patient.to_get_discharge = True


def discharge_patient(patient, ward):
    patient.discharge(ward)
    return patient
