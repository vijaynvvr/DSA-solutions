def binarySearch(arr, n, k):
    start = 0
    end = n-1
    while start <= end:
        mid = start + (end-start)//2
        if arr[mid] == k:
            return mid
        if arr[mid-1] >= start and arr[mid-1] == k:
            return mid-1
        if arr[mid+1] <= end and arr[mid+1] == k:
            return mid+1
        elif arr[mid] > k:
            end = mid-2
        else:
            start = mid+2
    return -1

# In a sorted array, if an element at ith position is at (i-1,i,i+1) positions then it is a nearly sorted array
arr = [10,3,40,20,50,80,70]
index = binarySearch(arr, len(arr), 50)
print(index)
