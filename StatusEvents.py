from TimeEvents import *


def assign_patient_to_ward(waiting_patients, hospital, time_events, time):
    if waiting_patients:
        for doctor in hospital.doctors:
            if doctor.available:
                waiting_patients[0].get_assign_to_ward(doctor)
                patient = waiting_patients.pop(0)
                time_events.append([time + patient.diagnosis_time,
                                    end_of_assignment_patient,
                                    [patient, hospital]])
                return True
    return False


def diagnose_patient(hospital, time_events, time):
    i = False
    for department, ward in hospital.wards.items():
        if ward.waiting_patients:
            if ward.waiting_patients[0].get_diagnosis(ward.doctors_special):
                patient = ward.waiting_patients.pop(0)
                # Appending time_events with end of diagnosis
                time_events.append([time + patient.diagnosis_time,
                                    end_of_diagnosis,
                                    [hospital, patient]])
                i = True
    if i:
        return True
    return False


def treat_patient(wards, time, time_events, waiting_patients):
    i = False
    for department, ward in wards.items():
        for patient in ward.patients:
            if patient.diagnosis_result['details']['operation_time'] == None and not patient.to_get_discharge:
                time_events.append([time + patient.diagnosis_result['details']['hospitalization_time'],
                                    discharge_patient,
                                    [patient, ward]])
                patient.to_get_discharge = True
                i = True
            elif patient.get_treatment(ward):
                time_events.append([time + patient.diagnosis_result['details']['operation_time'],
                                    end_of_treatment,
                                    [patient, ward, time_events, time+patient.diagnosis_result['details']['operation_time']]])
                i = True
    if i:
        return True
    return False
