def buyMaximumProducts(n, k, price):
 
    # Making pair of stock cost and day number
    arr = []
     
    for i in range(n):
        arr.append([i + 1, price[i]])
 
    # Sort based on the price of stock
    arr.sort(key = lambda x: x[1])
     
    # Calculating the max stocks purchased
    total_purchase = 0
    for i in range(n):
        P = min(arr[i][0], k//arr[i][1])
        total_purchase += P
        k -= (P * arr[i][1])
 
    return total_purchase
 
# Driver code
price = [ 10, 7, 19 ]
n = len(price)
k = 45
   
print(buyMaximumProducts(n, k, price))
