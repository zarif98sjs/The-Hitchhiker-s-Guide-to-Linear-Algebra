def echelon(A):

  n_col = A.shape[1]
  n_row = A.shape[0]

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
      # print(A)

  return A , pivot_cols