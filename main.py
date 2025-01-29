from Hospitals import Hospital
import Patients
from Parameters import QUEUE_LENGHT
from StatusEvents import *
from TimeEvents import *

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
