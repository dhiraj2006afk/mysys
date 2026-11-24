# Eigenvectors, Eigenvalues and Diagonalization
import numpy as np

A = np.array([[4, -2], [1, 1]])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Matrix A:")
print(A)
print("Eigenvalues:")
print(eigenvalues)
print("Eigenvectors:")
print(eigenvectors)

P = eigenvectors
D = np.diag(eigenvalues)
A_check = P @ D @ np.linalg.inv(P)
print("\nDiagonalization(P * D * P^-1):")
print(A_check)
