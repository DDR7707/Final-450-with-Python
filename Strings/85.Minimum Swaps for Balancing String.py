# Normal Swaps
class Solution:
    def minimumNumberOfSwaps(self,S):
        # code here 
        c = 0
        final = 0
        for i in S:
            if i == "[":
                c -= 1
            else:
                c += 1
            final = max(final , c) 
        return (final + 1)  // 2 
      
    
# Adjacent Swaps      
       
def swapCount(s):
     
    chars = s
     
    # Stores total number of left and 
    # right brackets encountered
    countLeft = 0
    countRight = 0
     
    # Swap stores the number of swaps 
    # required imbalance maintains the
    # number of imbalance pair
    swap = 0
    imbalance = 0;
     
    for i in range(len(chars)):
        if chars[i] == '[':
             
            # Increment count of left bracket
            countLeft += 1
             
            if imbalance > 0:
                 
                # Swaps count is last swap
                # count + total number
                # imbalanced brackets
                swap += imbalance
                 
                # Imbalance decremented by 1
                # as it solved only one
                # imbalance of left and right
                imbalance -= 1
                 
        elif chars[i] == ']':
             
            # Increment count of right bracket
            countRight += 1
             
            # Imbalance is reset to current
            # difference between left and
            # right brackets
            imbalance = (countRight - countLeft)
 
    return swap
 
# Driver code
s = "[]][][";
print(swapCount(s))
 
s = "[[][]]";
print(swapCount(s))



# Reversals
'''
First remove all balanced with help of stacks
then return ceil(m/2) + ceil(n/2)
where m = left brackets , n = right brackets

'''
