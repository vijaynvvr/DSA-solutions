def printArr(arr, index):
    if index >= len(arr): return
    print(arr[index], end=" ")
    printArr(arr, index+1)


arr = [3,2,5,6,2,1,6]
index = 0
printArr(arr, index)