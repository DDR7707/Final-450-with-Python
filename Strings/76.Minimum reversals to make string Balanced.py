def countRev (s):
    # your code here
    if len(s)%2 != 0:
        return -1
        
    stack = []
    left = 0
    right = 0
    for i in s:
        if i == "{":
            stack.append(i)
            right += 1
        else:
            if not stack or stack[-1] == "}":
                stack.append(i)
                left += 1
            else:
                stack.pop()
                right -= 1
    return (left+1) // 2 + (right+1) // 2 
