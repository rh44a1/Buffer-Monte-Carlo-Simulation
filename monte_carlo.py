import random
import statistics
from buffer_model import calculate_pH

def monte_carlo_curve(Ka, acid_initial, base_initial, NaOH_conc, runs=300):

    mean_curve = []
    std_curve = []
    volumes = []

    for volume_added in range(0, 151):
        simulation_results = []

        for _ in range(runs):
            Ka_var = Ka * random.uniform(0.9, 1.1)
            acid_var = acid_initial * random.uniform(0.9, 1.1)
            base_var = base_initial * random.uniform(0.9, 1.1)

            pH = calculate_pH(volume_added, Ka_var, acid_var, base_var, NaOH_conc)
            simulation_results.append(pH)

        mean_curve.append(statistics.mean(simulation_results))
        std_curve.append(statistics.stdev(simulation_results))
        volumes.append(volume_added)

    return volumes, mean_curve, std_curve
