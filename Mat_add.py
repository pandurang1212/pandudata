
#program for matrix addition and subtraction using for loop
X = [[1,2,3],[4,5,6],[7,8,9]]
Y = [[9,8,7],[6,5,4],[3,2,1]]

result = [[0,0,0],[0,0,0],[0,0,0]]

#addition of two matrices
for i in range(3):
    for j in range(3):
        result[i][j] = X[i][j]+Y[i][j]
print("Matrix addition is")
print(result)

#subtracting two matrices
for i in range(3):
    for j in range(3):
        result[i][j] = X[i][j]-Y[i][j]
print("Matrix subtraction is")
print(result)
