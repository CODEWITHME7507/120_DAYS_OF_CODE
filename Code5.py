'Day 5 (Questions 41–50)'

'Q41. Count the number of vowels and consonants in a string.'

string=str(input('Enter a string : '))

vowels=0
consonants=0
for i in string:
    if i.upper() in 'AEIOU':
        vowels+=1
    else:
        consonants+=1
print('Vowels in this string is :', vowels)
print('Consonants in this string is :',consonants)


'Q42. Reverse a given string.'

string=str(input('Enter a string : '))
rev=string[::-1]
print('Reverse string',rev)

'Q43. Check whether a string is a palindrome.'

string=str(input('Enter a string : '))

if string == string[::-1]:
    print('This is palindrome string ',string)
else:
    print('This is not palindrome string',string)    

'Q44. Count the frequency of each character in a string.'

string=str(input('Enter a string : '))
dicts=dict()
stringb=string.upper()
for i in stringb:
    dicts[i]=stringb.count(i)
for i,j in dicts.items():
    print(f'frequency of {i} is :',j)  

'Q45. Remove all spaces from a string.'

string=str(input('Enter a string : '))
withoutspace=''
for i in string:
    if i != ' ':
        withoutspace+=i
print(withoutspace)        

'Q46. Count the number of words in a sentence.'

string=str(input('Enter a string : '))
words=string.split()
count_words=len(words)
print('words in sentence is :',count_words)

'Q47. Convert a string from uppercase to lowercase and lowercase to uppercase.'

string=str(input('Enter a string : '))
upper_lower_rev=''
for i in string:
    if i.isupper():
        upper_lower_rev += i.lower()
    else:
        upper_lower_rev += i.upper()
print('uppercase to lowercase and lowercase to uppercase :',upper_lower_rev)            

'Q48. Check whether two strings are anagrams.'

string1=str(input('Enter a string 1: '))
string2=str(input('Enter a string 2: '))

if len(string1) != len(string2):
    print('These are not anagrams strings') 
    exit()

sort1,sort2=sorted(string1),sorted(string2)
anagrams=True
for i,j in zip(sort1,sort2):
    
    if  i != j:
        anagrams=False
        break
if anagrams:
    print('These are anagrams strings')
else:
    print('These are not anagrams strings')            

'Q49. Replace all vowels in a string with *.'

string=str(input('Enter a string: '))
repwith=''
for i in string:
    if i.upper() in 'AEIOU':
        repwith += '*'
    else:
        repwith += i    
print('Replaced with * string is :',repwith)

'Q50. Find the longest word in a sentence.'

string=str(input('Enter a sentance: '))
words=string.split()
longest_word=words[0]
word_size=len(words[0])
for i in words:
    if len(i) > word_size:
        word_size=len(i)
        longest_word=i
print('The longest word in sentance is :',longest_word)
