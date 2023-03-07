def commonElements (self,A, B, C, n1, n2, n3):
    # your code here
    i = j = k = 0
    ans = []
    while i < n1 and j < n2 and k < n3:
        if A[i] == B[j] and B[j] == C[k]:
            if len(ans) == 0 or ans[-1] != A[i]:
                ans.append(A[i])
            i += 1
            j += 1
            k += 1
        elif A[i] < B[j]:
            i += 1
        elif B[j] < C[k]:
            j += 1
        else:
            k += 1
    return ans