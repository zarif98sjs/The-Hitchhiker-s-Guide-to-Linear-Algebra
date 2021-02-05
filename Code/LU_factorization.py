import numpy as np

M = np.array([[2,4,-1,5,-2],
     [-4,-5,3,-8,1],
     [2,-5,-4,1,8],
     [-6,0,7,-3,1]],dtype = float)

print(M)

def LU_Factorization(A):

  n_col = A.shape[1]
  n_row = A.shape[0]

  cur_pivot_row = 0

  L = np.identity(n_row)

  for col in range(0,n_col):
    if A[cur_pivot_row][col] != 0 :
      for row in range(cur_pivot_row+1, n_row): ## eliminating everything down
        mul = A[row][col]/A[cur_pivot_row][col]
        A[row][col:] = A[row][col:] - mul*A[cur_pivot_row,col:]
        L[row][col] = mul
      cur_pivot_row += 1
      # print(A)
  U = A
  return L,U

L , U = LU_Factorization(M)

print(L)
print(U)