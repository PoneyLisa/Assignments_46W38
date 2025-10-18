import matplotlib.pyplot as plt
import numpy as np

# Data for EU energy generation sources in 2023
energy_sources = ['Crude oil', 'Natural gas', 'Renewable energy', 'Solid fuels', 'Nuclear Energy']
percentages = [37.7, 20.4, 19.5, 10.6, 11.8]

# Create figure with subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Color scheme for better visualization
colors = ['#8B4513', '#4682B4', '#228B22', '#696969', '#FFD700']

# 1. Bar chart
bars = ax1.bar(energy_sources, percentages, color=colors, edgecolor='black', linewidth=1.2)
ax1.set_ylabel('Percentage of Total Energy Generation (%)', fontsize=12, fontweight='bold')
ax1.set_title('EU Energy Generation Sources - 2023\n(Bar Chart)', fontsize=14, fontweight='bold')
ax1.set_ylim(0, 45)
ax1.grid(axis='y', alpha=0.3, linestyle='--')

# Add value labels on bars
for bar, percentage in zip(bars, percentages):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + 0.5,
             f'{percentage}%', ha='center', va='bottom', fontweight='bold', fontsize=10)

# Rotate x-axis labels for better readability
ax1.set_xticklabels(energy_sources, rotation=45, ha='right')

# 2. Pie chart
explode = (0.1, 0.05, 0.05, 0, 0)  # explode the largest slice (Crude oil)
wedges, texts, autotexts = ax2.pie(percentages, explode=explode, labels=energy_sources, 
                                     colors=colors, autopct='%1.1f%%', startangle=90,
                                     shadow=True, textprops={'fontsize': 10})

# Make percentage text bold
for autotext in autotexts:
    autotext.set_fontweight('bold')
    autotext.set_color('white')

ax2.set_title('EU Energy Generation Sources - 2023\n(Pie Chart)', fontsize=14, fontweight='bold')

# Overall title
fig.suptitle('Energy Generation in the European Union (2023)', fontsize=16, fontweight='bold', y=1.02)

# Add a text box with key insights
textstr = 'Key Insights:\n• Fossil fuels (oil, gas, coal) account for 68.7%\n• Renewable energy is nearly 20%\n• Nuclear provides 11.8% of energy'
props = dict(boxstyle='round', facecolor='wheat', alpha=0.8)
fig.text(0.5, -0.15, textstr, transform=ax1.transAxes, fontsize=10,
         verticalalignment='top', bbox=props)

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Save the figure
#plt.savefig('/home/claude/eu_energy_plot.png', dpi=300, bbox_inches='tight')
#print("Plot saved as 'eu_energy_plot.png'")

# Display the plot
plt.show()

# Print summary statistics
print("\n=== EU Energy Generation Sources 2023 - Summary ===")
print(f"Total percentage check: {sum(percentages)}%")
print(f"\nBreakdown by source:")
for source, pct in zip(energy_sources, percentages):
    print(f"  {source:20s}: {pct:5.1f}%")

print(f"\nFossil fuels total (Oil + Gas + Coal): {37.7 + 20.4 + 10.6:.1f}%")
print(f"Clean energy total (Renewable + Nuclear): {19.5 + 11.8:.1f}%")