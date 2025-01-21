import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Define parameters for the simulation
num_simulations = 1000

# Injection rate (liters per minute) - Normal distribution
injection_rate_mean = 100
injection_rate_std = 10

# Pressure (atmospheres) - Uniform distribution
pressure_min = 1
pressure_max = 5

# Temperature (Celsius) - Normal distribution
temperature_mean = 25
temperature_std = 5

# Geological permeability (mD) - Log-normal distribution
permeability_mean = 2
permeability_std = 0.5

# Generate random samples for each parameter
injection_rates = np.random.normal(injection_rate_mean, injection_rate_std, num_simulations)
pressures = np.random.uniform(pressure_min, pressure_max, num_simulations)
temperatures = np.random.normal(temperature_mean, temperature_std, num_simulations)
permeabilities = np.random.lognormal(permeability_mean, permeability_std, num_simulations)

# Create a DataFrame to store the results
results_df = pd.DataFrame({
    'Injection Rate': injection_rates,
    'Pressure': pressures,
    'Temperature': temperatures,
    'Permeability': permeabilities
})

# Display the head of the results DataFrame
print(results_df.head())

# Save the DataFrame to a CSV file
csv_file_path = "C:/Users/ENG. JMK/OneDrive/Desktop/SEISMIC ANALYSIS/simulation_results.csv"
results_df.to_csv(csv_file_path, index=False)
print(f"Results saved to {csv_file_path}")

# Plot histograms of the parameters
plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
plt.hist(results_df['Injection Rate'], bins=30, color='blue', alpha=0.7)
plt.title('Injection Rate Distribution')
plt.xlabel('Injection Rate (L/min)')
plt.ylabel('Frequency')

plt.subplot(2, 2, 2)
plt.hist(results_df['Pressure'], bins=30, color='green', alpha=0.7)
plt.title('Pressure Distribution')
plt.xlabel('Pressure (atm)')
plt.ylabel('Frequency')

plt.subplot(2, 2, 3)
plt.hist(results_df['Temperature'], bins=30, color='red', alpha=0.7)
plt.title('Temperature Distribution')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')

plt.subplot(2, 2, 4)
plt.hist(results_df['Permeability'], bins=30, color='purple', alpha=0.7)
plt.title('Permeability Distribution')
plt.xlabel('Permeability (mD)')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
