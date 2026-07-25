'Day 10 (Questions 91–100)'


"""
'Q91. Create a list of student dictionaries containing Name, Age, and Marks, then display all records.'

lisn=['Ram','Siya','Diya','Dipak','Dipali','Riya']
lisa=[20,21,28,19,16,18]
lism=[80,70,90,60,80,75]
dictc={'Name':lisn,'Age':lisa,'Marks':lism}
print(dictc)

'Q92. Find the student with the highest marks from a list of dictionaries.'

lisn=['Ram','Siya','Diya','Dipak','Dipali','Riya']
lisa=[20,21,28,19,16,18]
lism=[80,70,90,60,80,75]
dictc={'Name':lisn,'Age':lisa,'Marks':lism}
high_mark=dictc['Marks'][0]
student_name=''
for i,j in zip(dictc['Name'],dictc['Marks']):
    if j > high_mark:
        high_mark = j
        student_name=i
print('The highest marks securer : ',student_name,high_mark)        
        

'Q93. Count how many times each word appears in a paragraph.'

paragraph='''Artificial Intelligence (AI) is the branch of computer science focused on creating systems capable of performing tasks that typically require human intelligence, such as reasoning, learning, decision-making, and problem-solving . These systems can process vast amounts of data, recognize patterns, and adapt their behavior over time without explicit programming.
AI encompasses multiple subfields, including machine learning (ML), deep learning, natural language processing (NLP), computer vision, and generative AI. While narrow AI (or weak AI) is designed for specific tasks like voice assistants or recommendation engines, artificial general intelligence (AGI)—machines with human-level cognitive abilities—remains theoretical .'''

lis=paragraph.split()
dic=dict()
for i in lis:
    dic[i] = lis.count(i)
print('Counted the each word : ',dic)    


'Q94. Merge two lists into a dictionary (one list for keys and one for values).'

lisn=['Ram','Siya','Diya','Dipak','Dipali','Riya']
lisa=[20,21,28,19,16,18]
dic=dict()
for i , j in zip(lisn,lisa):
    dic[i] = j
print('Merge two list into dictionary',dic)    

'Q95. Convert a list of tuples into a dictionary.'

lis=[('name','shubham'),('age',20),('Marks',80)]
dicts=dict()
for i in lis:
    j=i[0]
    k=i[1]
    dicts[j]=k
print('list of tuple is converted into dict : ',dicts)    

'Q96. Flatten a nested list into a single list.'

flat_list=[10,20,[30,40],40,50,[60,70],[80,90]]
sing_lis=[]

for i in flat_list:
    if isinstance(i,int):
        sing_lis.append(i)
    else:
        sing_lis.extend(i)
print(sing_lis)            


'Q97. Separate even and odd numbers from a list into two different lists.'

list1=[1,2,3,4,5,6,7,8,9]
even=[]
odd=[]
for i in list1:
    if i % 2 == 0:
        even.append(i)
    elif i % 2 != 0:
        odd.append(i)
print(f'Even list: {even}')        
print(f'Odd list: {odd}') 

'Q98. Find the common elements between two lists.'

list1=[1,2,3,4,5,6]
list2=[3,4,5,6,7,8]
common_list=[]
for i in list1:
    if i in list2 :
        common_list.append(i)
print('Common elements are',common_list)        

'Q99. Remove duplicate elements from a nested list while preserving the order.'

lis=[[1,2],[1,2],[3,4],[3,4],[5,6],[5,6]]
lis1=[]
for i in lis:
    if i not in lis1:
        lis1.append(i)
print('Removed duplicate from nested list : ',lis1)        


"""
'Q100. Build a menu-driven program that performs list operations (Insert, Delete, Search, Update, Display, Exit).'

lis=[]
print('Enter 1 for insert :')
print('Enter 2 for delete :')
print('Enter 3 for search :')
print('Enter 4 for update :')
print('Enter 5 for Display :')
print('Enter 6 for Exist :')
exist=False

while not exist:
  chose=int(input('Enter your choice : '))  
  if chose == 1:
    insert=input('Enter a value which is you want to insert : ')
    lis.append(insert)
    print('inserted succesfully')
  elif chose == 2:
    delete=input('Enter a value which is you want to delete : ')
    lis.remove(delete)
    print('deleted succesfully')
  elif chose ==3:    
    search = input('Enter a value which is you want to search')
    if search in lis:
       ind=lis.index(search)
       print('Your value at :',ind)
    else:
        print('Your value is not present in list')
  elif chose ==4: 
    update=input('Enter a value which is you want to update : ')
    if update in lis:
        new=input('Enter new value which is you want to replace with old value')
        inde=lis.index(update)
        lis[inde]=new
        print('Your value is updated succesfully')
    else:
        print('Your value is not present in list')    

  elif chose ==5: 
    print(lis)

  elif chose ==6:
    print('Existed succesfully')
    exist=True     