import pandas as pd

# read pokemon_data csv file
#print('reading first 5 rows of .csv file')
#df = pd.read_csv('pokemon_data.csv')
# print(df.head(5))

# print()
# print('---------------------------------------------------------------')
#print('reading first 5 rows of excel file')
#df_xlsx = pd.read_excel('pokemon_data.xlsx')
# print(df_xlsx.head(5))

#df = pd.read_csv('pokemon_data.csv', delimiter='xxx')
# print(df_xlsx.head(5))

# Read Headers
df = pd.read_csv('pokemon_data.csv', engine='python')
print(df.columns)

# Read each column
# print(df['Name'])                 # print Pokemon name
# print(df['Name'][0:5])            # just the first 5 names, please
# print(df.Name)                    # prints the whole data set, alternative
# print(df[['Name', 'Type 1', 'HP']])    # enumerates columns

# Read each row
# print(df.head(4))       # print first 4 rows
# print(df.iloc[1])       # specific row

# use iterrows()
# for index, row in df.iterrows():
#    print(index, row)

# filter
# print(df.loc[df['Type 1'] == "Fire"])
# print(df.loc[df['Type 1'] == "Grass"])

# Read specific location (R, C)
# print(df.iloc[2, 1])     # second row, first column (Venosaur)

# sort_values()
#df = pd.read_csv('pokemon_data.csv', engine='python')
df_xlsx = pd.read_excel('pokemon_data.xlsx')
# print(df_xlsx.sort_values('Name'))  #sorts in ascending order by name (default is ascending)
# sorts in descending order
# print(df_xlsx.sort_values('Name', ascending=False))
# print("----------------------------------------------------------")
# print("sort ascending on one column, sort descending on another column")
# print(df_xlsx.sort_values(['Type 1', 'HP'], ascending=[1, 0]))
# print()
# print(df.head(5))
# print()
# print("`----------------------------------------------------------")
#print("total the columns")
df_xlsx['Total'] = df_xlsx['HP'] + df_xlsx['Attack'] + df_xlsx['Defense'] + \
    df_xlsx['Sp. Atk'] + df_xlsx['Sp. Def'] + df_xlsx['Speed']
# print(df_xlsx.head(5))
# print()
# print("----------------------------------------------------------")
#print("drop the total column")
df_xlsx = df_xlsx.drop(columns=['Total'])
print(df_xlsx.head(5))
print()
print("----------------------------------------------------------")
print("using list slicing:  drop the total")
df_xlsx['Total'] = df_xlsx.iloc[:, 4:10].sum(axis=1)
print(df_xlsx.head(5))
