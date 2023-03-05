def pushZerosToEnd(self,arr, n):
    k = 0
    while k < n:
        if arr[k] == 0:
            break
        k += 1
    start = k
    next = k+1
    while next < n:
        if arr[next] != 0:
            arr[start], arr[next] = arr[next], arr[start]
            start += 1
        next += 1