'Day 12 (Questions 111–120)'



'Q111. Find the factorial of a number using recursion.'

def factorial(value):
    if value == 1:
        return value
    return value * factorial(value - 1)
print('This is a factorial: ',factorial(5))        

'Q112. Find the Nth Fibonacci number using recursion.'

def fibonacci(value):
    if value <= 1:
        return value
    return fibonacci(value-1) + fibonacci(value-2)
value=int(input('Enter a value: '))
print(fibonacci(value))

'Q113. Find the sum of the first N natural numbers using recursion.'

def first_number_sum(value):
    if value == 0:
        return value
    return value + first_number_sum(value - 1)
value=int(input('Enter a value: '))    
print('This is first natural number sum:',first_number_sum(10))        

'Q114. Calculate the power of a number (a^b) using recursion.'

def power_of_number(value,power):
    if power == 1:
        return value
    return value * power_of_number(value,power-1)    
value=int(input('Enter a value: '))    
print('The power of number : ',power_of_number(value,3))

'Q115. Reverse a string using recursion.'

def reverse_string(string):
    if string == '':
        return string
    return reverse_string(string[1:]) + string[0]
string=str(input('Enter a string: '))
print('The reverse string is : ',reverse_string(string))     



'Q116. Check whether a string is a palindrome using recursion.'

def palindrome_string(string):
    if len(string) <= 1 :
        return True
    if string[0] != string[-1]:
        return False
    return palindrome_string(string[1:-1])     
string=str(input('Enter a string: '))  
if palindrome_string(string):
    print('This is palindrome string')
else:
    print('This is not palindrome string')          

'Q117. Find the sum of digits of a number using recursion.'

def sum_of_digit(digit):
    if digit == 0:
        return digit
    return  (digit % 10) + sum_of_digit(digit//10)    
print('The sum of digit is',sum_of_digit(123))

'Q118. Find the product of digits of a number using recursion.'
def sum_of_digit(digit):
    if digit == 0:
        return 1
    return  (digit % 10) * sum_of_digit(digit//10)    
print('The product of digit is',sum_of_digit(1234))


'Q119. Find the Greatest Common Divisor (GCD) of two numbers using recursion.'

def gcd(num1,num2):
    if num1 == 0:
        return num2
    return gcd(num2,num1 % num2)    
print('The greatest common divisor is : ',gcd(12,48))    


'Q120. Count the number of digits in a number using recursion.'


def count_digit(digit):
    if digit == 0:
        return digit
    return 1 + count_digit(digit//10)
print('The number of digit is :',count_digit(12345))        
