from Hospitals import Hospital
import Patients
from Parameters import QUEUE_LENGHT


def assign_patient_to_ward(waiting_patients, hospital, time_events, time):
    for doctor in hospital.doctors:
        if doctor.available:
            if waiting_patients[0].get_assign_to_ward(doctor):
                patient = waiting_patients.pop(0)
                time_events.append([time+patient.diagnosis_time, end_of_assignment_patient, [patient, hospital]])
                return True
    return False

def end_of_assignment_patient(patient, hospital):
    patient.end_of_assignment(hospital)


def diagnose_patient(hospital, time_events, time):
    i = 0
    for department, ward in hospital.wards.items():
        try:
            if ward.waiting_patients[0].get_diagnosis(ward.doctors_special):
                patient = ward.waiting_patients.pop(0)
                # Appending time_events with end of diagnosis
                time_events.append([time + patient.diagnosis_time, end_of_diagnosis, [hospital, patient]])
                i += 1
        except:
            pass
    if i != 0:
        return True
    return False


def end_of_diagnosis(hospital, patient):
    hospital.wards[patient.diagnosis_result['details']["department"]].capacity -= 1
    hospital.wards[patient.diagnosis_result['details']["department"]].add_patient(patient)
    for doctor in patient.doctors:
        doctor.free()
    patient.doctors = []


def treat_patient(wards, time, time_events):
    i = 0
    for department, ward in wards.items():
        for patient in ward.patients:
            if patient.diagnosis_result['details']['operation_time'] == None:
                time_events.append([time + patient.diagnosis_result["details"]["hospitalization_time"], discharge_patient, [patient, ward]])
            if patient.get_treatment(ward.doctors_special):
                time_events.append([time + patient.diagnosis_result['details']['operation_time'], end_of_treatment,
                                    [patient, ward, time_events, time]])
                i += 1
    if i == 0:
        return False
    return True


def end_of_treatment(patient, ward, time_events, time):
    ward.rooms['available'] += 1
    for doctor in patient.doctors_special:
        doctor.free()
    patient.doctors_special = []
    # if patient.disease['name'] == patient.diagnosis_result['name']:
    #     patient.hospitalization_time = time + patient.diagnosis_result["details"]["hospitalization_time"]
    #     time_events.append([patient.hospitalization_time, discharge_patient, [patient, ward]])
    patient.hospitalization_time = time + patient.diagnosis_result["details"]["hospitalization_time"]
    time_events.append([patient.hospitalization_time, discharge_patient, [patient, ward]])


def discharge_patient(patient, ward):
    patient.discharge(ward)
    return patient


if __name__ == '__main__':
    status_events = ['assign_patient_to_ward(waiting_patients, hospital, time_events, time)',
                     'diagnose_patient(hospital, time_events, time)',
                     'treat_patient(hospital.wards, time, time_events)']
    time_events = []
    waiting_patients = []
    discharged_patients = []

    # Creating a hospital
    hospital = Hospital()
    hospital.init_hospital()

    # Creating and filling a queue
    q = Patients.Patients_Queue()
    q.fill_queue(QUEUE_LENGHT)

    # Sorting the queue by the coming time
    q.sort()

    # Setting time to time of coming first patient
    time = q.queue[0].arrival_time

    # Putting patients to time events list
    for patient in q.queue:
        time_events.append([patient.arrival_time, waiting_patients.append, [patient]])
    time_events.sort(key=lambda x: x[0])

    q.print_queue()

    while len(time_events) > 0 or len(waiting_patients) > 0:

        # Check time events
        if len(time_events) > 0:
            event = time_events.pop(0)
            if event[1] == discharge_patient:
                discharged_patients.append(event[1](*event[2]))

                print(f'evaluated discharge event: {event}', end='\n\n')
            else:
                event[1](*event[2])

                print(f'evaluated time event: {event}')

        # Check status events
        while True:

            i = 0
            for event in status_events:
                try:
                    if eval(event):
                        i += 1
                        print(f'evaluated status event: {event}')
                except:
                    pass

            if i == 0:
                break
        try:
            time_events.sort(key=lambda x: x[0])
            time = time_events[0][0]
            print()
        except:
            pass

    print()
    try:
        for patient in discharged_patients:
            print(patient.__str__())
    except:
        print('No discharged patients')
