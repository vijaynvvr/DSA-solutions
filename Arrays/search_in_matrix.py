def matSearch(self,mat, N, M, X):
    # only if row-wise and column-wise sorted
    i = 0
    j = M-1
    while i < N and j >=0:
        if mat[i][j] == X:
            return 1
        elif mat[i][j] > X:
            j -= 1
        else:
            i += 1
    return 0

    # if row-wise and column wise and sorted and first element of an array is greater than last element of prev array
    # start = 0
    # end = N*M-1
    # while start <= end:
    #     mid = start + (end-start)//2
    #     x = mid//M
    #     y = mid%M
    #     if mat[x][y] == X:
    #         return 1
    #     if mat[x][y] > X:
    #         end = mid-1
    #     else:
    #         start = mid+1
    # return 0
