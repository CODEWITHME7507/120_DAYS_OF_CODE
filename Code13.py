'Day 13 (Questions 121–130)'

"""

'Q121. Use a lambda function to find the square of a number.'

a=20
lamd = lambda a : a ** 2
print('The square of a number is :',lamd(a))

'Q122. Use the map() function to square all elements in a list.'

lis=[10,20,30,40,50,60]
def square(a):
    return a ** 2
lis1=list(map(square,lis))  
print(lis1)

'Q123. Use the filter() function to extract all even numbers from a list.'

lis=[1,2,3,4,5,6,7,8,9]
def extract(a):
    if a % 2 == 0:
        return a
lis1=list(filter(extract,lis))
print(lis1)        

'Q124. Use the filter() function to extract all prime numbers from a list.'

def prime_extract(a):
    if a <= 1:
        return 0
    
    for i in range(2,a):
        if a % i == 0:
            return 0
    return a
lis = [1,2,3,4,5,6,7,8,9]
lis1=list(filter(prime_extract,lis))
print(lis1)    



'Q125. Use the reduce() function to find the sum of all elements in a list.'

import functools as fv 
def sum_of_list(a,b):
    return a+b
lis=[1,2,3,4,5]
lis1=fv.reduce(sum_of_list,lis)
print(lis1)    

'Q126. Use the reduce() function to find the product of all elements in a list.'

import functools as fv
def product(a,b):
    return a*b
lis=[1,2,3,4,5,6]
lis1=fv.reduce(product,lis)    
print(lis1)

'Q127. Sort a list of tuples using a lambda function based on the second element.'

lam=[(1,2),(4,3),(1,1)]
lam1=sorted(lam,key = lambda a : a[0])
print(lam1)

'Q128. Sort a list of dictionaries by a specific key using a lambda function.'

lis=[{'age':1},{'age':24},{'age':0},{'age':10},{'age':20}]
lam=sorted(lis,key = lambda a : a['age'])
print(lam)

'Q129. Use map() to convert a list of strings into uppercase.'

lis1=['s','h','u','b','h','a','m']
def convert_upper(a):
    return a.upper()
lis= list(map(convert_upper,lis1))
print(lis)    
"""
'Q130. Use filter() and lambda together to remove all negative numbers from a list.'

lis=[1,2,-2,-2,1,-3,10,-22]
fil = list(filter(lambda a : a if a >= 0 else 0,lis))
print(fil)