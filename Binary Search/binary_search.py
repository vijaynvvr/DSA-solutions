def binarySearch(arr, n, k):
    start = 0
    end = n-1
    while start <= end:
        mid = start + (end-start)//2
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            end = mid-1
        else:
            start = mid+1
    return -1