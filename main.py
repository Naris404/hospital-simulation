import random

from Tools.scripts.patchcheck import status
from fontTools.merge.util import current_time

from Hospitals import Hospital
import Patients
from medical_data import DISEASES
from Parameters import QUEUE_LENGHT

if __name__ == '__main__':
    status_events = []
    time_events = []

    # Creating a hospital
    hospital = Hospital()
    hospital.init_hospital()

    # Creating and filling a queue
    queue = Patients.Patients_Queue()
    queue.fill_queue(QUEUE_LENGHT)

    # Sorting the queue by the coming time
    queue.sort()

    # List of waiting Patients
    waiting_patients = []

    # Setting time to time of coming first patient
    time = queue.queue[0].hospital_days #change to coming time
    time_events.append([queue.queue[0].coming_time, waiting_patients.append, (queue.pop_patient())])
    status_events.append([random.choice(hospital.doctors).diagnose_patient, (waiting_patients[0], DISEASES)])


    while len(time_events) > 0 or len(status_events) > 0 or len(queue.queue) > 0 or len(waiting_patients) > 0:

        # Check time events
        if len(time_events) > 0:
            time_events.sort(key=lambda x: x[0])
            event = time_events.pop()
            event[1](*event[2])

        # Check status events
        while len(status_events) != 0:

            status_events_copy = status_events.copy()

            for event in status_events_copy:
                if event[0](*event[1]):
                    status_events.remove(event)
            else:
                if status_events == status_events_copy:
                    break

        # Check queue
        if queue.queue[0].coming_time <= time_events[0][0] and queue.queue[0].coming_time >= current_time:
            time_events.append([queue.queue[0].coming_time, waiting_patients.append, (queue.pop_patient())])


        for doctor in hospital.doctors:
            if doctor.available:
                status_events.append([doctor.diagnose_patient, (waiting_patients.pop(), DISEASES)])
                break



