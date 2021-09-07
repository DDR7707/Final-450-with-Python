class Solution:
	def FirstNonRepeating(self, A):
		# Code here
		look = [0]*26
		final = ""
		que = []
		
		for i in A:
		    look[ord(i)-ord("a")] += 1
		    que.append(i)
		    while que:
		        if look[ord(que[0])-ord("a")] > 1:
		            que.pop(0)
		        else:
		            final += que[0]
		            break
		    if not que:
		        final += "#"
		        
		return final 
