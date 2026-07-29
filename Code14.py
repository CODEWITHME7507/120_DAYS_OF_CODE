'Day 14 (Questions 131–140)'

"""

'Q131. Handle a ZeroDivisionError using try-except.'

try:
   Val=11/0
except ZeroDivisionError:
    print('We can divide by zero')   

'Q132. Handle a ValueError when the user enters invalid input.'

try:
    ind=int(input('Enter a value: '))
except ValueError:
    print('You Enter wrong value')    

'Q133. Use multiple except blocks to handle different exceptions.'

try :
    ind=int(input('Enter a value: '))
except ZeroDivisionError:
    print('We cant divide any value by zero')
except ValueError:
    print('You entered wrong value')        

'Q134. Use a finally block to display a message after exception handling.'

try :
    lis=[1,2,3,4,5,6]
    d=lis[8]
except IndexError:
    print('You Entered wrong index') 
finally:
    print('Program execute succesfully')       


'Q135. Raise a custom exception using the raise keyword.'

class Invalidageerror(Exception):
    pass
age=0
if age <= 0:
    raise Invalidageerror('Enter valid age')
else:
    print('Your age is not able')    

'Q136. Create a program that handles a FileNotFoundError when opening a file.'
try:
    file=open('sham.txt','r')
except FileNotFoundError:
    print('This file not in your system')
finally:
    print('Executed')        

'Q137. Handle an IndexError when accessing list elements.'

lis=[10,20,30]
try :
    k=lis[2]
except IndexError:
    print('You enter wrong index')
else:
    print(k)        

'Q138. Handle a KeyError when accessing dictionary values.'

duc={1:'s',2:'b'}
try :
    k=duc[3]
except KeyError:
    print('You entered wrong key')    
finally:
    print('Program executed')

'Q139. Create a custom exception class and use it in a program.'

class NameError(Exception):
    pass
name='shubham'
name_in=input('Enter a name')
if name_in != name:
    raise NameError('The name not exist')
else:
    print('You are right')    
    
"""

'Q140. Build a menu-driven calculator that uses exception handling to prevent program crashes.'


try:
    Num1=int(input('Enter first number'))
    Num2=int(input('Enter second numbrer'))
    Num3= Num1 / Num2
    Num4= Num1 + Num2
except ZeroDivisionError:
    print('you cant divide num1 by zero')
except ValueError:
    print('You Entered wrong value')        


