'Day 22 (Questions 211–215)'

"""

'Q211. Find the top 3 largest unique elements in a list without using sort().'

lis=[10,20,80,40,30,10,60,70]
def unique_largest(lis):
    maxx=[]
    large = 0
    for i in lis:
        if max(lis) not in maxx and large < 3:
            maxx.append(max(lis))
            lis.remove(max(lis))
            large += 1
    return maxx    
print(unique_largest(lis))        

'Q212. Find all pairs of elements in a list whose difference equals a given number.'

lis=[10,20,30,40,50,10,20,30]
equal = 10
def find_all_pairs(lis,equal):
    pairs = 0
    for i in range(len(lis)-1):
        for j in range(i+1,len(lis)):
           if abs(lis[i] - lis [j]) == equal:
              pairs+=1            
    return pairs
print(find_all_pairs(lis,equal))                 


'Q213. Find the most frequent element in a list. If multiple elements have the same frequency, return the first one.'
lis=[10,20,30,40,50,60,70,80,70]
def  frequent_element(lis):
    dicts={}
    for i in lis:
        dicts[i]=lis.count(i)
    if max(dicts.values()) == all(dicts.values()):
        return lis[0]
    for j in dicts.keys():
        if dicts[j] == max(dicts.values()):
            return j 
print(frequent_element(lis))
"""
'Q214. Find the longest substring without repeating characters.'



'Q215. Given a string containing letters, digits, and special characters, find the character that occurs most frequently, ignoring spaces and treating uppercase/lowercase as the same.'