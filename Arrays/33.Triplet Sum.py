#User function Template for python3
class Solution:
     
    #Function to find if there exists a triplet in the 
    #array A[] which sums up to X.
    def find3Numbers(self,A, n, X):
        # Your Code Here
        A.sort()
        for i in range(n):
            l = i+1
            r = n-1
            while l < r:
                add = A[i] + A[l] + A[r]
                if add == X:
                    return True
                
                elif add > X:
                    r -= 1
                
                else:
                    l += 1
        return False 
      
      
      
      # Zero sum special case
      
      
      
      
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final = []
        nums.sort()
        
        for i , val in enumerate(nums):
            if i > 0 and val == nums[i-1]:
                continue
                
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                sam = nums[i] + nums[l] + nums[r]
                
                if sam > 0:
                    r -= 1
                
                elif sam < 0:
                    l += 1
                
                else:
                    final.append([nums[i] , nums[l] , nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                        
        return final        
