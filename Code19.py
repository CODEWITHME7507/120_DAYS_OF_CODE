'Day 19 (Questions 181–190)'



'Q181. Create a generator that prints numbers from 1 to N.'

def number_generator(N):
    for i in range(1,N+1):
        print(i)
number_generator(20)

'Q182. Create a generator to produce the Fibonacci sequence.'

def fibonacci_generator(N):
    num1 = 0
    num2 = 1
    for i in range(N):
        num3 = num1 + num2
        num2 = num1
        num1 = num3
        print(num2,end = ',')
fibonacci_generator(10)        

'Q183. Create a custom iterator that prints even numbers up to N.'

def custom_iterator_Even(N):
    for i in range(N):
        if i % 2 == 0:
            print(i)
custom_iterator_Even(10)            

'Q184. Use the enumerate() function to display the index and value of a list.'

def use_enum(lis):
    for index,value in enumerate(lis):
        print(index,value)
use_enum([10,20,30,40])        

'Q185. Use the zip() function to combine two lists into pairs.'

def use_zip(lis1,lis2):
    if len(lis1) == len(lis2):
        for i,j in zip(lis1,lis2):
            print(i ,':', j)
    else:
        print('This lists are not zipable')        
use_zip([10,20,30,40],[50,60,70,80])            

     

'Q186. Unzip a list of tuples into two separate lists.'

def unzip_list(lis):
    for i in lis:
        lis1= [i]
        print(lis1)
unzip_list([(10,20,30,40),(50,60,70,80),(90,100,120,130)])        

'Q187. Create a decorator that prints a message before and after executing a function.'

def decorator(func):
    def wrapper():
        print('start')
        func()
        print('End')
    return wrapper
@decorator
def hello():
    print('Hello')

hello()    
'Q188. Create a decorator to calculate the execution time of a function.'

import time as tm
def timer(cal_time):
    def wrapper():
        start = tm.time()
        cal_time()
        end = tm.time()
        print(f"The execution time is : {end - start :.6f} seconds")
    return wrapper
@timer
def display():
    for i in range(100000):
        pass
display()    

'Q189. Use the *args parameter to create a function that accepts any number of arguments and returns their sum.'

def vla(*lis):
    print('The sum of : ',sum(lis))
vla(10,20,30,40)    

'Q190. Use the **kwargs parameter to create a function that accepts any number of keyword arguments and displays them.'

def vlka(**lis):
    for key , value in lis.items():
        print(key , ':' , value)

vlka(name = 'shubham', age = 19 , std = 10)    