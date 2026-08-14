'Day 21 (Questions 201–210)'

"""

'Q201. Create a program to find the second largest element in a list without using sort().'

def second_largest(lis):
    second_largest=lis[0]
    for i in lis:
        if i > second_largest and i != max(lis):
            second_largest = i
    print('Second Largest Element is: ',second_largest)
lis = [10,20,30,40,20,30,40,50,60,90,40,60]             
second_largest(lis)

'Q202. Find all duplicate elements in a list.'

def duplicate_element(lis):
    duplicate = set()
    unique = []
    for i in lis:
        if i not in unique:
            unique.append(i)
        else:
            duplicate.add(i)
    print('Duplicate element is: ',duplicate)            
lis = [10,20,30,40,20,30,40,50,60,90,40,60]
duplicate_element(lis)


'Q203. Find the first non-repeating character in a string.'

def non_repeating(string):
    seen = []
    for i in range(len(string)):
        if string[i] not in string[i+1:] and string[i] not in seen:
            return string[i]
        elif string[i] in string[i+1:]:
            seen.append(string[i])           
string = 'shubhamshubhap'            
print("first non-repating character is : ",non_repeating(string))            

'Q204. Find the first repeating element in a list.'

def first_repeating(lis):
    for i in range(len(lis)):
        if lis[i] in lis[i+1:]:
            return lis[i]
    return 'No repeating element in list'        
lis = [10,20,30,40,20,30,40,50,60,90,40,60]
print(first_repeating(lis))            

'Q205. Find the missing number from a list containing numbers from 1 to N.'

def missing_number(lis,n):
    return n * (n + 1) // 2 - sum(lis)
lis=[1,2,4,5]
n=5
print(missing_number(lis,n))    

'Q206. Find all pairs of numbers in a list whose sum equals a given target.'

def all_pairs(lis,target):
    pairs=0
    for i in range(len(lis)):
        for j in range(i+1,len(lis)):
            if (lis[i] + lis[j]) == target:
                pairs += 1
    return pairs
lis = [10,20,30,40]
target=70
print('The number of pairs is : ',all_pairs(lis,target))                

'Q207. Find the maximum sum of a contiguous subarray.'

def maximum_sum(arr):
    current_sum = arr[0]
    max_sum = arr[0]
    for num in arr[1:]:
      current_sum = max(num, current_sum + num)
      max_sum = max(max_sum, current_sum)
    return max_sum
arr=[10,20,30,-30,-40,50]
print(maximum_sum(arr))    
"""

'Q208. Rotate a list to the right by K positions.'

def rotate_list(lis,k):
    if len(lis) < k:
        return 'Rotate is not possible'
    for i in range(k,0,-1):
        print(i)
    return lis
lis = [1,2,3,4,5]
k=2
print(rotate_list(lis,k))        




'Q209. Find the intersection of three lists without duplicate values.'



'Q210. Find the longest consecutive sequence of integers in an unsorted list.'


