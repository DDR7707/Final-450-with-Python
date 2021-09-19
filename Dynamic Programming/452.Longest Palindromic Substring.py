class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(l , r):
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1
            return s[l+1:r]
        
        final = ""
        for i in range(len(s)):
            temp = helper(i,i)
            
            if len(temp) > len(final):
                final = temp
                
            temp = helper(i , i+1)
            
            if len(temp) > len(final):
                final = temp
                
        return final        
