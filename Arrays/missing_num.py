def missingNumber( A, N):
    sum = 0
    actual_sum = N*(N+1)/2
    for num in A:
        sum += num
    return int(actual_sum - sum)