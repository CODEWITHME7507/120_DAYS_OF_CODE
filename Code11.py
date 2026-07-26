'Day 11 (Questions 101–110)'


'Q101. Create a function to add two numbers.'

def Addition(Num1,Num2):
    addtion=Num1+Num2
    print('Two Numbers Addition is : ',addtion)
Num1 = int(input('Enter Number 1 : '))
Num2 = int(input('Enter Number 2 : '))
Addition(Num1,Num2)    

'Q102. Create a function to check whether a number is even or odd.'

def Even_Odd_checker(Num):
    if Num % 2 == 0 :
        print('This number is Even : ',Num)
    elif Num % 3 != 0:
        print('This number is Odd : ',Num)
Num=int(input('Enter a Number'))
Even_Odd_checker(Num)    

'Q103. Create a function to find the factorial of a number.'

def Factorial_generator(Num):
    factorial=1
    for i in range(1,Num+1):
        factorial*=i
    print('Factorial is : ',factorial)
Num=int(input('Enter a Number '))
Factorial_generator(Num)        

'Q104. Create a function to check whether a number is prime.'

def Prime_checker(Num):
    if Num == 2:
        print('This is Prime Number')
        return
    elif Num <= 1:
        print('This is not Prime number')    
    for i in range(2,Num):
        if Num % i == 0 :
            print('This is Not Prime Number : ',Num)
            return
    print('This is prime number : ',Num)  
Num = int(input('Enter a Number '))
Prime_checker(Num)          

'Q105. Create a function to return the largest element in a list.'

def largest_ele(lis):
    large = lis[0]
    for i in lis:
        if i > large:
            large = i
    return large
lis=[10,20,30,40,50]
print('This is largest element in list : ',largest_ele(lis))            

'Q106. Create a function to reverse a string.'

def Reverse_string(string):
    return string[::-1]
string = 'shubham'
print('Reversed string is : ',Reverse_string(string))    

'Q107. Create a function to check whether a string is a palindrome.'

def Palindrome_checker(string):
    if string == string[::-1]:
        return 'This is palindrome '
    else:
        return 'This is not Palindrome '
string=input('Enter a string ')
print(Palindrome_checker(string))            

'Q108. Create a function to count vowels in a string.'

def vowels_counter(string):
    vowels_count = 0
    for i in string:
        if i.upper() in 'AEIOU':
            vowels_count+=1
    return vowels_count
string = input('Enter a string ')
print('The vowels in a string is : ',vowels_counter(string))            

'Q109. Create a function that accepts a list and returns the sum of all elements.'

def list_sum(lis):
    return sum(lis)
lis=[10,20,30,40,50,60,70]    
print('The sum of all element in list is : ',list_sum(lis))

'Q110. Create a function that accepts a sentence and returns the number of words.'

def word_counter(sentance):
    word_count=0
    for i in sentance:
        if i.isalpha():
            word_count+=1
    return word_count
sentance=input('Enter a sentance : ')
print('The Total word in sentance is : ',word_counter(sentance))            
