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

# Ensure DataFrame is correctly created
print("Initial Results DataFrame:")
print(results_df.head())

# Constants for Darcy's Law
A = 1.0  # Cross-sectional area (m^2)
mu = 0.001  # Viscosity of CO2 (Pa.s)
L = 1.0  # Length of the flow path (m)

# Check if required columns exist in the DataFrame
required_columns = ['Permeability', 'Pressure']
missing_columns = [col for col in required_columns if col not in results_df.columns]

if missing_columns:
    raise ValueError(f"Missing columns in the DataFrame: {missing_columns}")

# Ensure pressure gradient is positive (Pressure - 1 > 0)
if any(results_df['Pressure'] - 1 <= 0):
    raise ValueError("Some pressure values are too low to calculate a valid flow rate.")

# Calculate flow rates using Darcy's law
results_df['Flow Rate'] = results_df['Permeability'] * A * (results_df['Pressure'] - 1) / (mu * L)

# Display the updated DataFrame
print("Results with Flow Rates:")
print(results_df.head())

# Save the DataFrame to a CSV file
output_path = r"C:\Users\ENG. JMK\OneDrive\Desktop\SEISMIC ANALYSIS\simulation_results_with_flow_rates.csv"
results_df.to_csv(output_path, index=False)
print(f"Results saved to: {output_path}")

# Plot histogram of flow rates
plt.figure(figsize=(8, 6))
plt.hist(results_df['Flow Rate'], bins=30, color='purple', alpha=0.7)
plt.title('Flow Rate Distribution')
plt.xlabel('Flow Rate (m^3/s)')
plt.ylabel('Frequency')
plt.grid()
plt.show()
