import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset
file_path = r'C:\Users\13176\Documents\Projects\LA_Fires_Analysis\data\cleaned_fire_data.csv'
fire_data_cleaned = pd.read_csv(file_path)

# Yearly Fire Trends
fires_per_year = fire_data_cleaned['YEAR_'].value_counts().sort_index()

# Plot the number of fires per year
plt.figure(figsize=(8, 5))
fires_per_year.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Number of Fires Per Year')
plt.xlabel('Year')
plt.ylabel('Number of Fires')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
# Save the chart to the outputs/plots folder
output_path = r'C:\Users\13176\Documents\Projects\LA_Fires_Analysis\outputs\plots\fires_per_year.png'
plt.savefig(output_path, dpi=300)
print(f"Chart saved to: {output_path}")
plt.show()

# Fire Cause Analysis
fire_causes = fire_data_cleaned['CAUSE'].value_counts()

# Plot the most common fire causes
plt.figure(figsize=(10, 6))
fire_causes.plot(kind='bar', color='coral', edgecolor='black')
plt.title('Most Common Fire Causes')
plt.xlabel('Cause')
plt.ylabel('Number of Fires')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Save the chart
output_path = r'C:\Users\13176\Documents\Projects\LA_Fires_Analysis\outputs\plots\fire_causes.png'
plt.savefig(output_path, dpi=300)
print(f"Chart saved to: {output_path}")

# Display the chart
plt.show()

# Acres Burned Over Time
acres_per_year = fire_data_cleaned.groupby('YEAR_')['GIS_ACRES'].sum()

# Line Chart
plt.figure(figsize=(10, 6))
acres_per_year.plot(kind='line', marker='o', color='darkorange')
plt.title('Total Acres Burned Per Year')
plt.xlabel('Year')
plt.ylabel('Total Acres Burned')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Save the chart
output_path = r'C:\Users\13176\Documents\Projects\LA_Fires_Analysis\outputs\plots\acres_burned_line_chart.png'
plt.savefig(output_path, dpi=300)
print(f"Chart saved to: {output_path}")

# Display the chart
plt.show()

# Fire Duration Histogram
plt.figure(figsize=(10, 6))
plt.hist(fire_data_cleaned['DURATION'], bins=30, color='teal', edgecolor='black', alpha=0.7)
plt.title('Distribution of Fire Durations')
plt.xlabel('Fire Duration (Days)')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Save the histogram
output_path = r'C:\Users\13176\Documents\Projects\LA_Fires_Analysis\outputs\plots\fire_duration_histogram.png'
plt.savefig(output_path, dpi=300)
print(f"Chart saved to: {output_path}")

# Display the histogram
plt.show()

import seaborn as sns

# Correlation Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(fire_data_cleaned[['DURATION', 'GIS_ACRES', 'Shape__Area', 'Shape__Length']].corr(), 
            annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap of Numerical Features')
plt.tight_layout()

# Save the heatmap
output_path = r'C:\Users\13176\Documents\Projects\LA_Fires_Analysis\outputs\plots\correlation_heatmap.png'
plt.savefig(output_path, dpi=300)
print(f"Chart saved to: {output_path}")

# Display the heatmap
plt.show()
    