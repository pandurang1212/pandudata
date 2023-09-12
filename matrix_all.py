import numpy as np

# initializing matrices
x = np.array([[1, 2], [4, 5]])
y = np.array([[7, 8], [9, 10]])

# using add() to add matrices
print ("The element wise addition of matrix is : ")
print (np.add(x,y))

# using subtract() to subtract matrices
print ("The element wise subtraction of matrix is : ")
print (np.subtract(x,y))

print ("The element wise multiplication of matrix is : ")
print (np.multiply(x,y))

# using divide() to divide matrices
print ("The element wise division of matrix is : ")
print (np.divide(x,y))

