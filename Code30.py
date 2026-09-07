'''Day 30 
Q236.find the First Missing Positive Number.
given an unsorted list of integers, find the smallest positive integer that is missing from the list.

def first_missing_positive(lis):
    smallest_positive_element = max(lis)
    for i in lis:
        if i >= 1 and i < smallest_positive_element:
            smallest_positive_element = i        
    for j in range(smallest_positive_element,max(lis),1):
        if j  not in lis:
            return j       
lis = [1,-1,3,2,5]    
print(first_missing_positive(lis))
'''

'''Q237. Move All Negative Numbers to the Beginning.
Given a list of integers, move all negative numbers to the beginning while keeping the relative order of the 
remaining positive numbers.'''

def move_all_negative_beg(lis):
    for i in range(len(lis)):
        index = lis.index(min(lis[i:]))
        lis[index],lis[i] = lis[i],lis[index]
    return lis
    
lis=[1,-1,2,-2,-3,3,4,-4]
print(move_all_negative_beg(lis))        
