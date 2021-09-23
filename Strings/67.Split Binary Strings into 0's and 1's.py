def maxSubStr(str, n):
     
    # To store the count of 0s and 1s
    count0 = 0
    count1 = 0
     
    # To store the count of maximum
    # substrings str can be divided into
    cnt = 0
     
    for i in range(n):
        if str[i] == '0':
            count0 += 1
        else:
            count1 += 1
             
        if count0 == count1:
            cnt += 1
 
# It is not possible to
    # split the string
    if cnt == 0:
        return -1
             
    return cnt
 
# Driver code
str = "0100110101"
n = len(str)
print(maxSubStr(str, n))
