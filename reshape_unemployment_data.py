# We intend to reshape the unemployment data into long format before using python or tableau to create dataviz
# Imports
import pandas as pd

df = pd.read_csv(r"Data/unemployment_analysis.csv")

print(df)

# Reshaping data in Long Format

melted_df = pd.melt(df, id_vars=['Country Name', 'Country Code'], var_name='Year', value_name='Unemployment Rate')

print(melted_df)

# Creating a file for reshaped data to be used for Visualizations
melted_df.to_csv(r"Data/reshaped_unemployment_data.csv", index=False)