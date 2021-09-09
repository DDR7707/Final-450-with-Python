class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs , key = lambda x : x[1])
        temp = float("-inf")
        final = 0
        
        for x,y in pairs:
            if temp < x:
                temp = y
                final += 1
        
        return final
