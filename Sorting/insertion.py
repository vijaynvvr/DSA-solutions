def insertionSort(arr, n):
    for i in range(1,n):
        value = arr[i]
        j = i-1
        while j >= 0:
            if value < arr[j]:
                arr[j+1] = arr[j]
            else:
                break
            j -= 1
        arr[j+1] = value
    return arr

arr = [2,5,3,8,6,1,9]
print(insertionSort(arr, len(arr)))