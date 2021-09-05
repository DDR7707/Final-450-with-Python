class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            m = len(matrix)
            n = len(matrix[0])
            left = 0
            right = n-1
            ref = 0
        
            while True:
                if ref > m-1:
                    return False
                
                if target >= matrix[ref][left] and target <= matrix[ref][right]:
                    break
                
                else:
                    ref += 1
            
            arr = matrix[ref]
            def binary(arr):
                low = 0
                high = len(arr) - 1
            
                while low <= high:
                    mid = (low+high) // 2
                    if arr[mid] == target:
                        return True
                
                    elif arr[mid] > target:
                        high = mid-1
                
                    else:
                        low = mid+1
                    
                return False
        
            return binary(arr)
