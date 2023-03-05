def search(self, A, N):
    xor = 0
    for num in A:
        xor = xor^num
    return xor
