'Day 26'



'Q228. Find the common elements between two lists without using set().'

def common_elements(lis,lis1):
    commion = []
    for i in lis:
        if i in lis1 and i not in commion:
            commion.append(i)
    return commion
lis = [10,20,30,40,50]
lis1 = [20,30,40,50,60]
print(common_elements(lis,lis1))            

'Q229. Count the frequency of each element in a list using a dictionary.'

def frequency_count(lis):
    dicts = {}
    for i in lis:
        dicts[i]=dicts.get(i,0)+1
    return dicts
lis=[10,20,30,40,50,60,70,10,20,10,30,20,40,30]
print(frequency_count(lis))        
