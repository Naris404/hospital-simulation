import random

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

    # Setting time to time of coming first patient
    time = queue.queue[0].hospital_days #change to coming time
    status_events.append([random.choice(hospital.doctors).diagnose_patient, (queue.queue[0], DISEASES)])


    while len(time_events) > 0 or len(status_events) > 0 or len(queue.queue) > 0:
        event = time_events.pop()
        event[0](*event[1])


