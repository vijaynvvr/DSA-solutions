def remove_duplicate(self, A, N):
    i = 0
    # for j in range(1, N):
    #     if A[i] != A[j]:
    #         i += 1
    #         A[i] = A[j]
    # return i+1
    j = 1
    while True:
        if j == len(A):
            break
        if A[i] == A[j]:
            A.pop(j)
        else:
            i = j
            j += 1
    return len(A)
