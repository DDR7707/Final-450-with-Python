class Solution:
    def smallestSubWithSum(self, a, n, x):
        # Your code goes here 
        que = []
        add = 0
        final = n
        for i in range(n):
            que.append(a[i])
            add += a[i]
            while que and add > x:
                top = que[0]
                if x < add-top:
                    que.pop(0)
                    add -= top
                else:
                    break
                    
            if add > x:
                final = min(final , len(que))
        return final  
                
