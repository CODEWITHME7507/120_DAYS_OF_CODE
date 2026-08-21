'Day 23 (Questions 216–220)'



'Q216. Find the longest word in a sentence without using max().'

def longest_word(sentence):
    lis = sentence.split()
    longest_word = lis[0]
    length = len(lis[0])
    for i in lis:
        if len(i) > length:
            length = len(i)
            longest_word = i
    return longest_word            

sentence='my name is shubham '
print(longest_word(sentence))


'Q217. Find the second most frequent character in a string.'

def second_frequent(string):
    dicts = {}
    for i in string:
        dicts[i]=dicts.get(i,0)+1
    frequent = sorted(dicts.values(),reverse= True)  
    second = frequent[1]
    for i in dicts.keys():
        if dicts[i] == second:
            return i
string='sshhubham'
print(second_frequent(string))    

'Q218. Check whether two strings are rotations of each other.'

def rotations_eachother(lis,lis1):
    if len(lis) == len(lis1) and lis in (lis + lis1):
        return 'Rotation'
    else : 
        return 'Not Rotation'
lis = "abcd"
lis1="acbd"
print(rotations_eachother(lis,lis1))


'Q219. Find all subarrays whose sum equals a given target.'

def subarrays_equal(lis,target):
    sub_arrays = []
    for i in range(len(lis)-1):
        for j in range(i+1,len(lis)):
            if (lis[i] + lis[j]) == target :
                sub_arrays.append([lis[i],lis[j]])
    return sub_arrays
lis=[10,20,30,40,50,20,30]
target = 60
print(subarrays_equal(lis,target))

'Q220. Given an array of integers, find the element that appears more than N/2 times (majority element).'

def appears_more2(lis):
    more2=[]
    for i in lis:
        if lis.count(i) >= 2 and i not in more2:
            more2.append(i)
    
    print('Element who appers more than 2 or 2 is :',more2)
lis=[10,20,30,10,20,30,40]
appears_more2(lis)            
