def searchInArr(arr, index, key):
    if index >= len(arr): return False
    if key == arr[index]: return True
    return searchInArr(arr, index+1, key)

def indexInArr(arr, index, key):
    '''returns first occurrence of key in arr'''
    if index >= len(arr): return -1
    if key == arr[index]: return index
    return indexInArr(arr, index+1, key)

def freqencyInArr(arr, index, key, count):
    if index >= len(arr): return count
    if key == arr[index]: count += 1
    return freqencyInArr(arr, index+1, key, count)

key = 10
index = 0
arr = [6,3,1,10,9,4,3,10,4]
count = 0
ans1 = searchInArr(arr, index, key)
ans2 = indexInArr(arr, index, key)
ans3 = freqencyInArr(arr, index, key, count)
print(ans1, ans2, ans3)