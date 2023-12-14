# [3, 1, 4, 1, 5]
# find unique pairs in arr (arr[i], arr[j])
# with difference of elements pair is k,  abs(arr[j]-arr[i]) = k
# contraints: i!=j, 0 <= i,j < nums.length
# ouput: 2 {(1,3), (3,5)}

# --------------------------------------------------------------
# approach-1 (bruteforce)
# check condition {abs(arr[j]-arr[i]) = k} for all possible pairs in the array
# for i in (0->n-1) {
# for j in (i+1->n-1) {condition, body}
# }
# T.C: O(n^2)

# --------------------------------------------------------------
# approach-2 (sorting)
# 2.1
# 2-pointer approach
# i=0, j=1
# while j < len(arr):
#   if abs(arr[j]-arr[i]) = k :ans++, i++, j++
#   elif abs(arr[j]-arr[i]) > k : i++ (since diff is greater than k in sorted array, move i forward to make diff less)
#   else/(elif abs(arr[j]-arr[i]) < k) : j++ (since diff is lesser than k in sorted array, move j forward to make diff more)
# T.C: O(nlog(n))

# 2.2
# binary search
# after sorting, i = 0, for each element at i, apply binary search from i+1 to len(arr)
# condition: arr[mid] = arr[i]+k 
# T.C: O(nlog(n))


def findPairs(self, nums: list[int], k: int) -> int:
    i = 0; j = 1
    nums.sort()
    ans = set()

    # 2-pointer
    # while j < len(nums):
    #     if i == j:
    #         j += 1
    #         continue
    #     if nums[j] - nums[i] == k:
    #         ans.add((nums[i], nums[j]))
    #         i += 1; j +=1
    #     elif nums[j] - nums[i] < k:
    #         j += 1
    #     else:
    #         i += 1
    # return len(ans)

    # binary search
    for i in range(len(nums)):
        found = self.bin_search(nums, i+1, len(nums)-1, k+nums[i])
        if found != -1:
            ans.add((nums[i], nums[found]))
    return len(ans)



def bin_search(self, arr, start, end, key):
    while start <= end:
        mid = start + (end-start)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            start = mid+1
        else:
            end = mid-1
    return -1