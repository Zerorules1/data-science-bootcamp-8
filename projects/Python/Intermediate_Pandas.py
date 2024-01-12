# Intermediate Pandas


import pandas as pd

penguins = pd.read_csv('penguins.csv')

# preview first 5 rows
penguins.head() # nan = missing value

penguins.tail()

# shape of dataframe
penguins.shape

# information of dataframe
penguins.info()

# select columns
penguins['species'] 
penguins.species # same result

# select columns
penguins[['species','island','sex']].head()

# select columns
penguins[['species','island','sex']].tail(8)

# integer location based indexing (iloc)
mini_penguins = penguins.iloc[0:5,[0,2,5]]

# filter rows by a codition
penguins[penguins['island'] == 'Torgersen']

penguins[penguins['bill_length_mm'] > 34]

# filter more than one condition
filtered_penguins = penguins[(penguins['island'] == 'Torgersen') & (penguins['bill_length_mm'] < 35)]
filtered_penguins = penguins[(penguins['island'] == 'Torgersen') | (penguins['bill_length_mm'] < 35)]

# filter with .query()
penguins.query('island == "Torgersen"') # "island == 'Torgersen'"
penguins.query('island == "Torgersen" & bill_length_mm < 35')

# check missing in each column
penguins.isna().sum()

# filter missing value in column sex
penguins[penguins['sex'].isna()]

# drop na
clean_penguins = penguins.dropna()
clean_penguins.head(10)

# fill missing values
top5_penguins = penguins.head(5)

avg_value = top5_penguins['bill_length_mm'].mean()

print(avg_value)

top5_penguins = top5_penguins['bill_length_mm'].fillna(value=avg_value)
top5_penguins

# sort bill_length_mm low to high, high to low
penguins.dropna().sort_values('bill_length_mm', ascending= False).head(10)

# sort multiple columns
penguins.dropna().sort_values(['island','bill_length_mm'])

# unique values
penguins['species'].unique()

# count values
penguins['species'].value_counts()

# count more than one columns
result = penguins[['island','species']].value_counts().reset_index()
result.columns = ['island', ' species', 'count']

result

# summarize dataframe
penguins.describe(include='all')

# average, mean
penguins['bill_length_mm'].std()

# group by + sum/ mean
# penguins[penguins['species'] == 'Adelie']['bill_length_mm'].mean()
penguins.groupby('species')['bill_length_mm'].median()

# aggregate function
penguins.groupby('species')['bill_length_mm'].agg(['min','mean','median', 'std', 'max'])

# if your code is long use \
result = penguins.groupby(['island', 'species'])['bill_length_mm']\
    .agg(['min','mean','max'])\
    .reset_index()

# map values MALE: m, FEMALE: f
# penguins['sex'].head()
penguins['sex_new'] = penguins['sex'].map({'MALE': 'm', 'FEMALE': 'f'}).head(10).fillna('other')
penguins.head()

# pandas style
penguins['bill_length_mm'].mean()

# numpy
import numpy as np
np.mean(penguins['bill_length_mm'])

# other function of numpy
print(np.sum(penguins['bill_depth_mm']))
print(np.std(penguins['body_mass_g']))

# where
score = pd.Series([80, 50 ,62, 95, 20])

grade = np.where(score >= 80, "passed", "failed")
print(grade)

df = penguins.query("species == 'Adelie'")[['species', 'island', 'bill_length_mm']].dropna()

df.head()
df['new_column'] = np.where(df['bill_length_mm'] > 40, True, False) #boolean

df.head(

)

# Merge DataFrame
left = {
    'key': [1,2,3,4],
    'name': ['Petch','Toy','Joe','Mary'],
    'age': [29,33,24,23]
}

right = {
    'key': [1,2,3,4],
    'city': ['Bangkok', 'London', 'Seoul', 'Tokyo'],
    'zip': [1001,2504,2094,9802]
}

df_left = pd.DataFrame(left)
df_right = pd.DataFrame(right)

df_left

df_result = pd.merge(df_left,df_right, on='key')
df_result

# histogram one column
penguins['body_mass_g'].plot(kind='hist');

# histogram two columns
penguins[['body_mass_g','bill_length_mm']].plot(kind='hist', bins= 30);

# defined bins and color
penguins[['body_mass_g']].plot(kind='hist', bins= 30, color="orange");

# bar plot for species
penguins['species'].value_counts().plot(kind='bar', color=['salmon','orange','gold'])

# scatter plot
penguins[['bill_length_mm','bill_depth_mm']].\
    plot(x='bill_length_mm', y = 'bill_depth_mm', kind="scatter", color='orange')

# datalore
penguins
