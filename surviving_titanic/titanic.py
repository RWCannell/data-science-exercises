import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
titanic_df = pd.read_csv('csv/titanic.csv')

# Display the first 5 rows of the dataset
titanic_df_first_five_rows = titanic_df.head()
print(f"First 5 rows of the dataset:\n {titanic_df_first_five_rows}")

# Return the number of rows and columns in the dataset
rows, columns = titanic_df.shape
print(f"Number of rows: {rows}")
print(f"Number of columns: {columns}")

# Describe the statistics of the dataset
titanic_stats = titanic_df.describe()
print(f"\nTitanic Statistics:\n {titanic_stats}")

# Filter out columns with numeric data
titanic_df_columns = titanic_df.describe().columns
print(f"\nTitanic Numeric Columns:\n {titanic_df_columns}")

# Separate numerical and categorical values into different dataframes
df_numerical = titanic_df[['Age', 'SibSp', 'Parch', 'Fare']]
df_categorical = titanic_df[['Survived', 'Pclass', 'Sex', 'Ticket', 'Embarked']]

print(f"First 5 rows of numerical dataset:\n {df_numerical.head()}")
print(f"First 5 rows of categorical dataset:\n {df_categorical.head()}")

# # Look at histograms to find data that forms a normal distribution
# for i in df_numerical.columns:
#     plt.hist(df_numerical[i])
#     plt.title(i)
#     plt.show()

# # Look at barplots for categorical data
# for i in df_categorical.columns:
#     sns.barplot(df_categorical[i].value_counts()).set_title(i)
#     plt.show()

# Survival rate compared across Age, SibSp, Parch, and Fare
survived_pivot_table = pd.pivot_table(titanic_df, index='Survived', values=['Age', 'SibSp', 'Parch', 'Fare'])
print(f"Survived Pivot Table:\n {survived_pivot_table}")

# Pivot table for Survived and Pclass
survived_pclass_pivot_table = pd.pivot_table(titanic_df, index='Survived', columns='Pclass', values='Ticket', aggfunc='count')
print(f"Survived-Pclass Pivot Table:\n {survived_pclass_pivot_table}")

# Pivot table for Survived and Sex
survived_sex_pivot_table = pd.pivot_table(titanic_df, index='Survived', columns='Sex', values='Ticket', aggfunc='count')
print(f"Survived-Pclass Pivot Table:\n {survived_sex_pivot_table}")

# Pivot table for Survived and Embarked
survived_embarked_pivot_table = pd.pivot_table(titanic_df, index='Survived', columns='Embarked', values='Ticket', aggfunc='count')
print(f"Survived-Pclass Pivot Table:\n {survived_embarked_pivot_table}")