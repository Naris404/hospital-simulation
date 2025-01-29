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
    if patient.to_get_discharge: # correct diagnosis, well recovered - discharge
        if patient.diagnosis_result['details']['operation_time'] != None:
            ward.rooms['available'] += 1
            for doctor in patient.doctors:
                doctor.free()
            patient.doctors = []
        time_events.append([time+patient.diagnosis_result['details']['hospitalization_time'], discharge_patient, [patient, ward]])
    else: # patient didn't fully recover - incorrect diagnosis
        time_events.append([time, waiting_patients.append, [patient]])


def check_status(patient, ward, time_events, time, waiting_patients):
    for doctor in ward.doctors_special:
        if doctor.available:
            patient.to_get_discharge = doctor.check_status(patient)
            if patient.diagnosis_result['details']['operation_time'] == None:
                a = patient.diagnosis_result['details']['hospitalization_time']
            else:
                a = patient.diagnosis_result['details']['operation_time']
            time_events.append([time + a,
                                    end_of_treatment,
                                    [patient, ward, time_events, time+a, waiting_patients]])
            return
    time_events.append([time + 50, # wait for another doctor if everyone is occupied
                            check_status,
                            [patient, ward, time_events, time, waiting_patients]])



def discharge_patient(patient, ward):
    patient.discharge(ward)
    return patient
