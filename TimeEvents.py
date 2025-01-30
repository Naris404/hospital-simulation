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


def end_of_treatment(patient, ward, time_events, time, waiting_patients):
    patient.to_get_discharge = patient.doctors[0].check_status(patient)
    ward.rooms['available'] += 1
    for doctor in patient.doctors:
        doctor.free()
    patient.doctors = []
    if patient.to_get_discharge: # correct diagnosis, well recovered - discharge
        time_events.append([time+patient.diagnosis_result['details']['hospitalization_time'], discharge_patient, [patient, ward]])
    else: # patient didn't fully recover - incorrect diagnosis
        ward.patients.remove(patient)
        time_events.append([time, ward.waiting_patients.append, [patient]])


def discharge_patient(patient, ward):
    patient.discharge(ward)
    return patient
