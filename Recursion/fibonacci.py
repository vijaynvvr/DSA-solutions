def fibonacci(n):
    if n == 0 or n == 1: return n
    return fibonacci(n-1) + fibonacci(n-2)

n = 10
ans = fibonacci(n)
# print(ans)

for i in range(5):
    print(fibonacci(i), end=" ")