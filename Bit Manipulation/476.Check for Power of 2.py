class Solution:
    ##Complete this function
    # Function to check if given number n is a power of two.
    def isPowerofTwo(self,n):
        ##Your code here
        if n == 0:
            return False
        return True if n & (n-1) == 0 else False
