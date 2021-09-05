'''
    lis[][0]:Petrol
    lis[][1]:Distance
'''

class Solution:
    
    #Function to find starting point where the truck can start to get through
    #the complete circle without exhausting its petrol in between.
    def tour(self,lis, n):
        #Code here
        gas = [lis[i][0] for i in range(n)]
        dist = [lis[i][1] for i in range(n)]
        
        if sum(gas) < sum(dist):
            return -1
        
        final = 0
        ref = 0
        
        for i in range(n):
            ref += gas[i] - dist[i]
            if ref < 0:
                ref = 0
                final = i+1
        return final    
