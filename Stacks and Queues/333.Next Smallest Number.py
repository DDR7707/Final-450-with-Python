class Solution:
	# @param A : list of integers
	# @return a list of integers
	def nextSmallest(self, A):
        stack = []
        final = [-1]*len(A)

        for i in range(len(A)-1 , -1 , -1):
            while stack and stack[-1] > A[i]:
                stack.pop()

            if stack:
                final[i] = stack[-1]

            stack.append(A[i])
        return final 
