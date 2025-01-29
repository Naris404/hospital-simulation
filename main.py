from Hospitals import Hospital
import Patients
from Parameters import QUEUE_LENGTH, N
from StatusEvents import *
from TimeEvents import *
import matplotlib.pyplot as plt


def simulation(queue_length):
    status_events = ['assign_patient_to_ward(waiting_patients, hospital, time_events, time)',
                     'diagnose_patient(hospital, time_events, time)',
                     'treat_patient(hospital.wards, time, time_events)']

    time_events = []
    waiting_patients = []
    discharged_patients = []  # [time when patient was discharged, patient]

    # Creating a hospital
    hospital = Hospital()
    hospital.init_hospital()

    # Creating and filling a queue
    q = Patients.Patients_Queue()
    q.fill_queue(queue_length)

    # Sorting the queue by the coming time
    q.sort()

    # Setting time to time of coming first patient
    time = q.queue[0].arrival_time

    # Putting patients to time events list
    for patient in q.queue:
        time_events.append([patient.arrival_time, waiting_patients.append, [patient]])
    time_events.sort(key=lambda x: x[0])

    # q.print_queue()

    while len(time_events) > 0 or len(waiting_patients) > 0:

        # Check time events
        if len(time_events) > 0:
            event = time_events.pop(0)
            if event[1] == discharge_patient:
                discharged_patients.append([time, event[1](*event[2])])

                # print(f'eval discharge event: {event}', end='\n\n')
            else:
                event[1](*event[2])

                # print(f'eval time event: {event}')

        # Check status events
        while True:

            i = 0
            for event in status_events:
                try:
                    if eval(event):
                        i += 1
                        # print(f'eval status event: {event}')
                except:
                    pass

            if i == 0:
                break
        try:
            time_events.sort(key=lambda x: x[0])
            time = time_events[0][0]
        except:
            pass

    # Collecting data
    hospitalization_time = []

    for time, patient in discharged_patients:
        # print(patient.__str__())
        hospitalization_time.append(time - patient.arrival_time)
    return sum(hospitalization_time) / queue_length


def simulate_n_times(N, queue_length):
    avg_hospitalization_time = []
    for n in range(N):
        avg_hospitalization_time.append(simulation(queue_length))
    return avg_hospitalization_time


if __name__ == '__main__':
    avg_hosp_time = simulate_n_times(N, QUEUE_LENGTH)
    print(avg_hosp_time, sum(avg_hosp_time) / N)

    # plot average hospitalization time
    plt.plot(avg_hosp_time)
    plt.show()