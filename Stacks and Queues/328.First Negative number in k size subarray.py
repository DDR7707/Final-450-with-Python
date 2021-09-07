def printFirstNegativeInteger( A, N, K):
    # code here
    final = []
    que = []
    
    for i in range(K):
        if A[i] < 0:
            que.insert(0 , i)
    if que:
        final.append(A[que[-1]])
    else:
        final.append(0)
        
    for i in range(K , N):
        while que and que[-1] <= i-K:
            que.pop()
        
        if A[i] < 0:
            que.insert(0 , i)
        if que:
            final.append(A[que[-1]])
        else:
            final.append(0)
    
    return final  
