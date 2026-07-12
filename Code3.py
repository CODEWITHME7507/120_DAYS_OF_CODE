'''Day 3 (Questions 21–30)'''
'''Q21. Print numbers from 1 to 100 using a for loop.'''

for i in range(1,101):
    print(i)

'''Q22. Find the sum of the first N natural numbers.'''
natural_num=14
sum_natural_num=0
for i in range(natural_num+1):
    sum_natural_num+=i
print(sum_natural_num)    
    
'''Q23. Print the multiplication table of a given number.'''

number=int(input('Enter a number'))
for i in range(1,11):
    print(number*i)

'''Q24. Find the factorial of a number.'''

number=int(input('Enter a number'))
facto=1
for i in range(1,number+1):
    facto*=i
print(facto)    

'''Q25. Count the number of digits in an integer.'''

number=int(input('Enter a number'))
number_of_digit=0
while number != 0:
    number = number // 10
    print(number)
    number_of_digit+=1
print(number_of_digit)    

'''Q26. Find the sum of digits of a number.'''
number=int(input('Enter a number'))
digit_sum=0
for i in str(number):
    if i.isdigit():
        digit_sum+=int(i)
print(digit_sum)                

'''Q27. Reverse a given number.'''

number=int(input('Enter a number'))
rever=''
num=str(number)
if '-' in num:
    rever+='-'
for i in num[::-1]:
    if i.isdigit():
        rever+=i
print(int(rever))        
        

'''Q28. Check whether a number is a palindrome.'''

number=int(input('Enter a number'))
palin=str(abs(number))
if number == int(palin[::-1]):
    print('This is palindrome number')
else:
    print('this is not palindrome number')    

'''Q29. Generate the Fibonacci series up to N terms.'''

number=int(input('Enter a number'))
num1=0
num2=1
for i in range(number):
    print(num1,end=' ')
    c=num1 + num2
    num2=num1
    num1=c
   
'''Q30. Check whether a number is an Armstrong number.'''

number=int(input('Enter a number'))
num=str(abs(number))
arm=0
for i in num:
   arm+=int(i)**len(num)
if number == arm:
    print('This is armstrong number') 
else:
    print('This is not armstrong number') 
         
   
