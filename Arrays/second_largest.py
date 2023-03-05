def print2largest(self,arr, n):
    maxNum = secMaxNum = -1
    for num in arr:
        if num > maxNum:
            secMaxNum = maxNum
            maxNum = num
        elif num > secMaxNum and num != maxNum:
            secMaxNum = num
    return secMaxNum