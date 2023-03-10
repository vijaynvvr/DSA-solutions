# find the odd occurring element in an array
# all elements occur even number of times except one element
# all repeating occurrence of elements appear in pairs
# ex: [1,1,2,2,3,3,4,4,3,600,600,4,4,2,2]

def oddOccurrence(arr, n):
    s = 0
    e = n-1
    while s <= e:
        m = s + (e-s)//2
        if s == e:
            return m
        if m%2 == 0:
            if arr[m] == arr[m+1]:
                s = m+2
            else:
                e = m
            # if arr[m] == arr[m-1]:
            #     e = m-2
            # else:
            #     s = m
        else:
            if arr[m] == arr[m-1]:
                s = m+1
            else:
                e = m-1
            # if arr[m] == arr[m+1]:
            #     e = m-1
            # else:
            #     s = m+1

arr = [1,1,2,2,4,4,3,600,600,4,4,2,2]
index = oddOccurrence(arr, len(arr))
print(f"Index = {index} and value = {arr[index]}")