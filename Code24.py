'Day 24 (Questions 221–225)'


'Q221. Find the intersection of two arrays without using built-in set operations.'

def intersection(lis,lis1):
    intersec = []
    for i in lis:
        if i in lis1 and i not in intersec:
            intersec.append(i)
    return intersec
lis=[1,2,3]
lis1=[2,3,4]
print(intersection(lis,lis1))


'Q222. Find the union of two arrays without using built-in set operations.'

def union(lis,lis1):
    lis3=lis+lis1
    unio = []
    for i in lis3:
        if i not in unio:
            unio.append(i)
    return unio
lis=[1,2,3]
lis1=[2,3,4]
print(union(lis,lis1))            

'Q223. Move all zeroes to the end of a list while maintaining the relative order of non-zero elements.'

def move_zeroes(lis):
    for i in range(len(lis)):
            for j in range(i+1,len(lis)):
                if lis[i] == 0:
                    lis[i],lis[j] = lis[j],lis[i]
                     
    return lis
lis=[1,0,5,2,0,3,0,4]
print(move_zeroes(lis))                    


'Q224. Find the smallest missing positive integer from an unsorted list.'

def min_positive(lis):
    minpo=lis[0]
    for i in lis:
        if i < minpo and i > 0:
            minpo = i
    return minpo
lis=[1,-1,2,0,3,4,5,0.5]
print(min_positive(lis))            

'Q225. Find the maximum product of two elements in an integer list without sorting the list.'

def maximum_product(lis):
    maximum = lis[0]
    for i in range(len(lis)-1):
        for j in range(i+1,len(lis)):
            if (lis[i]*lis[j]) > maximum:
                maximum = lis[i] * lis[j]
    return maximum
lis=[1,2,3,4,5]
print(maximum_product(lis))                
