
#program for matrix addition and subtraction using for loop
X = [[1,2,3],[4,5,6],[7,8,9]]
Y = [[9,8,7],[6,5,4],[3,2,1]]

result = [[0,0,0],[0,0,0],[0,0,0]]

#Multiplying two matrices
for i in range(3):
    for j in range(3):
        for k in range(3):
            result[i][j] += X[i][k]*Y[k][j]
print("matrix multiplication is")
print(result)



