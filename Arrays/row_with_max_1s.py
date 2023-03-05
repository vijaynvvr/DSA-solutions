# Matrix with each row sorted containing 0s and 1s
def rowWithMax1s(self,arr, n, m):
    for i in range(m):
        for j in range(n):
            if arr[j][i]:
                return j
    return -1
