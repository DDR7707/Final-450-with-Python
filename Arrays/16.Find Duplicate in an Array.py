class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow    






# Modifying array
def printRepeating(arr, size):
 
    print("The repeating elements are: ")
 
    for i in range(0, size):
 
        if arr[abs(arr[i])] >= 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]
        else:
            print(abs(arr[i]), end=" ")
 
 
# Driver code
arr = [1, 2, 3, 1, 3, 6, 6]
arr_size = len(arr)
 
printRepeating(arr, arr_size)









# Only one repeated number in array
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        x = (n*(n+1)) // 2 - sum(nums)
        add = 0
        for i in nums:
            add += i*i
            
        y = n*(n+1)*(2*n+1) // 6 - add
        z = y // x
        return (z-x) // 2
