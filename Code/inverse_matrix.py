import numpy as np

M  = np.array([[1,1,1,-1],
     [1,1,-1,1],
     [1,-1,1,1],
     [-1,1,1,1]],dtype = float)

print(M)

def inverse(A):

  n_col = A.shape[1]
  n_row = A.shape[0]

  if n_col != n_row :
    print("Not Square Matrix")
    return

  I = np.identity(n_col)
  A = np.hstack((A,I))

  ## ECHELON 
  pivot_cols = []
  cur_pivot_row = 0

  for col in range(0,n_col):

    ## finding the row with maximum absolute value / partial pivoting
    max_abs_row = (0,-1) # (value,row)
    for row in range(cur_pivot_row, n_row):
      if np.abs(A[row][col]) >= max_abs_row[0]:
        max_abs_row = (np.abs(A[row][col]),row)

    ## row interchange (cur_pivot_row and max_abs_row) 
    A[[cur_pivot_row,max_abs_row[1]]] = A[[max_abs_row[1],cur_pivot_row]]

    if A[cur_pivot_row][col] != 0 :
      pivot_cols.append(col) ## updating pivot column
      for row in range(cur_pivot_row+1, n_row): ## eliminating everything down
        mul = A[row][col]/A[cur_pivot_row][col]
        A[row][col:] = A[row][col:] - mul*A[cur_pivot_row,col:]

      cur_pivot_row += 1

  if len(pivot_cols) < n_col :
    print("Determinant 0 , Not invertible")
    return

  ## RREF
  for col in pivot_cols:
    pivot_row = -1
    for row in range(n_row-1,-1,-1):
      if A[row][col] != 0 :
        pivot_row = row
        break

    A[pivot_row][:] = A[pivot_row][:] / A[pivot_row][col] # scaling to 1
      
    for row in range(0,pivot_row): ## eliminating everything up
      mul = A[row][col]/A[pivot_row][col]
      A[row][:] = A[row][:] - mul*A[pivot_row,:]

  return A[:,n_col:]
  
print(inverse(M))