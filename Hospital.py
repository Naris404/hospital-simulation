import Wards


class Hospital:
    def __init__(self):
        """
        Initializes a Hospital instance with an empty list of wards.

        """
        self.wards = []

    def add_ward(self, ward: Wards.Ward):
        """
        Adds a Ward to the hospital.

        Args:
            ward (Wards.Ward): The Ward to be added.
        """
        self.wards.append(ward)