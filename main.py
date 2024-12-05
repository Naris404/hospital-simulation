import random
from medical_data import SYMPTOMS

def generate_symptoms(symptom_list):
    num_symptoms_distribution = [0, 1, 2, 3, 4, 5, 6]  # Liczby objawów
    num_symptoms_weights = [0.05, 0.3, 0.2, 0.2, 0.15, 0.07, 0.03]  # Wagi
    num_symptoms = random.choices(num_symptoms_distribution, num_symptoms_weights, k=1)[0]

    if num_symptoms == 0:
        return []

    symptoms, probabilities = zip(*symptom_list)

    return random.choices(symptoms, probabilities, k=num_symptoms)

patien_symptoms = generate_symptoms(SYMPTOMS)
print(patien_symptoms)