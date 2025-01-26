from Hospitals import Hospital
import Patients
from Parameters import QUEUE_LENGHT


def diagnose_patient_from_waiting_patients(waiting_patients, time_events, time):
    if waiting_patients[0].get_diagnosis(hospital.doctors):
        patient = waiting_patients.pop()

        # Appending time_events with end of diagnosis
        time_events.append([time + patient.diagnosis_time, end_of_diagnosis, [hospital, patient]])
        return True
    return False


def end_of_diagnosis(hospital, patient):
    hospital.wards[patient.diagnosis_result["department"]].capacity -= 1
    hospital.wards[patient.diagnosis_result["department"]].add_patient(patient)
    for doctor in patient.doctors:
        doctor.free()
    patient.doctors = []

def treat_patient(wards, time, time_events):
    i = 0
    for department, ward in wards.items():
        for patient in ward.patients:
            if patient.get_treatment(ward.doctors):
                time_events.append([time + patient.diagnosis_result['details']['operation_time'], end_of_treatment, [patient, ward]])
                i += 1
    if i == 0:
        return False
    return True

def end_of_treatment(patient, ward):
    ward.rooms['available'] += 1
    for doctor in patient.doctors:
        doctor.free()
    patient.doctors = []



if __name__ == '__main__':
    status_events = ['diagnose_patient_from_waiting_patients(waiting_patients, time_events, time)', ]
    time_events = []
    waiting_patients = []

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

    while len(time_events) > 0 or len(waiting_patients) > 0:

        # Check time events
        if len(time_events) > 0:
            event = time_events.pop()
            event[1](*event[2])

        # Check status events
        while True:

            i = 0
            for event in status_events:
                try:
                    if eval(event):
                        i += 1
                except:
                    pass

            if i == 0:
                break
        try:
            time_events.sort(key=lambda x: x[0])
            time = time_events[0][0]
        except:
            pass
