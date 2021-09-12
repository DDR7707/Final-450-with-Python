class Solution:
    #Function to return the minimum cost of connecting the ropes.
    def minCost(self,arr,n) :
    
        # code here
        import heapq
        heapq.heapify(arr)
        
        final = 0
        
        while len(arr) > 1:
            one = heapq.heappop(arr)
            two = heapq.heappop(arr)
            
            temp = one+two
            final += temp
            heapq.heappush(arr , temp)
        
        return final    
