from Hospitals import Hospital
import Patients

if __name__ == '__main__':
    status_events = []
    time_events = []

    hospital = Hospital()
    hospital.init_hospital()

    queue = Patients.Patients_Queue()