# Buffer-Monte-Carlo-Simulation

📘 **Monte Carlo Simulation of Weak Acid Buffer Titration**

Computational modeling and uncertainty analysis of weak acid–strong base titration systems using Python.

## 🧪 Project Overview

This project simulates the titration of weak acids with a strong base (NaOH) using:

- 📐 Henderson–Hasselbalch equation
- ⚗️ Stoichiometric reaction modeling
- 🎲 Monte Carlo uncertainty propagation
- 📊 Statistical sensitivity analysis
- 🔍 Comparative multi-acid visualization

Users can select from a database of 50 weak acids (or input their own), and the system dynamically generates titration curves with uncertainty bands.

## 🚀 Features

- ✔ Interactive acid selection
- ✔ 50+ weak acids database (JSON-based)
- ✔ Fuzzy name matching (intelligent input correction)
- ✔ Monte Carlo simulation (±10% parameter uncertainty)
- ✔ Mean pH curve generation
- ✔ Standard deviation sensitivity analysis
- ✔ Comparative visualization of two acids
- ✔ Modular Python architecture

## 📈 What This Project Demonstrates

- Numerical simulation of chemical equilibria
- Sensitivity of buffer systems near equivalence
- Statistical analysis of experimental uncertainty
- Clean software modularization
- Scientific computing using NumPy & Matplotlib

## 🧠 Scientific Background

For a weak acid HA:

```
HA + OH⁻ → A⁻ + H₂O
```

**Before equivalence:**

```
pH = pKa + log([A⁻]/[HA])
```

**At equivalence:**
- Hydrolysis of conjugate base considered
- Kb = Kw/Ka

**After equivalence:**
- Excess strong base determines pH

Monte Carlo simulations introduce controlled variation in:
- Ka
- Initial acid concentration
- Initial base concentration

to quantify output uncertainty.

## 🗂 Project Structure

```
buffer-montecarlo-project/
│
├── buffer_model.py       # Core pH calculation logic
├── monte_carlo.py        # Monte Carlo simulation engine
├── acid_database.json    # 50-acid Ka dataset
├── main.py               # User interaction & plotting
├── requirements.txt
└── README.md
```

## 💻 Installation

1. Clone the repository:
```bash
git clone https://github.com/rh44a1/buffer-montecarlo-project.git
cd buffer-montecarlo-project
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## ▶️ How To Run

```bash
python main.py
```

You will be prompted to:
1. Enter first acid name
2. Enter second acid name

The program will then generate comparative Monte Carlo titration curves.

## 📊 Example Comparison

Try:
- **phenol**
- **trifluoroacetic acid**

You will observe:
- Dramatically different initial pH
- Different equivalence behavior
- Variation in buffer capacity
- Distinct uncertainty profiles

## 📉 Sensitivity Analysis

The shaded region around curves represents:

```
pH_mean ± σ
```

A separate standard deviation plot identifies regions of maximum system sensitivity (typically near equivalence points).

## 🧰 Dependencies

- Python 3.x
- NumPy
- Matplotlib

## 🔬 Applications

- Buffer stability analysis
- Experimental error propagation studies
- Educational visualization tool
- Computational chemistry demonstrations
- Numerical methods coursework

## 📌 Future Improvements

- [ ] Diprotic and polyprotic acid modeling
- [ ] GUI interface (Streamlit / Tkinter)
- [ ] Real-time adjustable parameters
- [ ] Integration with chemical property APIs
- [ ] Vectorized Monte Carlo for performance optimization



## 🙏 Acknowledgments

[Add any acknowledgments here]
