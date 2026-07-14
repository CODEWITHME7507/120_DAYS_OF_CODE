'''Day 4 (Questions 31–40)'''

'''Q31. Check whether a number is a Prime Number.'''

num=int(input('Enter a number'))
is_prime=True
for i in range(2,num):
    if num % i == 0:
        is_prime=False
        break
    if is_prime:
        print('Prime number')
    else:
        print('not a prime number')        

'''Q32. Print all Prime Numbers between two given numbers.'''

start = int(input('Enter a starting number'))
end = int(input('Enter a ending number'))

for i in range(start,end+1):
    if i >= 2:
        is_prime = True
    for j in range(2,i):
        if i % j == 0:
            is_prime=False
            break
    if is_prime:
        print(i)         

'''Q33. Find the Greatest Common Divisor (GCD/HCF) of two numbers.'''

num1=int(input('Enter first number'))
num2=int(input('Enter second number'))
if num1 > num2:
    num1,num2 = num2,num1
gcd = 0
for i in range(1,num1+1):
    if num1 % i == 0 and num2 % i == 0:
        gcd=i
print('The gcd is :',gcd)        

'''Q34. Find the Least Common Multiple (LCM) of two numbers.'''

num1=int(input('Enter a first number'))
num2=int(input('Enter a second number'))
lcm=1
while True:
    if  lcm % num1 == 0 and lcm % num2 == 0:
        print('The lcm is:',lcm)
        break
    lcm+=1     
'''Q35. Check whether a number is a Perfect Number.'''

num = int(input('Enter a number'))
perfect=False
count=0
for i in range(1,num):
    if num % i == 0:
       count+=i
    elif count > num:
        break
if count == num:
    perfect = True   
if perfect:
    print('This is perfect number')
else:
    print('This is not perfect number')        
            
'''Q36. Check whether a number is a Strong Number.'''
num=int(input('Enter a number : '))
fact=0
numstr=str(num)
for i in numstr:
    ints=int(i)
    count=1
    for j in range(1,ints+1):
        count*=j
    fact+=count    
if fact == num:
    print('This is strong number')  
else:
    print('This is not strong number ')
                              
'''Q37. Check whether a number is an Automorphic Number.'''

num = int(input('Enter a number'))
if num == 1:
    print("This is Automorphic number")
    exit() 
numstr=str(num)
square=num**2
squstr=str(square)
if num == int(squstr[len(numstr):]):
    print('This is Automorphic number')
else:
    print('This is not Automorphic number')

'''Q38. Check whether a number is a Harshad (Niven) Number.'''

num = int(input('Enter a number'))
numstr=str(num)
count=0
for i in numstr:
    count+=int(i)
if num % count == 0:
    print('This is niven number')
else:
    print('This is  not niven number')

'''Q39. Check whether a number is a Neon Number.'''

num = int(input('Enter a number'))
squa=str(num**2)
digit_sum = 0
for i in squa:
    digit_sum+=int(i)
if digit_sum == num :
    print('This is neon number') 
else:
    print('This is not neon number')       

'''Q40. Check whether a number is a Spy Number.'''
num = int(input('Enter a number'))
numstr=str(num)
pro=1
sum=0
for i in numstr:
    k=int(i)
    pro*=k
    sum+=k
if pro == sum :
    print('This is spy number')
else:
    print('This not spy number')
