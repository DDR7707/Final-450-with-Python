def flip( ch):
    return '1' if (ch == '0') else '0'
 
# Utility method to get minimum flips when
# alternate string starts with expected char
def getFlipWithStartingCharcter(str, expected):
 
    flipCount = 0
    for i in range(len( str)):
         
        # if current character is not expected,
        # increase flip count
        if (str[i] != expected):
            flipCount += 1
 
        # flip expected character each time
        expected = flip(expected)
    return flipCount
 
# method return minimum flip to make binary
# string alternate
def minFlipToMakeStringAlternate(str):
 
    # return minimum of following two
    # 1) flips when alternate string starts with 0
    # 2) flips when alternate string starts with 1
    return min(getFlipWithStartingCharcter(str, '0'),
            getFlipWithStartingCharcter(str, '1'))
 
# Driver code to test above method
if __name__ == "__main__":
     
    str = "0001010111"
    print(minFlipToMakeStringAlternate(str))
