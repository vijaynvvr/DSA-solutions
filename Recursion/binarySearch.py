def binarySearch(arr, start, end, key):
    mid = start + (end - start)//2
    if key == arr[mid]: return mid
    if start > end: return -1
    else:
        if key < arr[mid]: return binarySearch(arr, start, mid-1, key)
        else: return binarySearch(arr, mid+1, end, key)

arr = [1,3,4,5,7,90]
key = 90
start = 0
end = len(arr)-1
ans = binarySearch(arr, start, end, key)
print(ans)