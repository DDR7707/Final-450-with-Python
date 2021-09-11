from queue import PriorityQueue
 
MAX_CHAR = 26
 
# Main Function to calculate min sum of
# squares of characters after k removals
def minStringValue(str, k):
    l = len(str) # find length of string
 
    # if K is greater than length of string
    # so reduced string will become 0
    if(k >= l):
        return 0
     
    # Else find Frequency of each
    # character and store in an array
    frequency = [0] * MAX_CHAR
    for i in range(0, l):
        frequency[ord(str[i]) - 97] += 1
 
    # Push each char frequency negative
    # into a priority_queue as the queue
    # by default is minheap
    q = PriorityQueue()
    for i in range(0, MAX_CHAR):
        q.put(-frequency[i])
 
    # Removal of K characters
    while(k > 0):
         
        # Get top element in priority_queue
        # multiply it by -1 as temp is negative
        # remove it. Increment by 1 and again
        # push into priority_queue
        temp = q.get()
        temp = temp + 1
        q.put(temp, temp)
        k = k - 1
 
    # After removal of K characters find
    # sum of squares of string Value    
    result = 0; # initialize result
    while not q.empty():
        temp = q.get()
        temp = temp * (-1)
        result += temp * temp
    return result
 
# Driver Code
if __name__ == "__main__":
    str = "abbccc"
    k = 2
    print(minStringValue(str, k))
 
    str = "aaab"
    k = 2
    print(minStringValue(str, k))
