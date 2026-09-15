'''Day 33 — Pandas Data Manipulation
Use the same pandas_day31_day45_messy_customers.csv dataset.'''

import pandas as pd
import numpy as np
df = pd.read_csv(r"C:\Users\mayur lagad\Downloads\pandas_day31_day45_messy_customers.csv")

'''Q21. Create a New Column
Create a new column called order_amount_double that contains 2 × order_amount.'''

df['order_amount'] = df['order_amount'].str.replace("₹","",regex = False)
df['order_amount'] = pd.to_numeric(df['order_amount'],errors='coerce')
df['order_amount'] = df['order_amount'].fillna(0)
df['order_amount_double'] = df['order_amount']*2


'''Q22. Create a Customer Category
Create a new column called age_group:
Age < 25 → "Young"
Age 25–40 → "Adult"
Age > 40 → "Senior"'''

df['age_group'] = np.select(
    [
        df['age'] < 25,
        (df['age'] > 25) & (df['age']<40),
        df['age'] > 40 
    ],
    [
        "Young",
        "Adult",
        "Senior"
    ],default=''
)



'''Q23. Rename Columns
Rename:
customer_id → Customer_ID
order_amount → Order_Amount
customer_status → Status'''

df.rename(columns={'customer_id':'Customer_ID','order_amount':'Order_Amount','customer_status':'Status'},inplace= True)


'''Q24. Delete a Column
Delete the age_group column created in Q22.'''

del df['age_group']


'''Q25. Change Values in a Column
In the customer_status column, replace:
"active" → "Active"
"INACTIVE" → "Inactive"
"Active " → "Active"'''

df['Status']=df['Status'].str.strip().str.title()

'''Q26. Replace Specific Values
In the gender column, replace:
"male" → "Male"
"female" → "Female"
" M" → "Male"
" F" → "Female"'''

df['gender']= df['gender'].str.strip()
maps = {"male":"Male","female":"Female","M":"Male","F":"Female"}
df['gender'] = df['gender'].replace(maps)




'''Q27. Create a High-Value Customer Column
Create customer_type based on order_amount:
>= 3000 → "High Value"
< 3000 → "Regular"'''

df['Customer_type'] = np.select(
    [
        df['Order_Amount'] >= 3000,
        df['Order_Amount'] < 3000
    ],
    [
        "High Value",
        "Regular"
    ],default=''
)



'''Q28. Delete Rows Based on Condition
Remove all rows where age is less than 18.'''

df = df[df['age'] >= 18]


'''Q29. Update Values Using a Condition
For customers whose order_amount is greater than 4000, change their customer_status to "Premium".'''

df.loc[df['Order_Amount'] > 4000,'Status'] = "Premium"
print(df["Status"].unique())

'''Q30. Create a Clean Subset Create a new DataFrame containing only customers where:
age > 30
order_amount > 2000
customer_status == "Active"'''

new2_df = pd.DataFrame(df[(df['age']>30) & (df['Order_Amount'] > 2000) & (df['Status'] == "Active")])
print(new2_df)