# You can pass in a dictionary to pd.DataFrame(). Each key is a column name and each value is a list of column values. The columns must all be the same length or you will get an error.
# You run an online clothing store called Panda’s Wardrobe. You need a DataFrame containing information about your products.

import pandas as pd

# Creating a dataframe using a dictionary object
df1 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4],
  'Product Name': ['t-shirt', 't-shirt', 'skirt', 'skirt'],
  'Color': ['blue', 'green', 'red', 'black']
})

print(df1)

# Creating a dataframe using lists
df2 = pd.DataFrame([
  [1, 'San Diego', 100],
  [2, 'Los Angeles', 120],
  [3, 'San Francisco', 90],
  [4, 'Sacramento', 115]
],
  columns=['Store ID', 'Location', 'Number of Employees'
  ])

print(df2)

# Comma seperated variables or csvs take the following pattern:
'''
header1,header2,header3,header4,
row1val1,row1val2,row1val3,row1val4,
row2val1,row2val2,row2val3,row2val4
'''

# Loading a csv into a dataframe
pd.read_csv('csv-file.csv')

# Saving to a csv from a dataframe
df.to_csv('new_csv_file_name.csv')

# .head() and .info() are quick ways to view the dataframe
print(df.head())
print(df.info())

# Isolating a single column of information from a dataframe
df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)

clinic_north = df.clinic_north

print(type(clinic_north)) # pandas series type
print(type(df)) # pandas dataframe type

# Can also call multiple columns
clinic_north_south = df[['clinic_north', 'clinic_south']]

print(type(clinic_north_south)) # pandas dataframe type

# Can call rows using .iloc
march = df.iloc[2]

# Select multiple rows with slicing
april_may_june = df.iloc[3:]

print(april_may_june)

# Select conditional
january = df[df.month == 'January']

print(january)

# Select multiple conditional
march_april = df[(df.month == 'March') | (df.month == 'April')]

print(march_april)

# Select multiple conditions using .isin()
january_february_march = df[df.month.isin(['January', 'February', 'March'])]

print(january_february_march)

# Using reset_index() after calling a dataframe from a previous dataframe resulting in non-consecutive indices
df2 = df.loc[[1, 3, 5]]
print(df2)

df3 = df2.reset_index()
df2.reset_index(drop=True, inplace=True)

# Working with shoefly data
orders = pd.read_csv('shoefly.csv')

print(orders.head())

emails = orders.email

frances_palmer = orders[(orders.first_name == 'Frances') & (orders.last_name == 'Palmer')]

comfy_shoes = orders[orders['shoe_type'].isin(['clogs', 'boots', 'ballet flats'])]