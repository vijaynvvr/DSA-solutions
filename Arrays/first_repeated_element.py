def firstRepeated(self,arr, n):    
    #arr : given array
    #n : size of the array
    
    # hash = dict()
    # for i in range(n):
    #     if hash.get(arr[i]):
    #         hash[arr[i]] += 1
    #     else:
    #         hash[arr[i]] = 1
    # for i in range(n):
    #     if hash[arr[i]] > 1:
    #         return i+1
    # return -1
    
    # using array as hash
    hash = [0 for i in range(max(arr)+1)]
    for i in range(n):
        hash[arr[i]] += 1
    for i in range(n):
        if hash[arr[i]] > 1:
            return i+1
    return -1