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

    
    
    
    class Solution:
    def intToRoman(self, num: int) -> str:
        look = {"I" : 1,
                "IV" : 4,
                "V" : 5,
                "IX" : 9,
                "X" : 10,
                "XL" : 40 ,
                "L" : 50,
                "XC" : 90,
                "C" : 100,
                "CD" : 400 ,
                "D" : 500 ,
                "CM" : 900,
                "M" : 1000}
        
        final = []
        
        for i , j in reversed(look.items()):
            while num > 0:
                if num >= j:
                    final.append(i)
                    num -= j
                else:
                    break
                    
        return "".join(final)   
