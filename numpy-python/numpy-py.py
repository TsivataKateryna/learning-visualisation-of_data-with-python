import numpy as np
import random as rd

def matrix_analysis(matrix : np.ndarray) -> None:
    print("matrix : ", matrix)
    print("determinant = ", np.linalg.det(matrix))
    print("rank :", np.linalg.matrix_rank(matrix))
    print("trace :", np.trace(matrix))
    print("inverse :", np.linalg.inv(matrix))
    print("norm :",  np.linalg.norm(matrix))
    print("eigenvalues / eigenvectors : ", np.linalg.eig(matrix))

def interpolation():
    pass

def mini_calculator():
    pass


A = np.random.randint(0, 10, size=(3, 3))

print(matrix_analysis(A))
# print(interpolation())
# print(mini_calculator())