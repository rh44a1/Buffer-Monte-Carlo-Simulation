import math

def calculate_pH(volume_added, Ka, acid_moles_initial, base_moles_initial, NaOH_conc):
    Kw = 1e-14

    volume_L = volume_added / 1000
    oh_moles = volume_L * NaOH_conc
    total_volume = 0.1 + volume_L

    # Before equivalence
    if oh_moles < acid_moles_initial:
        acid_moles = acid_moles_initial - oh_moles
        base_moles = base_moles_initial + oh_moles
        pKa = -math.log10(Ka)
        return pKa + math.log10(base_moles / acid_moles)

    # At equivalence
    elif abs(oh_moles - acid_moles_initial) < 1e-6:
        base_moles = base_moles_initial + oh_moles
        Kb = Kw / Ka
        base_conc = base_moles / total_volume
        OH = math.sqrt(Kb * base_conc)
        pOH = -math.log10(OH)
        return 14 - pOH

    # After equivalence
    else:
        excess_oh = oh_moles - acid_moles_initial
        OH_conc = excess_oh / total_volume
        pOH = -math.log10(OH_conc)
        return 14 - pOH
