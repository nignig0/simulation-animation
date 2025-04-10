import numpy as np

def sim_model(initial_X = 40, initial_Y = 9,
        T = 50, dt = 0.01, alpha = 1, beta = 0.1, delta = 0.2, 
          gamma = 0.9, sigma_x = 0.2, sigma_y = 0.2, K = 10):
    
    #T -> Total simulation time
    #dt -> Time step size
    N = int(T / dt)     # Number of integration steps
    t = np.linspace(0, T, N)

    # Model parameters
    #alpha -> Prey growth rate
    #beta -> Predation rate coefficient
    #delta -> Predator reproduction rate coefficient
    #gamma -> Predator death rate



    # Initialize populations: Prey (X) and Predator (Y)
    X = np.empty(N)
    Y = np.empty(N)
    X[0] = initial_X   # initial prey population
    Y[0] = initial_Y    # initial predator population

    # Euler-Maruyama Integration for the SDE
    for i in range(1, N):
        # Calculate drift terms (deterministic components)
        drift_X = alpha * X[i-1] * (1 - X[i-1] / K) - beta * X[i-1] * Y[i-1]
        drift_Y = delta * X[i-1] * Y[i-1] - gamma * Y[i-1]

        # Calculate diffusion terms (stochastic components)
        diffusion_X = sigma_x * X[i-1] * np.random.normal(0, np.sqrt(dt))
        diffusion_Y = sigma_y * Y[i-1] * np.random.normal(0, np.sqrt(dt))

        # Update populations
        X[i] = X[i-1] + drift_X * dt + diffusion_X
        Y[i] = Y[i-1] + drift_Y * dt + diffusion_Y
    
    return X, Y