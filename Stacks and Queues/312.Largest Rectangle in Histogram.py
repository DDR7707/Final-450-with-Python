def getMaxArea(histogram):
        final = 0
        stack = []
        
        for i in range(len(histogram)):
            if len(stack) == 0 or histogram[stack[-1]] < histogram[i]:
                stack.append(i)
            
            else:
                while stack and histogram[stack[-1]] > histogram[i]:
                    top = stack.pop()
                    if stack:
                        area = histogram[top]*(i-stack[-1]-1)
                    else:
                        area = histogram[top]*(i)
                    
                    final = max(final , area)
                
                stack.append(i)  
        
        while stack:
            top = stack.pop()
            if stack:
                area = histogram[top]*(i-stack[-1]-1)
            else:
                area = histogram[top]*(i)
            
            final = max(final , area)
        
        return final    

print(getMaxArea([7 , 2 , 8 , 9 , 1 , 3 , 6 , 5])) 
