def sort012(self,arr,n):
    # 1. by sorting
    # arr.sort()
    
    # 2. by counting
    # zeroes = ones = twos = 0
    # for num in arr:
    #     if num == 0:
    #         zeroes += 1
    #     elif num == 1:
    #         ones += 1
    #     else:
    #         twos += 1
    # count = 0
    # while zeroes:
    #     arr[count] = 0
    #     zeroes -= 1
    #     count += 1
    # while ones:
    #     arr[count] = 1
    #     ones -= 1
    #     count += 1
    # while twos:
    #     arr[count] = 2
    #     twos -= 1
    #     count += 1
        
    # 3. 3 pointers
    start = i = 0; end = n-1
    while i <= end:
        if arr[i] == 0:
            arr[start], arr[i] = arr[i], arr[start]
            start += 1
            i += 1
        elif arr[i] == 1:
            i += 1
        else:
            arr[end], arr[i] = arr[i], arr[end]
            end -= 1
