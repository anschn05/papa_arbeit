import numpy as np

# A = np.matrix([[1,2,0],
#                [0,-1,0],
#                [0,0,2]])

# Ainv = np.linalg.inv(A)
# print('A:\n',Ainv)


# detA = np.linalg.det(A)
# print(detA)

B = np.matrix([[2,0,0],
               [0,1,3],
               [0,0,-3]])

Binv = np.linalg.inv(B)

print('B:\n',Binv)
detB = np.linalg.det(B)
print(detB)