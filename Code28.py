'Day 28'
"""
'Q232. Find the longest word in a sentence. If multiple words have the same length, return the first one.'

def longest_word(sentence):
    longest_word=len(sentence[0])
    word = sentence[0]
    for i in sentence.split():
        if len(i) > longest_word:
            longest_word = len(i)
            word = i 
    return word
sentence='My name is shubham phuke'
print(longest_word(sentence))            
"""
'Q233. Check whether two strings are anagrams of each other without using sorted().'

def anagrams(s1,s2):
    if len(s1) != len(s2):
        return None
    dicts= dict()
    for i in s1:
        dicts[i] = dicts.get(i,0)+1
    for j in s2:
        if dicts[j] != ' '.join(s1).split().count(j):
            return "This strings are not anagrams of each other"
    
    return "This strings are anagrams of each other"        
print(anagrams('ssdf','ssdf'))        

