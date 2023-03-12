def bubbleSort(arr, n):
    for i in range(1,n):
        not_swapped = True
        for j in range(n-i):
            if arr[j] > arr[j+1]:
                not_swapped = False
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if not_swapped:
            break
    return arr

# arr = [2,5,3,8,6,1,9]
# arr = [1,2,3,5,6,8,9]
arr = [9,8,6,5,3,2,1]
print(bubbleSort(arr, len(arr)))