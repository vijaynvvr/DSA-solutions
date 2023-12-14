def checkSorted(arr, index):
    if index >= len(arr)-1: return True
    if arr[index] > arr[index + 1]: return False
    return checkSorted(arr, index + 1)


arr1 = [3,2,5,6,2,1,6]
arr2 = [1,3,4,5,7,90]
index = 0
print(checkSorted(arr1, index))
print(checkSorted(arr2, index))