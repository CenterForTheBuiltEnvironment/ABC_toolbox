import os
import numpy as np
import matplotlib.pyplot as plt

# Parameter settings
C = 500000  # Heat capacity of room air (J/K), calculated for an average house
h = 2       # Heat transfer coefficient (W/(m^2・K))
A = 400     # Surface area through which heat escapes (m^2)
T_out = 0   # Outdoor temperature (°C)
Q = 5000    # Heat supplied from a heat source (W), assuming a moderate heating system
T_initial = 20 # Initial indoor temperature (°C)

# Time settings
t_end = 3600  # Total time for calculation (seconds)
dt = 60       # Time step (seconds)

# Number of time steps
n_steps = int(t_end / dt)

# Initial conditions
temperatures = np.zeros(n_steps)
temperatures[0] = T_initial

# Solving the equation using the Explicit Euler Method
for i in range(1, n_steps):
    dTdt = (Q - h * A * (temperatures[i-1] - T_out)) / C
    temperatures[i] = temperatures[i-1] + dTdt * dt

# Generating the time axis
time = np.linspace(0, t_end / 60, n_steps)  # Convert seconds to minutes

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(time, temperatures, label='Room Temperature', marker='o')
plt.xlabel('Time (minutes)')
plt.ylabel('Temperature (°C)')
plt.title('Room Temperature Over Time')
plt.legend()
plt.grid(True)

save_path = "C:\\Users\\monyo\\PycharmProjects\\ABC_JSON_schema\\figure"
plt.savefig(os.path.join(save_path, "example_transient_heat_transfer.svg"))
plt.show()