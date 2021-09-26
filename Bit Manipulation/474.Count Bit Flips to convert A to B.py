class Solution:
    ##Complete this function
    # Function to find number of bits needed to be flipped to convert A to B
    def countBitsFlip(self,a,b):
        ##Your code here
        res = a ^ b
        def setbits(res):
            c = 0
            while res:
                c += 1
                res = res & (res-1)
            return c    
 
        return setbits(res)
