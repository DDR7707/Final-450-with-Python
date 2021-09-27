# Python 3 program to
# maximize the number
# of segments of length
# p, q and r

# Function that returns
# the maximum number
# of segments possible


def findMaximum(l, p, q, r):

	# Array to store the cut
	# at each length
	# All values with -1
	dp = [-1]*(l + 1)

	# if length of rod is 0 then
	# total cuts will be 0
	# so, initialize the dp[0] with 0
	dp[0] = 0

	for i in range(l+1):

		# if certain length is not
		# possible
		if (dp[i] == -1):
			continue

		# if a segment of p is possible
		if (i + p <= l):
			dp[i + p] = (max(dp[i + p],
							dp[i] + 1))

		# if a segment of q is possible
		if (i + q <= l):
			dp[i + q] = (max(dp[i + q],
							dp[i] + 1))

		# if a segment of r is possible
		if (i + r <= l):
			dp[i + r] = (max(dp[i + r],
							dp[i] + 1))

	# if no segment can be cut then return 0
	if dp[l] == -1:
		dp[l] = 0
	# return value corresponding
	# to length l
	return dp[l]


# Driver Code
if __name__ == "__main__":
	l = 11
	p = 2
	q = 3
	r = 5

	# Calling Function
	ans = findMaximum(l, p, q, r)
	print(ans)

# This code is contributed by
# ChitraNayal
