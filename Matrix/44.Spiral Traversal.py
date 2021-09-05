class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        top = 0
        bottom = m - 1
        left = 0
        right = n - 1
        final = []
        p = 1
        
        while len(final) < m*n:
            if p == 1:
                for i in range(left , right+1):
                    final.append(matrix[top][i])
                top += 1
                
            elif p == 2:
                for i in range(top , bottom+1):
                    final.append(matrix[i][right])
                right -= 1
            
            elif p == 3:
                for i in range(right , left-1 , -1):
                    final.append(matrix[bottom][i])
                bottom -= 1
            else:
                for i in range(bottom , top-1 , -1):
                    final.append(matrix[i][left])
                left += 1
            
            p = (p+1) % 4
        return final  
