import json
import numpy as np
import matplotlib.pyplot as plt
from difflib import get_close_matches
from monte_carlo import monte_carlo_curve

# Load database
with open("acid_database.json", "r") as f:
    acid_database = json.load(f)

def get_Ka_from_user(acid_name):

    if acid_name in acid_database:
        return acid_database[acid_name]

    matches = get_close_matches(acid_name, acid_database.keys(), n=1, cutoff=0.6)

    if matches:
        print("Did you mean:", matches[0], "?")
        return acid_database[matches[0]]

    else:
        print("Acid not found.")
        Ka = float(input("Enter Ka manually: "))
        acid_database[acid_name] = Ka
        return Ka


acid1 = input("Enter first acid name: ").lower()
acid2 = input("Enter second acid name: ").lower()

Ka1 = get_Ka_from_user(acid1)
Ka2 = get_Ka_from_user(acid2)

acid_initial = 0.01
base_initial = 0.01
NaOH_conc = 0.1

vol1, mean1, std1 = monte_carlo_curve(Ka1, acid_initial, base_initial, NaOH_conc)
vol2, mean2, std2 = monte_carlo_curve(Ka2, acid_initial, base_initial, NaOH_conc)

plt.plot(vol1, mean1, label=acid1)
plt.fill_between(vol1,
                 np.array(mean1)-np.array(std1),
                 np.array(mean1)+np.array(std1),
                 alpha=0.2)

plt.plot(vol2, mean2, label=acid2)
plt.fill_between(vol2,
                 np.array(mean2)-np.array(std2),
                 np.array(mean2)+np.array(std2),
                 alpha=0.2)

plt.xlabel("Volume of NaOH added (mL)")
plt.ylabel("pH")
plt.title("Comparative Monte Carlo Titration Curves")
plt.legend()
plt.show()
