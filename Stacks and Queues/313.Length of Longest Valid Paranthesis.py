class Solution:
    def findMaxLen(ob, S):
        # code here 
        left = 0
        right = 0
        final = 0
        for i in S:
            if i == "(":
                left += 1
            else:
                right += 1
            
            if left == right:
                final = max(final , 2*left)
            
            elif right > left:
                left = right = 0
        
        left = right = 0
        
        for i in range(len(S)-1 , -1 , -1):
            if S[i] == "(":
                left += 1
            else:
                right += 1
            
            if left == right:
                final = max(final , 2*left)
            elif left > right:
                right = left = 0
        
        return final 
