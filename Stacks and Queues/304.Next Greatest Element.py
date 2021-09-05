class Solution:
    def nextLargerElement(self,arr,n):
        #code here
        look = [-1] * n
        stack = []
        
        for i in range(n-1 , -1 , -1):
            while len(stack) > 0 and arr[i] > stack[-1]:
                stack.pop()
            
            if len(stack) != 0:
                look[i] = stack[-1]
            
            stack.append(arr[i])
            
        return look        
        
