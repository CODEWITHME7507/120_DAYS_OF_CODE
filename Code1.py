'''120 Days of Python Coding Challenge

Day 1 (Questions 1–10)'''

'''Q1. Print "Hello, World!"'''

print("Hello World!")

'''Q2. Take two numbers as input and print their sum.'''

num1=int(input('Enter a first number :'))
num2=int(input('Enter a second number :'))
print(f'addition of :{num1+num2}')

'''Q3. Take two numbers as input and print their difference.'''

num1=int(input('Enter a first number :'))
num2=int(input('Enter a second number :'))
print(f'difference of : {num1-num2}')

'''Q4. Take two numbers as input and print their product.'''

num1=int(input('Enter a first number :'))
num2=int(input('Enter a second number :'))
print('product of :',num1*num2)

'''Q5. Take two numbers as input and print their quotient.'''

num1=int(input('Enter a first number :'))
num2=int(input('Enter a second number :'))
print('quotient of :',num1/num2)

'''Q6. Swap two numbers without using a third variable.'''
num1=100
num2=200
num1,num2=num2,num1
print(f'swapped numbers num1 is :{num1} num2 is :{num2}')

'''Q7. Check whether a number is even or odd.'''

num1=int(input('Enter a number :'))
if num1%2==0:
    print('This is even number :',num1)
else:
    print('This is odd number',num1)    

'''Q8. Find the largest of two numbers.'''

num1=int(input('Enter a first number :'))
num2=int(input('Enter a second number :'))
if num1 > num2:
    print('num1 is greater than num2')
elif num2 > num1:
    print('num2 if greater than num1')
else:
    print('num1 and num2 is equal')        

'''Q9. Convert Celsius to Fahrenheit.'''

celsius=int(input('Enter a celsius'))
fahrenheit=celsius*9/5+32
print(f'celsius is: {celsius}')
print(f'fahrenheit is: {fahrenheit}F')


'''Q10. Take a number as input and print its square, cube, and square root.'''
num=int(input('Enter a number: '))
print('square of: ',num*num)
print('cube of ',num**3)
print('square root of',num**0.5)
