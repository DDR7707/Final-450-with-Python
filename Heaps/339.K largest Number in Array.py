class Solution:

	def kLargest(self,arr, n, k):
		# code here
        heap = []
        size = 0
        
        for i in arr:
            heapq.heappush(heap , i)
            size += 1
            
            if size > k:
                heapq.heappop(heap)
                size -= 1
        return heap[0] 
