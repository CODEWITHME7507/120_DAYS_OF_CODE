'Day 16 (Questions 151–160)'

"""

'Q151. Create a Student class with attributes name and age, then display the details.'

class student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
        print(name,age,marks)
s1=student('shubham',20,70)


'Q152. Create a Rectangle class with methods to calculate the area and perimeter.'

class Rectangle:
    def area_perimeter(self,length,height):
        area1=length * height
        perimeter1= (length + height)**2
        print('The area of rectangle is : ',area1)
        print('The perimeter of rectangel is : ',perimeter1)
r1=Rectangle()
r1.area_perimeter(20,30)        


'Q153. Create a BankAccount class with methods to deposit, withdraw, and check balance.'

class BankAccount12:
    def __init__(self,bank_balance,deposit,withdraw):
        self.deposit=deposit
        self.withdraw=withdraw
        self.__bank_balance=bank_balance
    def deposit_amount(self):
       self.__bank_balance+=self.deposit 
    def withdraw_amount(self):
        if self.__bank_balance >= self. withdraw:
           self.__bank_balance-=self.withdraw
        else:
            print('low balance')   
    def check_balance(self):
        print(self.__bank_balance)           
b1=BankAccount12(1000,2000,3000)
b1.deposit_amount()
b1.withdraw_amount()
b1.check_balance()


'Q154. Create a Car class with attributes brand, model, and year, then display the details.'

class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    def Car_details(self):
        print('Car Brand is : ',self.brand)
        print('Car model is : ',self.model)
        print('Car year is : ',self.year)
s1=Car('toyota',2,2023)        
s1.Car_details()


'Q155. Create a Circle class with methods to calculate the area and circumference.'
import math as ms
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area_circumference(self):
        self.area = ms.pi*self.radius**2
        self.circumference = 2 * ms.pi * self.radius
        print('Area of circle : ',self.area)
        print('circumference of circle : ',self.circumference)
s1 = Circle(5)
s1.area_circumference()             

'Q156. Create an Employee class and calculate the annual salary from the monthly salary.'

class Employee:
    def __init__(self,emp_name,monthly_salary):
        self.emp_name = emp_name
        self.monthly_salary = monthly_salary
    def annual_salary(self):
        self.annual_salary = self.monthly_salary * 12        
        print(f'The annual salary of {self.emp_name} is :',self.annual_salary)
s1=Employee('Ram',40000)
s1.annual_salary()        

'Q157. Create a Book class with attributes title, author, and price, then display the details.'

class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
    def display(self):
        print('book title is : ',self.title)    
        print('book author is : ',self.author) 
        print('book price is : ',self.price)
s1=Book('The billonare','Elon musk',2000)
s1.display()         

'Q158. Create a Calculator class with methods for addition, subtraction, multiplication, and division.'

class Calculator:
    def __init__(self,Num1,Num2):
        self.Num1=Num1
        self.Num2=Num2
    def addition(self):
        self.addition = self.Num1 + self.Num2
        print('Addition is :',self.addition)
    def multiplication(self):
        self.multiplication = self.Num1 * self.Num2
        print('multiplication is :',self.multiplication)
    def subtraction(self):
        self.subtraction = self.Num1 - self.Num2
        print('subtraction is :',self.subtraction)
    def division(self):
        self.division= self.Num1 / self.Num2
        print('division is :',self.division)
s1=Calculator(10,20)
s1.addition()
s1.multiplication()
s1.subtraction()
s1.division()        


'Q159. Create a Laptop class and create multiple objects to display different laptop details.'

class Laptop:
    def __init__(self,brand,model,ram,rom,batteryBackup,price,warranty):
        self.brand=brand
        self.model=model
        self.ram=ram
        self.rom=rom
        self.batteryBackup=batteryBackup
        self.price=price
        self.warranty=warranty
    def details(self):  
        print('The brand of laptop',self.brand)
        print('The model of laptop',self.model)
        print('The ram of laptop',self.ram)
        print('The rom of laptop',self.rom)
        print('The battery of laptop',self.batteryBackup)
        print('The price of laptop',self.price)
        print('The warranty of laptop',self.warranty)  
s1=Laptop('lenovo',2020,518,16,7000,15000,2)        
s1.details()

"""
'Q160. Create a Library class to add, search, and display books.'

class Library:
    def __init__(self,book_add,search):
        self.add=[]
        self.book_add=book_add
        self.search=search
    def add1(self):
        self.add.append(self.book_add)
    def search1(self):
        if self.search in self.add:
            print('This book is available')
    def display(self):
        for i in self.add:
            print(i)
s1=Library('build dont talk','build dont talk')            
s1.add1()
s1.search1()
s1.display()


