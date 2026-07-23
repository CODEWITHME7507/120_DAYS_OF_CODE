'Day 6 of #120DaysOfCode | Python Lists Practice' 

 
'Q51. Find the Maximum Element in a List'

lis=[10,20,30,40,50,44,33,55,22,77,8,66,44]
max_ele=lis[0]
for i in lis:
    if i > max_ele:
        max_ele=i
print('Maximum element is : ',max_ele)        

'Q52. Find the Minimum Element in a List'

lis=[10,20,30,40,50,44,33,55,22,77,8,66,44]
min_ele=lis[0]
for i in lis:
    if i < min_ele:
        min_ele=i
print('Minimum element is : ',min_ele)        
    

'Q53. Find the Sum of All Elements in a List'

lis=[10,20,30,40,50,44,33,55,22,77,8,66,44]
sum_all_ele=0
for i in lis:
    sum_all_ele+=i
print('Sum of all element in a List : ',sum_all_ele)    

'Q54. Find the Average of List Elements'

lis=[10,20,30,40,50,44,33,55,22,77,8,66,44]
Avg_of_ele = sum(lis) / len(lis)
print('Average of a list is : ',Avg_of_ele)

'Q55. Find the Second Largest Element in a List'

lis=[10,20,30,40,50,44,33,55,22,77,8,66,44]
first_largest=max(lis)
second_largest=lis[0]
for i in lis:
    if i < first_largest:
        if i  > second_largest:
            second_largest = i 
print('second largest element is : ',second_largest)        


'Q56. Find the Second Smallest Element in a List'

lis=[10,20,30,40,50,44,33,55,22,77,8,66,44]
first_small=min(lis)
second_small=lis[0]

for i in lis:
    if i > first_small:
        if i < second_small:
            second_small = i
print('Second small element is : ', second_small)            

'Q57. Remove Duplicate Elements from a List'

lis=[10,20,30,10,20,30,40,50,44,33,55,22,77,8,66,44]
duplicates=[]
for i in range(1,len(lis)):
    if lis[i-1] in lis[i:]:
        duplicates.append(lis[i-1])
for i in duplicates:
    lis.remove(i)        
print('List without duplicate element : ', lis)        
    
    


'Q58. Check Whether an Element Exists in a List'

num=int(input('Enter a Element : '))
lis=[10,20,30,10,20,30,40,50,44,33,55,22,77,8,66,44]
if num in lis:
    print('Yes this Element is exist in list : ',num)
else:
    print('No this Element is not exist in list : ',num)    

'Q59. Reverse a List'

lis=[10,20,30,10,20,30,40,50,44,33,55,22,77,8,66,44]
lis.reverse()
print('Reversed list is : ', lis)


'Q60. Sort a List in Ascending Order'

lis=[10,20,30,10,20,30,40,50,44,33,55,22,77,8,66,44]
lis.sort()
print('Sorted list is : ',lis)
