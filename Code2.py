
'''Day 2 (Questions 11–20)'''

'''Q11. Check whether a number is positive, negative, or zero.'''

num=int(input('Enter a number'))
if num>=0:
    print('This is positive number')
else:
    print('This is negative number')
    
'''Q12. Find the largest of three numbers.'''

num1=int(input('enter first number'))
num2=int(input('enter second number'))
num3=int(input('enter third number'))

if num1 > num2 and num1 > num3:
    print('This is largest number than second and third :',num1)
elif num2 > num1 and num2 > num3:
    print('This is largest number than first and third :',num2)
elif num3 > num1 and num3 > num2:
    print('This is largest number than first and second :',num3)
else:
    print('These three numbers are equal')       
        

'''Q13. Check whether a given year is a leap year.'''

num1=int(input('enter a year'))

if (num1 % 400 == 0) or (num1 % 4 == 0) and (num1 % 100 != 0):
    print('This is leap year :', num1)
else:
    print('This is not leap year : ', num1)    

'''Q14. Check whether an alphabet is a vowel or consonant.'''

alpha=str(input('Enter a alphabet'))
if alpha.upper() in ['A','E','I','O','U']:
    print('This is vowel')
else:
    print('This is not vowel')
        
'''Q15. Create a simple calculator using if-elif-else (+, -, *, /).'''
print('ENTER + FOR ADDITION')
print('ENTER - FOR SUBTRACATION')
print('ENTER * FOR MULTIPlICATION')
print('ENTER / FOR DIVISION')
print('ENTER = FOR TOTAL CALCULATION')

num1=int(input('Enter a number'))
while True:
  sim=str(input('Enter what you want between (+,-,*,/,=) :'))
  
  if sim == '=':
      print('This is your total calculation : ',num1)
      break
  num2=int(input('Enter another number :'))    
  if sim == '+':
     num1 += num2
     print('This is sum of num1 and num2 :',num1)
  elif sim == '-':
     num1 -= num2
     print('This is substracation  of num1 and num2 :',num1)    
  elif sim == '*':
     num1 *= num2
     print('This is multiplication  of num1 and num2 :',num1)        
  elif sim == '/':
      if num2 != 0:
        num1 /= num2  
        print('This is division  of num1 and num2 :',num1)    
      else:
          print('division by zero is not allowed')  
  
  else:
     print('you enter wrong symbol')            

'''Q16. Check whether a number is divisible by both 5 and 11.'''

num1=int(input('Enter a number'))

if num1 % 5 == 0 and num1 % 11 == 0:
    print('Yes this number divisible by 5 and 11')
else:
    print('this number is not divisible by 5 and 11')    

'''Q17. Find the lowest number from list'''

num=[10,20,30,40,-1,4,8,0]
lowest=num[0]
for i in num:
    if i < lowest:
        lowest=i
print(lowest)        


'''Q18. Check whether a person is eligible to vote (age ≥ 18).'''
age= int(input('Enter your age: '))
if age>=18:
    print('you are eligible for vote')
else:
    print('you are not eligible for vote')    

'''Q19. Calculate a student's grade based on marks:
90–100 → A
80–89 → B
70–79 → C
60–69 → D
Below 60 → F'''

marks=int(input('Enter students marks: '))
if marks >= 90:
    print('A')
elif marks >= 80:
    print('B')
elif marks >= 70:
    print('C')
elif marks >= 60:
    print('D')
else:
    print('F')
    
        
'''Q20.Find maximum from lis'''
lis=[10,20,30,40,50,60,44,33,234,543,643,644,599]
maxx=lis[0]
for i in lis:
    if i > maxx:
        maxx = i
print(maxx)        
        
