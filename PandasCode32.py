'''day32'''

import pandas as pd

df = pd.read_csv(r"C:\Users\mayur lagad\Downloads\pandas_day31_day45_messy_customers.csv")


'''Q11. Select Specific Columns
Display only:
customer_id
name
city
order_amount'''

columns = df[['customer_id','name','city','order_amount']]
print(columns)


'''Q12. Select Columns Using a List
Create a new DataFrame containing only:
name, age, gender, email.'''


New_df = pd.DataFrame(df[['name','age','gender','email']])
print(New_df)


'''Q13. Select One Column
Display the age column and check its Pandas data type.'''

pdtype = df['age']
print(pdtype.dtype)


'''Q14. Select the First 20 Rows
Display the first 20 records using .iloc[].'''

df_first_20 = df.iloc[0:20]
print(df_first_20)


'''Q15. Select Specific Rows and Columns
Using .iloc[], display rows 10 to 20 and only the columns name, city, and age.'''

column_rows = df.iloc[11:21,[1,3,6]]
print(column_rows)


'''Q16. Select Data Using .loc[]
Using .loc[], display the name, email, and city columns for the first 15 records.'''

loc_15 = df.loc[0:15,['name','email','city']]
print(loc_15)



'''Q17. Filter Customers by Age
Find all customers whose age is greater than 30.'''

gre_30 = df[df['age']>30]
print(gre_30)

'''Q18. Filter Customers by City
Find all customers whose city is Mumbai.
Notice that some city values are intentionally messy, such as "mumbai " and " PUNE". Do not clean them yet.'''

city_mum = df[df['city']=="Mumbai"]
print(city_mum)


'''Q19. Multiple Conditions
Find customers who:
are older than 30
AND have an order amount greater than 2,000.'''

#'>' not supported between instances of 'str' and 'int'
df['age'] = pd.to_numeric(df['age'],errors='coerce')
df['order_amount'] = pd.to_numeric(df['order_amount'],errors='coerce')
mul_con = df[(df['age'] > 30) & (df['order_amount'] > 2000)]
print(mul_con[['name','age','order_amount']])


'''Q20. Create a Filtered DataFrame Create a new DataFrame containing customers whose:
age is between 25 and 40
city is Pune
customer status is Active'''
fil_mul_df = df[(df['age'].between(25,40)) & (df['city'] == 'Pune') & (df['customer_status']=='active')]
new1_df = pd.DataFrame(fil_mul_df)
print(new1_df) 