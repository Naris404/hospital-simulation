from Hospitals import Hospital
import Patients
from Parameters import QUEUE_LENGTH, N
from StatusEvents import *
from TimeEvents import *
import matplotlib.pyplot as plt


def simulation(queue_length):
    status_events = ['assign_patient_to_ward(waiting_patients, hospital, time_events, time)',
                     'diagnose_patient(hospital, time_events, time)',
                     'treat_patient(hospital.wards, time, time_events, waiting_patients)']

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

    while len(time_events) > 0 or len(waiting_patients) > 0 or any(ward.waiting_patients for ward in hospital.wards.values()) or any(ward.patients for ward in hospital.wards.values()):
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
    dead_patients = []

    for time, patient in discharged_patients:
        # print(patient)
        if not patient.dead:
            hospitalization_time.append(time - patient.arrival_time)
        else:
            dead_patients.append(patient)
    print(len(discharged_patients))
    return sum(hospitalization_time) / queue_length, dead_patients


def simulate_n_times(N, queue_length):
    avg_hospitalization_time = []
    avg_dead_people = []
    for n in range(N):
        t, d = simulation(queue_length)
        avg_hospitalization_time.append(t)
        avg_dead_people.append(d)
    return avg_hospitalization_time, avg_dead_people


if __name__ == '__main__':
    avg_hosp_time, avg_dead_people = simulate_n_times(N, QUEUE_LENGTH)
    d = [len(a) for a in avg_dead_people]
    avg_hosp_time = [e/60 for e in avg_hosp_time]
    print(f"Average hospitalization time: {sum(avg_hosp_time)/N} hours")
    print(f"Average dead people: {sum(d)/len(d)}")

    # plot average hospitalization time
    a = [e/60 for e in avg_hosp_time]
    ylabel = "Hours"
    if max(a) > 100:
        a = [e/24 for e in a]
        ylabel = "Days"
    # plt.scatter(list(range(1,len(avg_hosp_time)+1)), a)
    # plt.ylabel(ylabel)
    # plt.xlabel("Number of patients")
    # plt.title("Average hospitalization time")
    # plt.show()

    plt.hist(a, bins=10, edgecolor='black')
    plt.xlabel(ylabel)
    #plt.show()