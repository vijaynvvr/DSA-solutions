def matSearch(mat, n, m, k):
    # only if row-wise and column-wise sorted
    # i = 0
    # j = m-1
    # while i < n and j >=0:
    #     if mat[i][j] == k:
    #         return 1
    #     elif mat[i][j] > k:
    #         j -= 1
    #     else:
    #         i += 1
    # return 0

    # if row-wise and column wise and sorted and first element of an array is greater than last element of prev array
    start = 0
    end = n*m-1
    while start <= end:
        mid = start + (end-start)//2
        x = mid//m
        y = mid%m
        if mat[x][y] == k:
            return 1
        if mat[x][y] > k:
            end = mid-1
        else:
            start = mid+1
    return 0
