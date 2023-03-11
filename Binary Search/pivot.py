def findPivot(arr, n):
    s = 0
    e = n-1
    while s <= e:
        mid = s + (e-s)//2
        if s == e:
            return s
        if mid <= e and arr[mid] > arr[mid+1]:
            return mid
        if mid-1 >= s and arr[mid-1] > arr[mid]:
            return mid-1
        if arr[s] > arr[mid]:
            e = mid-1
        else:
            s = mid+1
    return -1
        
if __name__ == "__main__":
    arr = [2,4,6,8,9,10]
    p = findPivot(arr, len(arr))
    print(p, arr[p], sep=" ")