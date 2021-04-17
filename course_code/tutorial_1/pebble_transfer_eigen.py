import numpy as np
from math import isclose
 
neighbor =  [[1, 3, 0, 0], [2, 4, 0, 1], [2, 5, 1, 2],
             [4, 6, 3, 0], [5, 7, 3, 1], [5, 8, 4, 2],
             [7, 6, 6, 3], [8, 7, 6, 4], [8, 8, 7, 5]]
transfer = np.zeros((9, 9))
for k in range(9):
    for neigh in range(4): transfer[neighbor[k][neigh], k] += 0.25
print(transfer)
eigenvalues, eigenvectors = np.linalg.eig(transfer)
# print(eigenvalues)
 
# you may print the eigenvectors by uncommenting the following lines...
for iter in range(9):
    # print(eigenvalues[iter])
    if isclose(eigenvalues[iter], 1):
        print(eigenvectors[..., iter] ** 2)

    # if isclose(eigenvalues[iter], 0.75):
    #     print(eigenvectors[..., iter] ** 2)

    # print([eigenvectors[i][iter] for i in range(9)])
