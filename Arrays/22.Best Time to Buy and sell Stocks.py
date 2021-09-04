class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ref = prices[0]
        final = 0
        
        for i in range(1,len(prices)):
            if prices[i] < ref:
                ref = prices[i]
            
            else:
                final = max(final , prices[i]-ref)
        
        return final
