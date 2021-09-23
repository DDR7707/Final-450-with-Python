def ispar(x):
    # code here
    look = {")" : "(" , "]" : "[" , "}" : "{"}
    stack = []
    for i in x:
        if i in look.values():
            stack.append(i)
            
        elif  i in look.keys():
            if len(stack) == 0:
                return False
            elif stack[-1] != look[i]:
                return False
            else:
                stack.pop()
    return True  if len(stack) == 0 else False
