import numpy as np

A8 = np.array([[50, 29, 30], [30, 44, 5], [4, 5, 6]])
AI = np.identity(3, float)
det = np.linalg.det(A8)
print(det)
