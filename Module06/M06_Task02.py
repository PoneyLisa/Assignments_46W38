import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load the Excel file and read the Exercise 2 sheet
file_path = 'C:/Users/pcber/OneDrive/Master_in_Wind_Energy/DTU_Master_in_Wind_Energy/' \
    '46W38 Scientific Programming for Wind Energy/Module06_Data Visualization with Matplotlib/Assignment/Module 6 - Exercises Data.xlsx'
df = pd.read_excel(file_path, sheet_name='Exercise 2')

# Print summary statistics
print("=" * 60)
print("WIND TURBINE DATA ANALYSIS - TASK 2")
print("=" * 60)
print("\nData Summary:")
print(df.describe())

# Get the wind speed column and metrics
wind_speed = df['Wind speed (m/s)']
metrics = df.columns[1:]  # All columns except wind speed

# Define colors for each metric
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
markers = ['o', 's', '^', 'D']

# Create the main figure with 2x2 subplots
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.flatten()

# Plot each metric with custom styling
for i in range(len(metrics)):
    metric = metrics[i]
    color = colors[i]
    marker = markers[i]
    ax = axes[i]
    
    # Plot the data with custom styling
    ax.plot(wind_speed, df[metric], 
            marker=marker, 
            color=color,
            linewidth=2.5, 
            markersize=7,
            markeredgecolor='white',
            markeredgewidth=1.5,
            label=metric)

    
    # Customize the subplot
    ax.set_xlabel('Wind Speed (m/s)', fontsize=11, fontweight='bold')
    ax.set_ylabel(metric, fontsize=11, fontweight='bold')
    ax.set_title(f'{metric} vs Wind Speed', fontsize=12, fontweight='bold', pad=10)
    
    # Add grid with custom style
    ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)
    ax.set_facecolor('#f8f9fa')
    
    # Format tick labels
    ax.tick_params(axis='both', which='major', labelsize=10)

# Show the plot
plt.show()