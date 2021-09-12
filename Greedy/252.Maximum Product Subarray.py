class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        final = nums[0]
        low , high = nums[0] , nums[0]
        
        for i in range(1,len(nums)):
            temp_low = min(nums[i] , nums[i]*low , nums[i]*high)
            temp_high = max(nums[i] , nums[i]*low , nums[i]*high)
            
            low , high = temp_low , temp_high
            
            final = max(final , high)
            
        return final 
