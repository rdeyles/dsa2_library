import numpy as np
MatrixA=np.random.randint(-10, 10, [3,6])
print(MatrixA)
MatrixB=np.matrix_transpose(MatrixA)
print(MatrixB)

MatrixC=np.matmul(MatrixA,MatrixB)
MatrixD=np.matmul(MatrixB,MatrixA)
print(MatrixC)
print(MatrixD)
