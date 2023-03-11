def binarySearch(arr, s, e, k):
    start = s
    end = e
    while start <= end:
        mid = start + (end-start)//2
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            end = mid-1
        else:
            start = mid+1
    return -1