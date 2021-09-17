class Solution:
    
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,a,n):
        # code here
        final = [a[0]]
        def ceil(arr , k):
            ans = 0
            low = 0
            high = len(arr)-1
            
            while low <= high:
                mid = (low+high) // 2
                if k > arr[mid]:
                    low = mid+1
                else:
                    ans = mid
                    high = mid-1
            return ans
        
        for i in range(1 , len(a)):
            if final[-1] < a[i]:
                final.append(a[i])
            
            else:
                temp = ceil(final , a[i])
                final[temp] = a[i]
        
        return len(final)  
