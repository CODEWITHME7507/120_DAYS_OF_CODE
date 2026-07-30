'Day 15 (Questions 141–150)'



'Q141. Create a text file and write data into it.'

with open('Student.txt','w') as file:
    file.write('Hi My Name is Shubham')   

'Q142. Read and display the contents of a text file.'

with open('Student.txt','r') as file:
    read = file.read()
    print(read)

'Q143. Append new data to an existing text file.'

with open('Student.txt','a') as file:
    file.write('I am from chhatrapati sambhajinagar')

'Q144. Count the number of lines, words, and characters in a text file.'

dic={'lines':0,'word':0,'char':0}
with open('Student.txt','r') as file:
   read=file.readlines()
   
   for line in range(len(read)):
     dic['lines']+=1
     for word in read[line].split():
        dic['word']+=1
        for char in word:
            dic['char']+=1
   
print('The total lines,word,character in file: ',dic)   
    


'Q145. Copy the contents of one file to another.'

with open('Student.txt','r') as file:
    content=file.read()
with open('New student.txt','w') as newfile:
    newfile.write(content)


'Q146. Search for a specific word in a text file and display the number of occurrences.'

word=str(input('Enter a which is want to search : '))
dic={word:0}
with open('New student.txt','r') as newfile:
   read = newfile.readlines()
   for lines in read:
    for words in lines.split():
        if word == words:
            dic[word]+=1
print(dic)            


'Q147. Read a text file and display only the unique words.'

unique = []
with open('Student.txt','r') as file:
    content=file.readlines()
    for lines in content:
        for word in lines.split():
            if word in unique:
                unique.remove(word)
            else:
                unique.append(word)
print(unique)                    

'Q148. Create a program that merges two text files into a third file.'

with open('Student.txt','r') as file:
    content1=file.read()
with open('New student.txt','r') as newfile:    
    content2=newfile.read()
with open('combination.txt','w') as merge:
    merge.write(content1+content2)
with open('combination.txt','r') as merge:
    read=merge.read()
    print(read)

'Q149. Read a CSV file and display all records using Python.'

with open(r"C:\Users\mayur lagad\Downloads\iiii.csv","r") as file:
    read = file.read()
print(read)    


'Q150. Build a simple Student Record Management System using file handling (Add, View, Search, Update, Delete).'

def student_record_management():
  while True:  
    print('Enter 1 for add Student')
    print('Enter 2 for view student')
    print('Enter 3 for search student')
    print('Enter 4 for Update student information')
    print('Enter 5 for Delete student information')
    print('Enter 6 for exist')
    Enter = int(input('Enter Your choice : '))
    def ID_checker(Id):
        with open('student1.txt','r') as stufile:
            read = stufile.readlines()
            for line in read:
                ids=line.split()
                if Id == ids[0]:
                    return True
            return False        


    if Enter == 1:
        Id=str(input('Enter student Id : '))
        Name=str(input('Enter student Name : '))
        Std = str(input('Enter student class number : '))
        Age = str(input('Enter student age : '))
        if not ID_checker(Id):
          studentinfo = Id+' '+Name+' '+Std+' '+Age+'\n'
          with open('student1.txt','a') as stufile:
            stufile.write(studentinfo)
          print('Student Added Successfully')
        else:
            print('ID already exist')  
    elif Enter == 2:
        with open('student1.txt','r') as stufile:
            read = stufile.readlines()
            for line in read:
                print(line) 
    elif Enter == 3:
       Id=str(input('Enter student Id : ')) 
       if ID_checker(Id):
         with open('student1.txt','r') as stufile:
            read = stufile.readlines()
            for line in read:
                ids=line.split()
                if Id == ids[0]:
                    print(ids)
       else:
        print('No result found')             
    elif Enter == 4:
        Id = str(input('Enter student Id : '))                
        if ID_checker(Id):
            with open('student1.txt','r') as file:
              read = file.readlines()
              for line in range(len(read)):
                ids = read[line].split()
                if Id == ids[0]:
                   Id=str(input('Enter student Id : '))
                   Name=str(input('Enter student Name : '))
                   Std = str(input('Enter student class number : '))
                   Age = str(input('Enter student age : '))  
                   if ID_checker(Id):
                      studentinfo = Id+' '+Name+' '+Std+' '+Age 
                      read[line]=studentinfo
                      with open('student1.txt','w') as stufile:
                           stufile.writelines(read)
                           print('Student updated Successfully')  
                   else:
                     print('Id already exist')        
    elif Enter == 5:
        Id= str(input('Enter student id : '))
        if ID_checker(Id):
          with open('student1.txt','r') as file:
              read = file.readlines()
              for line in range(len(read)):
                ids = read[line].split()
                if Id == ids[0]:
                   if ID_checker(Id): 
                      read[line]=''
                      with open('student1.txt','w') as stufile:
                           stufile.writelines(read)
                           print('Student deleted Successfully')  
         
                else:
                    print('Student ID not exist')
    elif Enter == 5:
        exit()             
student_record_management()         