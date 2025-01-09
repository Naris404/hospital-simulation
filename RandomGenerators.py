def Age_Generator():
    import numpy as np
    import matplotlib.pyplot as plt

    # Data from the table
    age_groups = np.array(
        [2, 7, 12, 17, 22, 27, 32, 37, 42, 47, 52, 57, 62, 67, 72, 77, 82, 87, 92, 97])  # Midpoints of age ranges
    probabilities_male = np.array(
        [0.63, 0.07, 0.09, 0.21, 0.25, 0.29, 0.45, 0.62, 0.90, 1.49, 2.62, 3.68, 5.97, 9.62, 14.71, 20.58, 16.80, 14.11,
         5.75, 1.17])
    probabilities_female = np.array(
        [0.48, 0.06, 0.08, 0.11, 0.15, 0.23, 0.32, 0.51, 0.76, 1.20, 1.95, 2.57, 3.99, 6.31, 10.54, 17.30, 17.78, 19.94,
         12.01, 3.70])

    # Combine probabilities by taking a simple average of male and female percentages
    combined_probabilities = (probabilities_male + probabilities_female) / 2

    # Normalize the combined probabilities to create a PDF
    pdf = combined_probabilities / np.sum(combined_probabilities)

    # Create the CDF
    cdf = np.cumsum(pdf)

    # Function to generate random ages
    def generate_random_age_combined(age_groups, cdf, n=1):
        """
        Generate random ages based on the combined CDF and age groups.
        :param age_groups: Array of age groups (midpoints or ranges)
        :param cdf: Cumulative distribution function
        :param n: Number of random samples to generate
        :return: Array of random ages
        """
        random_values = np.random.rand(n)  # Uniform random numbers
        random_ages = np.interp(random_values, cdf, age_groups)  # Map uniform to the distribution
        return np.round(random_ages).astype(int)

    return generate_random_age_combined(age_groups, cdf)


def generate_patient_arrival_times(mean_interval: float, num_patients: int):
    import numpy as np
    """
    Generuje czasy przyjścia pacjentów do szpitala na podstawie rozkładu wykładniczego.

    Args:
        mean_interval (float): Średni czas (w minutach) między przyjściami pacjentów.
        num_patients (int): Liczba pacjentów do wygenerowania.

    Returns:
        list: Lista czasów przyjścia (w minutach) od początku symulacji.
    """
    inter_arrival_times = np.random.exponential(mean_interval, num_patients)

    arrival_times = np.cumsum(inter_arrival_times)

    return arrival_times

def generate_diagnosis_time(disease_name: str):
    import numpy as np
    from medical_data import DISEASES
    """
    Generuje czas diagnozy dla pacjenta na podstawie rozkładu wykładniczego.

    Args:
        mean_diagnosis_time (float): Średni czas diagnozy w minutach.

    Returns:
        float: Czas diagnozy w minutach.
    """
    mean_diagnosis_time = DISEASES[disease_name]['mean_diagnosis_time']
    return np.random.exponential(mean_diagnosis_time)



