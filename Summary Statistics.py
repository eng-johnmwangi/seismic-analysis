import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Constants for Darcy's law
A = 1.0  # Cross-sectional area (m^2)
mu = 0.001  # Viscosity of CO2 (Pa.s)
L = 1.0  # Length of the flow path (m)

# Parameters for the new simulation
new_num_simulations = 1000
new_injection_rate_mean = 120
new_injection_rate_std = 15
new_pressure_min = 1.5
new_pressure_max = 6
new_temperature_mean = 30
new_temperature_std = 7
new_permeability_mean = 2.5
new_permeability_std = 0.6

# Generate new random samples for each parameter
np.random.seed(42)  # For reproducibility
new_injection_rates = np.random.normal(new_injection_rate_mean, new_injection_rate_std, new_num_simulations)
new_pressures = np.random.uniform(new_pressure_min, new_pressure_max, new_num_simulations)
new_temperatures = np.random.normal(new_temperature_mean, new_temperature_std, new_num_simulations)
new_permeabilities = np.random.lognormal(new_permeability_mean, new_permeability_std, new_num_simulations)

# Create a new DataFrame to store the results
new_results_df = pd.DataFrame({
    'Injection Rate': new_injection_rates,
    'Pressure': new_pressures,
    'Temperature': new_temperatures,
    'Permeability': new_permeabilities
})

# Calculate flow rates using Darcy's law
new_results_df['Flow Rate'] = (new_results_df['Permeability'] * A * (new_results_df['Pressure'] - 1) / (mu * L))

# Ensure the DataFrame is defined
print("Head of new_results_df:")
print(new_results_df.head())

# Calculate summary statistics
summary_statistics = new_results_df.describe()

# Display the summary statistics with improved formatting
print("\nSummary Statistics for the New Results DataFrame:")
print(summary_statistics.to_string())

# Save summary statistics to a CSV file
summary_output_path = r"C:\Users\ENG. JMK\OneDrive\Desktop\SEISMIC ANALYSIS\summary_statistics.csv"
summary_statistics.to_csv(summary_output_path)
print(f"\nSummary statistics saved to: {summary_output_path}")

# Plot histogram of new flow rates
plt.figure(figsize=(8, 6))
plt.hist(new_results_df['Flow Rate'], bins=30, color='orange', alpha=0.7)
plt.title('New Flow Rate Distribution')
plt.xlabel('Flow Rate (m^3/s)')
plt.ylabel('Frequency')
plt.grid()
plt.show()
