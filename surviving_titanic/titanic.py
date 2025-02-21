import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
titanic_data = pd.read_csv('csv/titanic.csv')

# Display the first 5 rows of the dataset
titanic_data_first_five_rows = titanic_data.head()
print(f"First 5 rows of the dataset:\n {titanic_data_first_five_rows}")

# Return the number of rows and columns in the dataset
rows, columns = titanic_data.shape
print(f"\nNumber of rows: {rows}")
print(f"Number of columns: {columns}")

# Describe the statistics of the dataset
titanic_stats = titanic_data.describe()
print(f"\nTitanic Statistics:\n {titanic_stats}")

# Filter out columns with numeric data
titanic_data_columns = titanic_data.describe().columns
print(f"\nTitanic Data Columns:\n {titanic_data_columns}")
