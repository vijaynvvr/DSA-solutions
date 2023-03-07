# Intuition: array (size-n) elements belonging to [1,n] range can be solved by playing with indices
# just like 3rd and 4th approaches

def findDuplicate(nums: list[int]) -> int:
    # O(n^2), O(1)
    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         if nums[i] == nums[j]:
    #             return nums[i]

    # O(nlogn), O(n)
    # nums.sort()
    # for i in range(len(nums)-1):
    #     if nums[i] == nums[i+1]:
    #         return nums[i]

    # O(n), O(1)
    # ans = -1
    # for i in range(len(nums)):
    #     index = abs(nums[i])
    #     if nums[index] < 0:
    #         ans = index
    #         break
    #     nums[index] *= -1
    # return ans

    # O(n), O(1)
    while nums[0] != nums[nums[0]]:
        index = nums[0]
        nums[0], nums[index] = nums[index], nums[0]
    return nums[0]

# solution without updating the original array with O(n) T.C and O(1) S.C not yet added