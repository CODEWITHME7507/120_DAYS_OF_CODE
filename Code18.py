'Day 18 (Questions 171–180)'

"""

'Q171. Create a single inheritance program using Person and Student classes.'

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class Student(Person):
    def student_info(self,std,marks):
        self.std = std
        self.marks = marks
        print('Student Name is: ',self.name)
        print('Student age is: ',self.age)
        print('Student class is: ',self.std)
        print('Student marks is: ',self.marks)
s1=Student('shubham',30)
s1.student_info(10,80)             

'Q172. Create a multilevel inheritance program using Person, Employee, and Manager classes.'

class Person:
    def __init__(self,Name,Age,City):
        self.Name = Name
        self.Age = Age
        self.City = City
class Employee(Person):
    def employee_info(self,Empid,department,salary):
        self.Empid=Empid
        self.department=department
        self.salary = salary
class Manager(Employee):
    def display_manager_info(self):
        print('Manger Name is : ',self.Name)
        print('Manager id is : ',self.Empid)
        print('Manager City is : ',self.City)
        print('Manager Department is : ',self.department)
        print('Manager Age is : ',self.Age)
        print('Manager Salary is : ',self.salary)
s3=Manager('Shubham',40,'delhi')
s3.employee_info(1,'IT',200000)
s3.display_manager_info()        
        


'Q173. Create a hierarchical inheritance program using a Shape class with Circle and Rectangle subclasses.'

class Shape:
    def __init__(self,name,color):
        self.name=name
        self.color=color
class Rectangle(Shape):
    def Rectangle_info(self,length,width):
        self.length = length
        self.width = width 
    def rectangle_display(self):
        self.result = self.length * self.width
        print('The name of shape is : ',self.name)            
        print('The color of shape is : ',self.color)
        print('The area of Rectange is :',self.result)
class Circle(Shape):
    def Circle_info(self,radius):
        self.radius= radius
    def circle_display(self):
        self.result = 3.14 * self.radius * self.radius
        print('The name of shape is : ',self.name)
        print('The color of shape is :',self.color)            
        print('The area of shape is :',self.result)

s1=Rectangle('Rectangle','Red')
s1.Rectangle_info(20,30)
s1.rectangle_display()


s2=Circle('Circle','Green')
s2.Circle_info(7)
s2.circle_display()



'Q174. Demonstrate method overriding in inheritance.'

class book1:
    def book_info(self):
        self.book_n_pages=1900
        self.book_price = 1000
class book2(book1):
    def book_info(self):
       super().book_info() 
       print('The book number of pages is : ',self.book_n_pages)
       print('The book Price is :',self.book_price)

s2=book2()
s2.book_info()

'Q175. Use the super() function to call the parent class constructor.'

class parent:
    def Parent_info(self):
        self.name = 'shivaji'
        self.age = 100
class child(parent):
    def child_info(self):
       super().Parent_info() 
       print('The Name is : ',self.name)
       print('The Age is :',self.age)
s1=child()
s1.child_info()

'Q176. Create a program demonstrating multiple inheritance.'

class school:
    def __init__(self,school_name):
        self.school_name =  school_name
class std:
    def __init__(self,class_number):
        self.class_number=class_number
class student(school,std):
    def __init__(self,school_name,class_number,stud_name):
        school.__init__(self,school_name)
        std.__init__(self,class_number)
        self.stud_name = stud_name
    def display(self):
        print('The Name of school is : ',self.school_name)
        print('The class number is : ',self.class_number)
        print('The name of student is : ',self.stud_name)
s3=student('vnm',10,'shubham')
s3.display()

'Q177. Create a class that demonstrates encapsulation using private attributes.'

class Bank:
    def __init__(self,Name,bank,Account_number):
        self.Name = Name
        self.bank = bank
        self.__Account_number = Account_number #Encapsulation Private Attributes
    def display_info(self):
        print('The account holder name is : ',self.Name)
        print('The Bank Name is : ', self.bank)
        print('The Account Number is : ', self.__Account_number) # here we print account number using encapsulation method
s1=Bank('shubham','IBPS',12345678)
s1.Name='Ram'
s1.display_info()           

'Q178. Create a class with getter and setter methods.'

class getter_setter:
    def __init__(self,Name,Age,Bank_name,Bank_pin,Bank_account_number):
        self.Name = Name
        self.Age = Age
        self.Bank_name = Bank_name
        self.__Bank_pin = Bank_pin
        self.__Bank_account_number = Bank_account_number
    def set_pin(self,old_pin,New_pin):
        self.old_pin = old_pin
        self.New_pin = New_pin
        if self.old_pin == self.__Bank_pin:
            self.__Bank_pin = self.New_pin
            print('The Pin change successfully')
        else:
            print('Old pin is not Matched')    
    def get_ac_pin(self):
        print('The account number is : ',self.__Bank_account_number)
        print('The pin is : ',self.__Bank_pin)
    def display_info(self):
        print('The name of account holder is : ',self.Name)
        print('The Age of account holder is : ',self.Age)
        print('The name of bank is : ',self.Bank_name)
s1=getter_setter('shubham',20,'IBPS',766692,123456789) 
s1.set_pin(766692,9421900)
s1.get_ac_pin()           
s1.display_info()

'Q179. Create an abstract class using the abc module and implement it in child classes.'

from abc import ABC , abstractmethod

class school(ABC):
    @abstractmethod
    def student(self):
        pass
class classs(school):
    def student(self): #HERE WE USE ABSTRACT CLASS METHOD WITHOUT THIS METHOD WE CANNOT ABSTRACT CLASS
        self.name = 'Shubham'    
        self.std = 10
        self.roll = 23
        print('The name of student is : ',self.name)
        print('The class of student is : ',self.std)
        print('The roll of student is : ',self.roll)
s1=classs()
s1.student()        
"""
'Q180. Create a Bank Account System using inheritance and method overriding.'

class Bank:
    def bank_info(self,bank_name,bank_Branch,bank_level):
        self.bank_name = bank_name
        self.bank_Branch = bank_Branch
        self.bank_level = bank_level
class person(Bank):
    def bank_info(self,Bank_ac_holder,holder_age,ac_number,holder_gender):
        super().bank_info('IBPS','delhi branch','National level')
        self.Bank_ac_holder = Bank_ac_holder
        self.holder_age = holder_age
        self.__ac_number = ac_number
        self.holder_gender = holder_gender
    def display_info(self):    
        print('The Name of bank is : ',self.bank_name)   
        print('The branch of bank is : ',self.bank_Branch ) 
        print('The level of bank  is : ',self.bank_level) 
        print('The Name of bank account holder is : ', self.Bank_ac_holder) 
        print('The Age of holder is : ',self.holder_age) 
        print('The ac_number is : ',self.__ac_number) 
        print('The holder gender is : ',self.holder_gender) 
        
s2=person()
s2.bank_info('shubham',20,12345678,'male')        
s2.display_info()
