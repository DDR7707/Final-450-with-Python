import numpy as np
class GFG:
     
    def MaxSumDifference(a,n):
        # sort the original array
        # so that we can retrieve
        # the large elements from
        # the end of array elements
        np.sort(a);
     
        # In this loop first we will
        # insert one smallest element
        # not entered till that time
        # in final sequence and then
        # enter a highest element(not
        # entered till that time) in
        # final sequence so that we
        # have large difference value.
        # This process is repeated till
        # all array has completely
        # entered in sequence. Here,
        # we have loop till n/2 because
        # we are inserting two elements
        # at a time in loop.
        j = 0
        finalSequence = [0 for x in range(n)]
        for i in range(0, int(n / 2)):
            finalSequence[j] = a[i]
            finalSequence[j + 1] = a[n - i - 1]
            j = j + 2
 
        # If there are odd elements, push the
        # middle element at the end.
        if (n % 2 != 0):
           finalSequence[n-1] = a[n//2 + 1]
 
        # variable to store the
        # maximum sum of absolute
        # difference
        MaximumSum = 0
     
        # In this loop absolute
        # difference of elements
        # for the final sequence
        # is calculated.
        for i in range(0, n - 1):
            MaximumSum = (MaximumSum +
                          abs(finalSequence[i] -
                              finalSequence[i + 1]))
     
        # absolute difference of last
        # element and 1st element
        MaximumSum = (MaximumSum +
                      abs(finalSequence[n - 1] -
                         finalSequence[0]));
     
        # return the value
        print (MaximumSum)
     
# Driver Code
a = [ 1, 2, 4, 8 ]
n = len(a)
GFG.MaxSumDifference(a, n);
