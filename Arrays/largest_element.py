def largest( arr, n):
    maxnum = arr[0]
    for num in arr:
        if maxnum < num:
            maxnum = num
    return maxnum
