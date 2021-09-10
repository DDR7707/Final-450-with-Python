def heapify(arr , n , i):
    largest = i
    left = 2*i+1
    right = 2*i+2

    while left < n and arr[left] > arr[largest]:
        largest = left

    while right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[largest] , arr[i] = arr[i] , arr[largest]
        heapify(arr , n , largest)


def insert(arr , k):
    n = len(arr)
    arr.append(k)
    i = n
    while i > 0:
        if arr[i//2] < arr[i]:
            arr[i//2] , arr[i] = arr[i] , arr[i//2]
        i = i//2

def delete(arr):
    i = len(arr)-1
    arr[0] , arr[i] = arr[i] , arr[0]
    arr.pop()
    for i in range(len(arr//2) , -1 , -1):
        heapify(arr , len(arr) , i)


    pass

def heapsort(arr):
    final = []

    # Heapify
    for i in range((len(arr) // 2) , -1 , -1):
        heapify(arr , len(arr) , i)
    

    # Delete from the top and heapify simultaniously

    for i in range(len(arr) - 1, -1 , -1):
        arr[0] , arr[i] = arr[i] , arr[0]
        final.append(arr.pop())

        heapify(arr , i , 0)

    print(final)


print(heapsort([ 1, 3, 5, 4, 6, 13, 
             10, 9, 8, 15, 17 ]))
