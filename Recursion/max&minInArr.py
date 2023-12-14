maxNum = float('-inf')
minNum = float('inf')

# def maxInArr(arr, index):
#     if index >= len(arr): return
#     global maxNum
#     maxNum = max(maxNum, arr[index])
#     maxInArr(arr, index+1)

# def minInArr(arr, index):
#     if index >= len(arr): return
#     global minNum
#     minNum = min(minNum, arr[index])
#     minInArr(arr, index+1)

def maxInArr(arr, index, maxNum):
    '''without using global variable'''
    if index >= len(arr): return maxNum
    maxNum = max(maxNum, arr[index])
    return maxInArr(arr, index+1, maxNum)

def minInArr(arr, index, minNum):
    '''without using global variable'''
    if index >= len(arr): return minNum
    minNum = min(minNum, arr[index])
    return minInArr(arr, index+1, minNum)

arr = [4,6,2,6,1,8,2,9]
index = 0
print(maxInArr(arr, index, maxNum))
print(minInArr(arr, index, minNum))
# print(maxNum)
# print(minNum)


# how to store ans in recursive problems
# 1. maintain gloabal variable and access in recursive function using 'global' keyword
# 2. parameterized recursion: pass ans variable as parameter by reference and store updated ans
# note: since we can't send reference by variable in python, store the ans as a single element in list
# 3. functional recursion: return the ans at base case and handle the recursive condition appropriately