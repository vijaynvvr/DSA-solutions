# find k closest elements w.r.t x in a sorted array

# ----------------------------------------------------
# approach-1 (bruteforce)

# find another sorted array with sorting condition as difference (arr[i]-x)
# return first k elements from the newly sorted array
# T.C: O(n^2)

# ----------------------------------------------------
# approach-2 (2-pointer)

# 2.1 - window contraction:
# l = 0, h = arr(len)-1
# until h-l+1 != k or h-l >= k
# if arr[l] < arr[h]: h--
# if arr[l] > arr[h]: l++
# T.C: O(n-k)

# 2.2 - binary search & window expansion
# find lower bound - lb or element in arr just less than or equal to x
# h = lb
# l = h-1
# if arr[l] > arr[h]: h--
# if arr[l] < arr[h]: l++
# T.C: O(nlog(n))

def lowerbound(arr, x):
    start = 0; end = len(arr)-1; ans = -1
    while start <= end:
        mid = start + (end-start)//2
        if arr[mid] <= x:
            ans = mid
            start = mid+1
        else:
            end = mid-1
        # if arr[mid] >= x:
        #         ans = mid
        #         end = mid-1
        # elif x > arr[mid]:
        #     start = mid+1
        # else:
        #     end = mid-1
    return arr[ans]

print(lowerbound([1,3,4,5,6,7,9,11,15,19], 14))