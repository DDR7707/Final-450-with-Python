def rev(q):
    #add code here
    l = 0
    r = len(q)
    
    def recursive(q,l,r):
        if l >= r:
            return
        q[l] , q[r] = q[r],q[l]
        recursive(q,l+1,r-1)
    recursive(q,l,r)
    return q
  

# Alternatively can use get , getleft , setleft functions  
