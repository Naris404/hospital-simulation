


class Doctor:
    def __init__(self, specialization: str, worktime: int):
        """
        Initializes a Doctor instance with a specialization and worktime.

        Args:
            specialization (str): The medical specialization of the doctor.
            worktime (int): The number of hours the doctor works.
        """
        self.specialization = specialization
        self.worktime = worktime
        self.actiontime = 0

    def action(self, actiontime: int):
        """
        Simulates the doctor's action by updating the actiontime attribute.
        """
        self.actiontime = actiontime

