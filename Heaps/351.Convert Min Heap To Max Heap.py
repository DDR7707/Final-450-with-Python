def MaxHeapify(arr, i, n):
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i
    if l < n and arr[l] > arr[i]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        MaxHeapify(arr, largest, n)
 
# This function basically builds max heap
def convertMaxHeap(arr, n):
     
    # Start from bottommost and rightmost
    # internal mode and heapify all
    # internal modes in bottom up way
    for i in range(int((n - 2) / 2), -1, -1):
        MaxHeapify(arr, i, n)
 
# A utility function to print a
# given array of given size
def printArray(arr, size):
    for i in range(size):
        print(arr[i], end = " ")
    print()
 
# Driver Code
if __name__ == '__main__':
     
    # array representing Min Heap
    arr = [3, 5, 9, 6, 8, 20, 10, 12, 18, 9]
    n = len(arr)
 
    print("Min Heap array : ")
    printArray(arr, n)
 
    convertMaxHeap(arr, n)
 
    print("Max Heap array : ")
    printArray(arr, n)
