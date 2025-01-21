import pandas as pd

# Load the dataset
file_path = r'C:\Users\ENG. JMK\OneDrive\Desktop\SEISMIC ANALYSIS\seismic data.csv'  # Replace <YourUsername> with your PC username
seismic_data = pd.read_csv(file_path)

# Drop irrelevant or highly missing columns
columns_to_drop = ['nst', 'gap', 'dmin', 'rms', 'horizontalError', 
                   'depthError', 'magError', 'id', 'updated', 'net']
cleaned_data = seismic_data.drop(columns=columns_to_drop, errors='ignore')

# Drop rows with missing values in essential columns
essential_columns = ['latitude', 'longitude', 'depth', 'mag']
cleaned_data = cleaned_data.dropna(subset=essential_columns)

# Convert numerical columns to the correct data type
numeric_columns = ['latitude', 'longitude', 'depth', 'mag']
cleaned_data[numeric_columns] = cleaned_data[numeric_columns].apply(pd.to_numeric, errors='coerce')

# Drop rows with any remaining NaN values
cleaned_data = cleaned_data.dropna()

# Save cleaned data for further analysis
output_path = r'C:\Users\ENG. JMK\OneDrive\Desktop\SEISMIC ANALYSIS\cleaned_seismic_data.csv'  # Replace <YourUsername> with your PC username
cleaned_data.to_csv(output_path, index=False)

print("Data cleaning completed. Cleaned data saved as 'cleaned_seismic_data.csv' in Downloads.")

# -------------------- STATISTICAL ANALYSIS --------------------

# Summary statistics for key columns
stats_summary = cleaned_data[['depth', 'mag']].describe()
print("\nSummary Statistics:\n", stats_summary)

# Correlation matrix
correlation_matrix = cleaned_data[['depth', 'mag']].corr()
print("\nCorrelation Matrix:\n", correlation_matrix)

# -------------------- VISUALIZATION --------------------
sns.set(style="whitegrid")

# Plot: Geographic distribution of seismic events
plt.figure(figsize=(10, 6))
plt.scatter(cleaned_data['longitude'], cleaned_data['latitude'], 
            c=cleaned_data['depth'], cmap='viridis', alpha=0.6, s=10)
plt.colorbar(label='Depth (km)')
plt.title('Geographic Distribution of Seismic Events')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True)
plt.show()

# Plot: Magnitude distribution
plt.figure(figsize=(8, 6))
sns.histplot(cleaned_data['mag'], kde=True, bins=30, color="blue", alpha=0.7)
plt.title('Distribution of Earthquake Magnitudes')
plt.xlabel('Magnitude')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Plot: Depth vs Magnitude
plt.figure(figsize=(10, 6))
plt.scatter(cleaned_data['depth'], cleaned_data['mag'], alpha=0.6, c='orange', s=10)
plt.title('Depth vs. Magnitude')
plt.xlabel('Depth (km)')
plt.ylabel('Magnitude')
plt.grid(True)
plt.show()

# -------------------- STOCHASTIC MODELING --------------------

# Monte Carlo simulation for CO2 injection depth distribution
num_simulations = 1000
depth_mean = cleaned_data['depth'].mean()
depth_std = cleaned_data['depth'].std()

# Generate random samples for depth
simulated_depths = np.random.normal(depth_mean, depth_std, num_simulations)

# Plot the simulated depth distribution
plt.figure(figsize=(8, 6))
sns.histplot(simulated_depths, kde=True, color="green", bins=30, alpha=0.7)
plt.title('Simulated Depth Distribution (Monte Carlo)')
plt.xlabel('Depth (km)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

print("\nStochastic modeling completed.")