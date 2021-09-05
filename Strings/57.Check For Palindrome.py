#User function Template for python3
class Solution:
	def isPlaindrome(self, S):
		# code here
		l = 0
		r = len(S)-1
		
		while l < r:
		    if S[l] != S[r]:
		        return False
		    l += 1
		    r -= 1
		return True
