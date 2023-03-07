arr = [[1,2,3,4], 
       [5,6,7,8], 
       [9,10,11,12]]
n = len(arr)
m = len(arr[0])
for i in range(m):
    if i%2==0:
        for j in range(n):
            print(arr[j][i], end=" ")
    else:
        for j in range(n-1, -1, -1):
            print(arr[j][i], end=" ")
