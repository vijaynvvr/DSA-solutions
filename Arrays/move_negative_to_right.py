# order of elements is not taken care here
def push_negatives(arr):
    left = 0
    right = len(arr) - 1
    while left <= right:
        if arr[left] >= 0:
            left += 1
        elif arr[right] < 0:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return arr

arr = [-1, 2, -3, 4, 5, -6, -7]
result = push_negatives(arr)
print(result)
