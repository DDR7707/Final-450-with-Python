class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        # code here 
        top = 0
        bottom = n-1
        
        while top < bottom:
            if M[bottom][top] == 1:
                bottom -= 1
            else:
                top += 1
        
        for i in range(n):
            if i != top:
                if M[i][top] == 0 or M[top][i] == 1:
                    return -1
        return top   
      
      
https://www.geeksforgeeks.org/the-celebrity-problem/      
