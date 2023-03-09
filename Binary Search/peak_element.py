def peakElement(arr, n):
    start = 0
    end = n-1
    while start < end:
        mid = start + (end-start)//2
        if arr[mid] < arr[mid+1]:
            start = mid+1
        else:
            end = mid
    return end

arr = [2,3,4,6,7,8,9,5,3,1,0]
peak = peakElement(arr,len(arr))
print(peak)