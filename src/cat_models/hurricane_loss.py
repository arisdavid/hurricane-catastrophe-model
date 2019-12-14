import numpy as np


def hurricane_loss_model(florida_landfall_rate, florida_mean, florida_sigma,
                         gulf_landfall_rate, gulf_mean, gulf_sigma, num_sim):
    total_loss = 0
    # O(n^2)
    for i in range(0, num_sim):
        simulation_loss = 0
        n_florida_events = florida_landfall_rate
        for n in range(0, n_florida_events):
            p1 = np.random.lognormal(florida_mean, florida_sigma)
            simulation_loss += p1

        n_gulf_events = gulf_landfall_rate
        for n in range(0, n_gulf_events):
            p2 = np.random.lognormal(gulf_mean, gulf_sigma)
            simulation_loss += p2

        total_loss += simulation_loss
    mean_loss = total_loss / num_sim

    return mean_loss