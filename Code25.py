'Day 25 (Questions 226–230)'

'Q226. Find the longest increasing contiguous subarray in a list and return its length.'
lis=[1, 2, 3, 2, 4, 5, 6, 1]
def longest_increasing(lis):
    longest=[]
    lis1 = []
    for i in range(len(lis)-1):
        if lis[i] < lis[i+1]:
            longest.append(lis[i])
        else:
            longest.append(lis[i])
            lis1.append(len(longest))
            longest = []
    if len(longest) != 0:
        longest.append(lis[-1])
        lis1.append(len(longest))            
    return max(lis1)
print(longest_increasing(lis))               


'Q227. Find the maximum sum of any two non-adjacent elements in a list.'
lis=[5, 10, 20, 15, 30]
def non_adjacent(lis):
    adjecent_sum=[]
    sums=0
    for i in range(len(lis)-2):
        for j in range(i+2,len(lis)):
            adjecent_sum.append(lis[i]+lis[j])
    return adjecent_sum
print(non_adjacent(lis))            


