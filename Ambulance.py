from random import uniform
from numpy import argmin


class Ambulance:
    def __init__(self, id: int, location = 0, status="free"):
        """
        Initializes an Ambulance instance with a status, location and identification number.
        """
        self.id = id
        self.status = status
        self.location = location

    def __repr__(self):
        return f"""
        Ambulance info
        id: {self.id}
        status: {self.status}
        location: {self.location}
        """

    def accept_report(self, report_loc):
        """
        Accept report and change ambulance's status to "on a way".
        """
        if self.status == "free":
            self.status = "on a way"
            self.location = report_loc
        else:
            return 0
        return 1

    def free(self):
        """
        Change status to "free" in order to accept next reports.
        """
        if self.status != "free":
            self.status = "free"
            self.location = 0 # in a hospital
        else:
            return 0
        return 1

    def simulate_time(self, distance: float):
        """
        Simulate ambulance's time of a drive depending on a distance
        """
        avg_speed = uniform(40, 80)  # average speed in km/h
        drive_time = (distance / avg_speed) * 60  # in minutes
        return drive_time
    


class Ambulance_Queue:
    def __init__(self, n:int, priority_coeficiente = 1.5):
        self.q = {Ambulance(i):0 for i in range(n)} # {ambulance:priority}
        self.priority_coeficiente = priority_coeficiente # 


    def select_ambulance(self, priority):
        location = 999999
        best = -1
        for a in list(self.q.keys()):
            if a.status == "free":
                if a.location < location:
                    location = a.location
                    best = a
        if best == -1: # if all ambulances are taken, then look at the priorities
            min_priority = min(list(self.q.values()))
            if priority * self.priority_coeficiente > min_priority:
                j = argmin(list(self.q.values()))
                best = list(self.q.keys())[j]
        return best


    def report(self, priority):
        ambulance = self.select_ambulance(priority=priority)
        time = ambulance.simulate_time()