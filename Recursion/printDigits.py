def printDigitsReverse(n):
    if n == 0: return
    print(n%10, end=" ")
    printDigitsReverse(n//10)

def printDigits(n):
    if n == 0: return
    printDigits(n//10)
    print(n%10, end=" ")


printDigits(6371187)
printDigitsReverse(6371187)