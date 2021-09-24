class Solution:
    def romanToDecimal(self, S): 
        # code here
        prev = 0
        cur = 0
        final = 0
        look = {"I" : 1 ,
                "V" : 5 , 
                "X" : 10 ,
                "L" : 50 ,
                "C" : 100 ,
                "D" : 500 ,
                "M" : 1000
        }
        
        for i in S[::-1]:
            cur = look[i]
            if cur >= prev:
                final += cur
            else:
                final -= cur
            prev = cur
        return final    
