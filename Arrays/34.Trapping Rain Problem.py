class Solution:
    def trappingWater(self, arr,n):
        #Code here
        i = 1
        j = n-2
        final = 0
        l_max = arr[0]
        r_max = arr[-1]
        
        while i <= j:
            if l_max < r_max:
                final += max(0 , l_max - arr[i])
                l_max = max(l_max , arr[i])
                i += 1
            else:
                final += max(0 , r_max - arr[j])
                r_max = max(r_max , arr[j])
                j -= 1
        return final  
