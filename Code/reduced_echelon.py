def rref(A):

  A , pivot_cols = echelon(A)

  n_col = A.shape[1]
  n_row = A.shape[0]

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

  return A , pivot_cols