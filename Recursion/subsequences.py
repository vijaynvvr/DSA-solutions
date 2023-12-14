def subsequences(arr, index, output):
    if index == len(arr):
        print(output)
        return
    
    subsequences(arr, index+1, output)
    output.append(arr[index])
    subsequences(arr, index+1, output)
    output.pop()

arr = [3, 1, 4]
output = []
index = 0
subsequences(arr, index, output)


