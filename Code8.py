'''Day 8 (Questions 71-80)'''


'Q71. Create a dictionary to store student names and marks.'

dict1={'Name':['Shubham','Mayur','Vaibhav','Krushna'],
        'Marks':[66,77,54,77]}
print(dict1.items())        

'Q72. Access the value of a specific key in a dictionary.'

dict1={'Name':'Shubham','Marks':66,'Age':12,'ID':3}
print(dict1.keys())
key1=str(input('Enter key between these all'))
print(dict1[key1])

'Q73. Add a new key-value pair to a dictionary.'

key1=str(input('Enter key any you want: '))
value=str(input('Enter value which you needed:'))

dict1=dict()
dict1[key1] = value

print('key value pair added succesfully : ',dict1)

'Q74. Update the value of an existing key.'

dict1={'Name':'Shubham','Marks':66,'Age':12,'ID':3}
update_value=int(input('Enter value which is you want : '))

dict1['ID']=update_value

print('Id succesfully updated of student',dict1)

'Q75. Delete a key-value pair from a dictionary.'

dict1={'Name':'Shubham','Marks':66,'Age':12,'ID':3}
print(dict1.keys())
delete = str(input('Enter any of these key which is you want to delete'))
dict1.pop(delete)
print('key value deleted succesfully',dict1)

'Q76. Count the frequency of each character in a string using a dictionary.'

keys='ShubhamPhuke'
dict1=dict()
dict1[keys]=len(keys)
print('The frequency of string is :',dict1)

'Q77. Count the frequency of each word in a sentence using a dictionary.'

sentance='THE QUICK BROWN FOX OVER THE LAZY THE DOG'
lis=sentance.split()
dict1={}
for i in lis:
    dict1[i]=len(i)
print('Frequency of each word in sentance : ',dict1)    

'Q78. Find the key with the maximum value in a dictionary.'

dict1={'value1':50,'value2':60,'value3':90,'value4':40}
maxx=dict1['value1']
for i in dict1.values():
    if i > maxx:
        maxx=i
for i in dict1.keys():
    if dict1[i]==maxx:
        print('This is maximum value key : ',i)        


'Q79. Merge two dictionaries into one.'

dict1={'value1':50,'value2':60,'value3':90,'value4':40}
dict2={'Name':'Shubham','Marks':66,'Age':12,'ID':3}

dict1.update(dict2)
print('Merged dictionaries :',dict1)

'Q80. Sort a dictionary by its values in ascending order.'


dict1={'value1':50,'value2':60,'value3':90,'value4':40}
sorted_dict=dict(sorted(dict1.items(),key=lambda value:value[1]))
print(sorted_dict)
