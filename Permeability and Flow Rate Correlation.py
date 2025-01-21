import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Ensure global constants are defined
A = 1.0  # Cross-sectional area (m^2)
mu = 0.001  # Viscosity of CO2 (Pa.s)
L = 1.0  # Length of the flow path (m)

# Define new parameters for additional simulations
new_num_simulations = 1000

# Adjusted parameters for the new simulation
new_injection_rate_mean = 120
new_injection_rate_std = 15
new_pressure_min = 1.5
new_pressure_max = 6
new_temperature_mean = 30
new_temperature_std = 7
new_permeability_mean = 2.5
new_permeability_std = 0.6

# Generate new random samples for each parameter
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

# Ensure no invalid pressure values for Darcy's law calculation
if any(new_results_df['Pressure'] - 1 <= 0):
    raise ValueError("Some pressure values are too low for Darcy's law calculation (Pressure - 1 must be > 0).")

# Calculate flow rates using Darcy's law for the new parameters
new_results_df['Flow Rate'] = (new_results_df['Permeability'] * A * (new_results_df['Pressure'] - 1) / (mu * L))

# Display the head of the new results DataFrame
print("New Results DataFrame:")
print(new_results_df.head())

# Save the new DataFrame to a CSV file
output_path = r"C:\Users\ENG. JMK\OneDrive\Desktop\SEISMIC ANALYSIS\new_simulation_results.csv"
new_results_df.to_csv(output_path, index=False)
print(f"New results saved to: {output_path}")

# Plot histogram of new flow rates
plt.figure(figsize=(8, 6))
plt.hist(new_results_df['Flow Rate'], bins=30, color='orange', alpha=0.7)
plt.title('New Flow Rate Distribution')
plt.xlabel('Flow Rate (m^3/s)')
plt.ylabel('Frequency')
plt.grid()
plt.show()
