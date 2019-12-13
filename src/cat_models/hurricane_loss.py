import numpy as np

def hurricane_loss_model(florida_landfall_rate, florida_mean, florida_sigma,
                         gulf_landfall_rate, gulf_mean, gulf_sigma, num_sim):

    total_loss = 0
    for i in range(0, num_sim):
        simulation_loss = 0
        n_florida_events = 1
        for n in range(0, n_florida_events):
            p = np.random.poisson(0, 1)
            print(np.mean(p))

    return 0.5


