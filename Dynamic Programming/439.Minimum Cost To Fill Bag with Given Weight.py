INF = 1000000
 
# cost[] initial cost array including unavailable packet
# W capacity of bag
def MinimumCost(cost, n, W):
 
    # val[] and wt[] arrays
    # val[] array to store cost of 'i' kg packet of orange
    # wt[] array weight of packet of orange
    val = list()
    wt= list()
 
    # traverse the original cost[] array and skip
    # unavailable packets and make val[] and wt[]
    # array. size variable tells the available number
    # of distinct weighted packets.
    size = 0
    for i in range(n):
        if (cost[i] != -1):
            val.append(cost[i])
            wt.append(i+1)
            size += 1
 
    n = size
    min_cost = [[0 for i in range(W+1)] for j in range(n+1)]
 
    # fill 0th row with infinity
    for i in range(W+1):
        min_cost[0][i] = INF
 
    # fill 0th column with 0
    for i in range(1, n+1):
        min_cost[i][0] = 0
 
    # now check for each weight one by one and fill the
    # matrix according to the condition
    for i in range(1, n+1):
        for j in range(1, W+1):
            # wt[i-1]>j means capacity of bag is
            # less than weight of item
            if (wt[i-1] > j):
                min_cost[i][j] = min_cost[i-1][j]
 
            # here we check we get minimum cost either
            # by including it or excluding it
            else:
                min_cost[i][j] = min(min_cost[i-1][j],
                    min_cost[i][j-wt[i-1]] + val[i-1])
 
    # exactly weight W can not be made by given weights
    if(min_cost[n][W] == INF):
        return -1
    else:
        return min_cost[n][W]
 
# Driver program to run the test case
cost = [1, 2, 3, 4, 5]
W = 5
n = len(cost)
 
print(MinimumCost(cost, n, W))
