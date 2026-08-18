'Day 23 (Questions 216–220)'

"""

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

"""
'Q217. Find the second most frequent character in a string.'

def second_frequent(string):
    dicts = {}
    lis = ' '.join(string).split()
    for i in lis:
        dicts[i]=lis.count(i)
    for i in dicts.keys():
        

string='shubham'
second_frequent(string)    

'Q218. Check whether two strings are rotations of each other.'



'Q219. Find all subarrays whose sum equals a given target.'



'Q220. Given an array of integers, find the element that appears more than N/2 times (majority element).'


