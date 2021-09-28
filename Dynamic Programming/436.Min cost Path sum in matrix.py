class Solution:
    def maximumPath(self, N, Matrix):
        # code here
        for i in range(N-2 , -1 , -1):
            for j in range(0,N):
                if j == 0:
                    Matrix[i][j] += max(Matrix[i+1][j] , Matrix[i+1][j+1])
                elif j == N-1:
                    Matrix[i][j] += max(Matrix[i+1][j] , Matrix[i+1][j-1])
                else:
                    Matrix[i][j] += max(Matrix[i+1][j] , Matrix[i+1][j-1] , Matrix[i+1][j+1])
                
        return max(Matrix[0]) 
