def selectionSort(arr, n):
    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

arr = [2,5,3,8,6,1,9]
print(selectionSort(arr, len(arr)))