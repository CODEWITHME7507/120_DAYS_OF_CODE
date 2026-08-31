'Day 27'
"""
'Q230. Find the second smallest unique element in a list without using sort().'

def second_smallest(lis):
    unique = []
    second_small = None
    for i in lis:
        if lis.count(i) == 1:
            unique.append(i)
    if len(unique) < 2:
        return None        
    for j in unique:
        if j != min(unique):
            if second_small is None or second_small > j:
                second_small = j
    return second_small
lis=[1,2,3,4,5,6,7,1,2,34,5,3,2,1,5,9,4]
print(second_smallest(lis))                        

"""

'Q231. Reverse the order of words in a sentence without reversing the characters of each word.'

def reverse_sentence(sentance):
    sen = sentance.split()
    return ' '.join(sen[::-1])
sentance = 'I love python' 
print(reverse_sentence(sentance))   