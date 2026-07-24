'Day 9 (Questions 81–90)'

'Q81. Create a 3×3 matrix and print it.'

matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]
print('Matrix 3 * 3 is : ',matrix)        

'Q82. Add two matrices.'

matrix1=[[1,2,3],
        [4,5,6],
        [7,8,9]]
matrix2=[[1,2,3],
        [4,5,6],
        [7,8,9]]   
matrix3 = []
for i,j in zip(matrix1,matrix2):
    m3=[]
    for m1,m2 in zip(i,j):
        m3.append(m1+m2)
    matrix3.append(m3)

        
print('Matrices matrix1 and matrix2 Addition is : ',matrix3)             

'Q83. Subtract two matrices.'

matrix1=[[1,2,3],
        [4,5,6],
        [7,8,9]]
matrix2=[[1,2,3],
        [4,5,6],
        [7,8,9]]   
matrix3 = []
for i,j in zip(matrix1,matrix2):
    m3=[]
    for m1,m2 in zip(i,j):
        m3.append(m1-m2)
    matrix3.append(m3)

print('Matrices matrix1 and matrix2 Substracation is : ',matrix3)

'Q84. Multiply two matrices.'

matrix1=[[1,2,3],
        [4,5,6],
        [7,8,9]]
matrix2=[[1,2,3],
        [4,5,6],
        [7,8,9]]   
matrix3 = []
for i,j in zip(matrix1,matrix2):
    m3=[]
    for m1,m2 in zip(i,j):
        m3.append(m1*m2)
    matrix3.append(m3)

print('Matrices matrix1 and matrix2 Multiplication is : ',matrix3)

'Q85. Find the transpose of a matrix.'

matrix=[[1,2,3],
        [4,5,6]]

trans=[] 

      
for j in range(len(matrix[0])):
    m1=[]
    for i in range(len(matrix)):
        m1.append(matrix[i][j])
    trans.append(m1)

print('Transpose matrix is : ',trans)




'Q86. Find the sum of the main diagonal elements of a square matrix.'

matrix1=[[1,2,3],
        [4,5,6],
        [7,8,9]]
sum_of_dia=0

for i in range(len(matrix1)):
    sum_of_dia += matrix1[i][i]
print('The Sum of main diagonal is : ',sum_of_dia)    


'Q87. Find the sum of the secondary diagonal elements of a square matrix.'

matrix1=[[1,2,3],
        [4,5,6],
        [7,8,9]]
sum_of_second=0       
for i in range(1,len(matrix1)):
    sum_of_second += matrix1[i-1][-i]
print('The Sum of secondary diagonal is : ',sum_of_second)            

'Q88. Check whether a matrix is an identity matrix.'

matrix1=[[1,0,0],
        [0,1,0],
        [0,0,1]]
identity=True
for i in range(len(matrix1)):
    if matrix1[i][i] != 1:
        identity = False
if identity:
    print('This is Identity matrix ',matrix1)        
else:
    print('This is not Identity matrix ',matrix1)

'Q89. Check whether a matrix is a symmetric matrix.'

matrix1=[[1,2,3],
         [2,3,4],
         [3,4,5]]
symmetric = True         
for i in range(len(matrix1)):
    for j in range(len(matrix1)):
      if matrix1[i][j] != matrix1[j][i]:
        symmetric = False
if symmetric:
    print('This is symmetric matrix',matrix1)
else:
    print('This is not symmetric matrix',matrix1)   

'Q90. Find the largest element in a matrix.'
matrix1=[[12212,21321,31212],
         [2133,313,4132],
         [3121,4121,5121]]

largest_element=matrix1[0][0]

for i in range(len(matrix1)):
    for j in range(len(matrix1[i])):
        if matrix1[i][j] > largest_element:
            largest_element = matrix1[i][j]
print('The largest number in matrix is : ', largest_element)            
