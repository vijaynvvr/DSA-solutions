def arraySortedOrNot(self, arr, n):
    isSorted = True
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            isSorted = False
            break
    return isSorted