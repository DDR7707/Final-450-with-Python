    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        if n == 2:
            return "11"
        s = "11"
        for i in range(2,n):
            count = 1
            res = ""
            
            for j in range(len(s)):
                if j == len(s)-1:
                    res += str(count) + s[j]
                    break
                    
                elif s[j] == s[j+1]:
                    count += 1
                
                else:
                    res += str(count) + s[j]
                    count = 1
            s = res
        return res    
