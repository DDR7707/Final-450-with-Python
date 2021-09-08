def isSubset( a1, a2, n, m):
    if len(set(a2)-set(a1)) == 0:
        return "Yes"
    return "No" 
