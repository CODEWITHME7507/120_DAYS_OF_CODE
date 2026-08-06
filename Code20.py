'Day 20 (Questions 191–200)'



'Q191. Read data from a JSON file and display its contents.'

import json as js
"""
student={'name':'shubham','age':21,'class':10,'marks':80}

with open('Studen.json','w') as file:
    js.dump(student,file,indent = 5)
print('Created successfully')   
with open ('Studen.json','r') as file:
    data=js.load(file)
for i,j in data.items():
    print(i,j)    

'Q192. Write a Python dictionary to a JSON file.'

import json as js
dic = {'Emp_id':1,'Emp_name':'dipak','salary':12000,'Department':'IT'}

with open('studen.json','a') as file:
    js.dump(dic,file,indent = 5)
print('Data added sucessfully')    
        


'Q193. Read data from a CSV file and calculate the average of a numeric column.'

import json as js
import csv as cs
data=[]
avg_count = 0
total_sal= 0
with open('emp.csv','r') as file:
    reader=cs.DictReader(file)
    for row in reader:
       data.append(row)
with open('emp.json','w') as js_file:
    js.dump(data,js_file,indent = 4)
with open('emp.json','r') as jsn_file:
    num_column=js.load(jsn_file)
    for i in num_column:
       total_sal += int(i['Salary'])
       avg_count += 1
print('The average salary of employees is :',total_sal/avg_count)       

"""
'Q194. Write data to a CSV file using Python.'

import csv as cs
import json as js
data = [['name','age','Marks'],
        ['shubham',10,80]]
with open('new.csv','w') as file:
    writes = cs.writer(file)
    for i in data:
         writes.writerow(i)
print('okk done')         




'Q195. Create a program that logs errors to a file using the logging module.'



'Q196. Create a student report card by reading marks from a CSV file and calculating the total, average, percentage, and grade.'



'Q197. Create a program that backs up a text file by copying it to another location with the current date in the filename.'



'Q198. Build a contact management system that stores and retrieves contact details using JSON.'



'Q199. Build a to-do list application that saves tasks in a JSON file.'



'Q200. Create a mini employee management system using CSV files with options to Add, View, Search, Update, and Delete employee records.'


