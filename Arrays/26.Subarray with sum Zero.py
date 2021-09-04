class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        ##Your code here
        #Return true or false
        look = set()
        final = 0
        
        for i in range(n):
            final += arr[i]
            if final in look or final == 0:
                return True
            look.add(final)
        return False  
