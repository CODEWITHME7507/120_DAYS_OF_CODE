'''Day 31 — Pandas Basics'''

'''Use the pandas_day31_day45_messy_customers.csv dataset.'''

# imported pandas
import pandas as pd

'''Q1. Load the Dataset
Read the CSV file using Pandas and store it in a DataFrame called df.'''

#loading the dataset
df = pd.read_csv(r"C:\Users\mayur lagad\Downloads\pandas_day31_day45_messy_customers.csv")


'''Q2. Display the First 10 Records
Display the first 10 rows of the DataFrame.'''

# Head is used for getting first rows from dataset
first_rows = df.head(10)
print("first 10 rows",first_rows)


'''Q3. Display the Last 10 Records
Display the last 10 rows of the DataFrame.'''

# Tail is used for getting last rows from dataset
last_rows = df.tail(10)
print("last 10 rows",last_rows)


'''Q4. Find Number of Rows and Columns
Find how many rows and columns are present in the dataset.'''

# shape told us how much rows and columns in dataset
rows_and_columns = df.shape
print("Number of rows in dataset:",rows_and_columns[0])
print("Number of Columns in dataset:",rows_and_columns[1])

'''Q5. Display Column Names
Display all column names present in the DataFrame.'''

# columns for getting columns name
columns_names = df.columns
print("Name of columns",columns_names)



'''Q6. Check Data Types
Display the data type of every column.'''

# astype for getting columns datatype
data_types_of_columns = df.dtypes
print("The datatype of columns",data_types_of_columns)

'''Q7. Get Basic Dataset Information
Use Pandas to display information about:
Column names
Non-null values
Data types
Memory usage'''

# info() for getting information of this
information = df.info()
print("Information",information)

'''Q8. Generate Statistical Summary
Generate a statistical summary of the numerical columns.'''

# describe() for Generate statistical summary of the numerical columns
statistical_summ_num_Col = df.describe()
print("Generated summary is ",statistical_summ_num_Col)


'''Q9. Check Missing Values
Find the number of missing values in each column.'''

# isnull() and sum() for finding missing values
missing_values = df.isnull().sum()
print("Missing values are",missing_values)


'''Q10. Find Duplicate Records
Check whether the dataset contains duplicate rows and find the total number of duplicate records.'''

# duplicated and sum() for count duplicate record
duplicatess = df.duplicated().sum()
print("duplicates",duplicatess)