class Patient:
    def __init__(self, age, gender, diagnosis = None, symptoms = None, priority = None, hospital_days = None , surival_prob = None):
        self.age = age
        self.gender = gender
        self.diagnosis = diagnosis
        self.symptoms = symptoms if symptoms else []
        self.priority = priority
        self.hospital_days = 0
        self.surival_prob = 1.0

    def add_symptoms(self, symptom):
        self.symptoms.append(symptom)

    def update_diagnosis(self, new_diagnosis):
        self.diagnosis = new_diagnosis

    def set_priority(self, priority):
        self.priority = priority

    def __str__(self):
        return f"Age: {self.age}, Gender: {self.gender}, Diagnosis: {self.diagnosis}, Symptoms: {', '.join(self.symptoms)}, Priority: {self.priority}"
