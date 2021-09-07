class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        arr = list(zip(start , end))
        arr.sort(key = lambda x : x[1])
        final = 1
        ref = arr[0][1]
        
        for i in range(len(start)):
            if arr[i][0] > ref:
                final += 1
                ref = arr[i][1]
        return final   
