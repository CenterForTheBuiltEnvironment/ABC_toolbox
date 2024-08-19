import matplotlib.pyplot as plt
import numpy as np

# Original logistic function definition
def calculate_logistic_function(x, a, b, c, offset):
    return a / (1 + np.exp(c * (x + offset))) - b

# Adjusted logistic function to match provided image
def calculate_local_comfort(x, a, b, c, offset, right_slope, maxcomfort):
    return calculate_logistic_function(x, a, b, c, offset) + right_slope * (x + offset) + maxcomfort

# Plotting function
def plot_functions(x_values, y_values, y_modified_values, title):
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, label="Logistic Function")
    plt.plot(x_values, y_modified_values, label="Local Comfort (Modified Logistic)")
    plt.title(title)
    plt.xlabel("Local Sensation (S1)")
    plt.ylabel("Local Comfort")
    plt.grid(True)
    plt.legend()
    plt.show()

# Example parameters and data generation
x_values = np.linspace(-4, 4, 400)
a, b, c, offset = 3, 1.5, 25, 0
right_slope, maxcomfort = -0.75, 1

# Calculate y values using the adjusted function
y_values = calculate_logistic_function(x_values, a, b, c, offset)
y_modified_values = calculate_local_comfort(x_values, a, b, c, offset, right_slope, maxcomfort)

# Plotting the final adjusted functions
plot_functions(x_values, y_values, y_modified_values, "Adjusted Logistic Function and Local Comfort Plot")
