def solve(n , s , m):
    if m > n or ((m*7) > (n*6) and s > 6):
        return -1
    
    final = (m*s) // n
    if (m*s) % n != 0:
        final += 1
    
        
    return int(final)

print(solve(10 , 10 , 2))   
