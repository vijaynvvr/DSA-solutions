def printCount(n):
    if n <= 0: return
    print(n)
    printCount(n-1)

def printCountReverse(n):
    if n <= 0: return
    printCountReverse(n-1)
    print(n)

n = 10
# printCount(n)
printCountReverse(n)