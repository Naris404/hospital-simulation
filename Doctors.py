


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
        self.available = True

    def action(self):
        """
        If the doctor is available, marks them as unavailable and returns True.

        If the doctor is unavailable, returns False.

        Returns:
            bool: Whether the doctor was available
        """
        if self.available:
            self.available = False
            return True
        else:
            return False

    def rest(self):
        """
        Makes the doctor available again.

        """
        self.available = True
