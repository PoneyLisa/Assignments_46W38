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
