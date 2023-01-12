import pandas as pd

# read pokemon_data csv file
print('reading first 5 rows of .csv file')
df = pd.read_csv('pokemon_data.csv')
print(df.head(5))

print()
print('---------------------------------------------------------------')
print('reading first 5 rows of excel file')
df_xlsx = pd.read_excel('pokemon_data.xlsx')
print(df_xlsx.head(5))
