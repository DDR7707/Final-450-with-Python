def solve(s):
    stack = []
    
    for i in s:
        if i == ")":
            c = 0
            while stack and c != "(":
                c += 1
            if c == 0 or c == 1:
                return 1
        else:
            stack.append(i)
    return 0

s1 = "((a+b))"
s2 = "(a+(b)/c)"
s3 = "(a+b*(c-d))"

for i in [s1 , s2 , s3]:
    print(solve(i))
    
    
    
    
    
    
    
    
    
def checkRedundancy(Str):
     
    # create a stack of characters
    st = []
 
    # Iterate through the given expression
    for ch in Str:
 
        # if current character is close
        # parenthesis ')'
        if (ch == ')'):
            top = st[-1]
            st.pop()
 
            # If immediate pop have open parenthesis
            # '(' duplicate brackets found
            flag = True
 
            while (top != '('):
 
                # Check for operators in expression
                if (top == '+' or top == '-' or
                    top == '*' or top == '/'):
                    flag = False
 
                # Fetch top element of stack
                top = st[-1]
                st.pop()
 
            # If operators not found
            if (flag == True):
                return True
 
        else:
            st.append(ch) # append open parenthesis '(',
                          # operators and operands to stack
    return False
 
# Function to check redundant brackets
def findRedundant(Str):
    ans = checkRedundancy(Str)
    if (ans == True):
        print("Yes")
    else:
        print("No")
 
# Driver code
if __name__ == '__main__':
    Str = "((a+b))"
    findRedundant(Str)
 
    Str = "(a+(b)/c)"
    findRedundant(Str)
 
    Str = "(a+b*(c-d))"
    findRedundant(Str)    
