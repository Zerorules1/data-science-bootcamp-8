import pandas as pd
# create dataframe from scratch

raw_data = {
    "name": ["Petch", "Toy", "Mary", "John", "Anna"],
    "age": [29, 33, 20, 22, 31],
    "gender": ["M", "M", "F", "M", "F"]
}

df = pd.DataFrame(raw_data)
df["city"] = ['London', 'London', 'London', 'Manchester', 'Liverpool']

df = df.drop('city', axis = 1 )

# remove index = 2
df = df.drop(2, axis = 0)

# reset index
df = df.reset_index(drop = True)

# column names
df.shape
list(df.columns)

# rename columns
df.columns = ['nickname', 'age', 'sex']

type(df['nickname'])
type(df)

# create a new series
s1 = pd.Series(['Mary', 20,'F'], index=['nickname','age','sex'])
print(s1)
print(type(s1))

# append s1 to df
df = df.append(s1, ignore_index = True)

s2 = pd.Series(['London', 'London', 'London', 'Manchester', 'Liverpool'])
df['city'] = s2

# write csv file
df.to_csv('mydata.csv')

# import csv file
df2 = pd.read_csv('data/data.csv')

# import excel file
df3 = pd.read_excel('data/data.xlsx')

# import json
df4 = pd.read_json('data/data.json')
