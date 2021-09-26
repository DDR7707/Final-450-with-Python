def rowWithMax1s( mat):
     
    # Initialize max values
    R = len(mat)
    C = len(mat[0])
    max_row_index = 0
    index=C-1;
    # Traverse for each row and
    # count number of 1s by finding
    # the index of first 1
    for i in range(0, R):
      flag=False #to check whether a row has more 1's than previous
      while(index >=0 and mat[i][index]==1):
        flag=True #present row has more 1's than previous
        index-=1
        if(flag): #if the present row has more 1's than previous
          max_row_index = i
      if max_row_index==0 and mat[0][C-1]==0:
        return 0;
    return max_row_index
 
# Driver Code
mat = [[0, 0, 0, 1],
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 0, 0, 0]]
print ("Index of row with maximum 1s is",
    rowWithMax1s(mat))
