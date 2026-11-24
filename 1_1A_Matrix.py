# Matrix Operations
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

add = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
mul = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
scalar = 3
result_scalar = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Matrix Addition
for i in range(3):
    for j in range(3):
        add[i][j] = A[i][j] + B[i][j]

# Matrix Multiplication
for i in range(3):
    for j in range(3):
        for k in range(3):
            mul[i][j] = mul[i][j] + A[i][k] * B[k][j]

# Scalar Multiplication
for i in range(3):
    for j in range(3):
        result_scalar[i][j] = scalar * A[i][j]  

print("Matrix A:")
print(A)
print("\nMatrix B:")  
print(B)
print("\nMatrix Addition (A + B):")
print(add)
print("\nMatrix Multiplication (A * B):")
print(mul)
print("\nScalar Multiplication (3 * A):")
print(result_scalar)