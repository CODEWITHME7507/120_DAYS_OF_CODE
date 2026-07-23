'''Day 7 (Questions 61–70)'''

'''Q61. Create a tuple and print all its elements.'''

tup=(10,20,30,40,50,60)
print(tup)

'''Q62. Find the length of a tuple.'''

tup=(10,20,30,40,50,60)
print(len(tup))

'''Q63. Check whether an element exists in a tuple.'''

tup=(10,20,30,40,50,60)
ele=int(input('Enter a Element'))
if ele in tup:
    print('Yes this element exist : ',ele)
else:
    print('No this element Not exist : ',ele)    

'''Q64. Count the number of occurrences of a specific element in a tuple.'''

spe_ele=int(input('Enter a Element'))
tup=(10,20,30,40,50,6010,20,30,40,20,10,20,10,20,10,40,90,50)
count=tup.count(spe_ele)
print(f'occurrence of {spe_ele} is: ',count)


'''Q65. Find the index of a given element in a tuple.'''

ind_ele=int(input('Enter a Element'))
tup=(10,20,30,40,50,6010,20,30,40,20,10,20,10,20,10,40,90,50)
index=[]
for i in range(len(tup)):
    if tup[i] == ind_ele:
        index.append(i)
print('The element index is: ',index)        



'''Q66. Create two sets and find their union.'''

set1={10,20,30,10,30,20,33,55,66,77}
set2={99,30,22,44,221,30,20,10,40,66}

set3=set1.union(set2)
print('The union of set1 and set2 is: ',set3)


'''Q67. Create two sets and find their intersection.'''

set1={10,20,30,10,30,20,33,55,66,77,100}
set2={99,30,22,44,221,30,20,10,40,66,100}

set3=set1.intersection(set2)
print('The intersection of set1 and set2 is: ',set3)

'''Q68. Create two sets and find their difference.'''

set1={10,20,30,10,30,20,33,55,66,77,100}
set2={99,30,22,44,221,30,20,10,40,66,100}

set3=set1.difference(set2)
print('The difference between set1 and set2 is: ',set3)

'''Q69. Remove duplicate elements from a list using a set.'''

lis=[10,20,30,40,50,10,20,40,60,10,20,40,44,22,00]
lis=list(set(lis))
print('Remove duplicate element using set : ',lis)

'''Q70. Check whether one set is a subset of another set.'''

set1={10,20,30,10,40,30,20,33,55,66,77,100}
set2={10,20,30,40}
sub1=set1.issubset(set2)
sub2=set2.issubset(set1)

if sub1:
    print('set1 is subset of set2')
elif sub2:
    print('set2 is subset of set1')
else:
    print('set1 and set2 these are subset of each other')        
