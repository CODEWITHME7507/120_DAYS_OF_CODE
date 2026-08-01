'Day 17 (Questions 161–170)'

"""

'Q161. Create a class that demonstrates the use of a constructor (__init__).'

class constructor:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def addition(self):
        return self.num1+self.num2
s1=constructor(20,30)
print(s1.addition())            

'Q162. Create a class with default constructor and parameterized constructor.'

class default_constructor:
    def __init__(self):
        self.name = 'Shubham'
        self.age = 21
    def display(self):
        print(self.name)
        print(self.age)
s1=default_constructor()
s1.display()

class parameterized_constructor:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name)
        print(self.age)
s1=parameterized_constructor('shubham',20)
s1.display()                       

'Q163. Demonstrate the use of the self keyword in a class.'

class demonstrates_self:
    def __init__(self,name):
        self.name = name #self is used to store value inside the object.
        print(self.name)
s1=demonstrates_self('shubham')



'Q164. Create a class with instance variables and instance methods.'

class constructor:
    def __init__(self,num1,num2):
        self.num1=num1 #instance variable
        self.num2=num2 #instance variable
    def addition(self): #instance method
        return self.num1+self.num2
s1=constructor(20,30)
print(s1.addition()) 

'Q165. Create a class with class variables and compare them with instance variables.'

class cls_variable_vs_intance_variable:
    name = 'shubham' #class variable
    def __init__(self,name1):
        self.name1 = name1 #instance variable
        print(self.name1) #we use only instance variable inside in any method
    print(name) # we cannot use class variable without self keyword inside method.  
s1=cls_variable_vs_intance_variable('Ram')
        


'Q166. Create a class that uses class methods (@classmethod).'

class classmethods:
    name='shubham'
    @classmethod
    def clsmethod(cls):
        print(cls.name)
s1=classmethods()
s1.clsmethod()        

'Q167. Create a class that uses static methods (@staticmethod).'

class staticmethods:
    name='shubham'
    @staticmethod
    def smethod():
         name='shubham'
         print(name)
s1=staticmethods()
s1.smethod()   

'Q168. Create a Student class to calculate the average marks of multiple subjects.'

class average_marks:
    def __init__(self,name,hindi,marathi,english,math):
        self.name=name
        self.hindi=hindi
        self.marathi=marathi
        self.english=english
        self.math=math
    def Avg_marks(self):
        self.Avg_marks= (self.marathi + self.hindi + self.english + self.math) / 4
        print(f'The average mark of {self.name} is :',self.Avg_marks)
s1=average_marks('shubham',10,20,30,40)
s1.Avg_marks()         

'Q169. Create a ShoppingCart class to add items and calculate the total bill.'

class ShoppingCart:
    def __init__(self):
        self.items={}
    def add_item(self,item,price):
        self.items[item]=price
    def total_bill(self):
        self.total_bill1 = sum(self.items.values())
        print('The items is :',self.items)
        print('The total bill is :',self.total_bill1)         
s1=ShoppingCart()
s1.add_item('laptop',20000)
s1.total_bill()
"""
'Q170. Create a Movie class and display the details of multiple movie objects.'

class movie:
    def __init__(self,movie_name,movie_type,movie_budget,movie_release,movie_lead_actor):
        self.movie_name = movie_name
        self.movie_type= movie_type
        self.movie_budget=movie_budget
        self.movie_release = movie_release
        self.movie_lead_actor = movie_lead_actor
    def movie_details(self):
        print('Movie Name :',self.movie_name) 
        print('Movie Type :',self.movie_type)
        print('Movie budget:',self.movie_budget)
        print('Movie release date :',self.movie_release)
        print('lead actor :',self.movie_lead_actor)   
s1=movie('pushpa','fightfull',5000,'10-02-2025','Allu arjun')
s1.movie_details()