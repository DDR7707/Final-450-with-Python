class Solution:

    def candyStore(self, candies,N,K):
        # code here
        arr1 = sorted(candies)
        arr2 = arr1[::-1]
        final = []
        temp = 0
        while arr1:
            temp += arr1.pop(0)
            for i in range(K):
                if not arr1:
                    break
                arr1.pop()
        final.append(temp)
        temp = 0
        while arr2:
            temp += arr2.pop(0)
            for i in range(K):
                if not arr2:
                    break
                arr2.pop()
        final.append(temp)      
        return final
