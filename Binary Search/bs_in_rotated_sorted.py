from pivot import findPivot
from binary_search import binarySearch

def search(arr, k):
    pivotIndex = findPivot(arr, len(arr))
    ans = -1
    if k >= arr[0] and k <= arr[pivotIndex]:
        ans = binarySearch(arr, 0, pivotIndex, k)
    else:
        ans = binarySearch(arr, pivotIndex+1, len(arr)-1, k)
    return ans

arr = [11,12,13,2,4,6,8,9,10]
target = 15
index = search(arr, target)
print(f"Index of {target} = {index}")