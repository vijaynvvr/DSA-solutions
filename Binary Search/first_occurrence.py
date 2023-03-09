def firstOccurrence(arr, n, k):
    start = 0
    end = n-1
    ans = -1
    while start <= end:
        mid = start + (end-start)//2
        if arr[mid] >= k:
            ans = mid
            end = mid-1
        else:
            start = mid+1
    return ans

if __name__ == "__main__":
    arr = [1,2,4,5,5,5,6,7,7]
    index = firstOccurrence(arr, len(arr), 5)
    print(index)