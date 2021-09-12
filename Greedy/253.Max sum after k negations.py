class Solution:
    def maximizeSum(self, a, n, k):
        # Your code goes here
        import heapq
        heapq.heapify(a)
        for i in range(k):
            temp = heapq.heappop(a)
            heapq.heappush(a , -temp)
        
        return sum(a) 
