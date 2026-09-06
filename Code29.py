#Day 29 

'''Q234. Find the Longest Palindromic Substring
Given a string, find the longest substring that reads the same forward and backward.
Example:
Input:  "babad"
Output: "bab" '''

def longest_palindrome(string):
    if string == string[::-1]:
        return string
    longest_string = ""
    for i in range(len(string)):
        curr_long_str = ''
        for j in range(i,len(string)):
            curr_long_str += string[j]
            if curr_long_str == curr_long_str[::-1]:
                if len(curr_long_str) > len(longest_string):
                    longest_string = curr_long_str
    return longest_string    
string = "shhsd"
print(longest_palindrome(string))        
    


'''Q235. Find the Missing Number in an Unordered List
You are given numbers from 1 to N, but one number is missing. The list is not necessarily sorted. Find the missing number.
Example:
Input:  [4, 1, 3, 5, 2, 7]
Output: 6 '''

def missing_number(lis):
    missing_numbers = []
    for i in range(1,max(lis)+1):
        if i not in lis:
            missing_numbers.append(i)
    if len(missing_numbers) == 1:
        return missing_numbers[0]
    return missing_numbers
lis = [1,3,4,6,5]
print(missing_number(lis))

