# return missing num in array containing duplicates, nums[i] E [1,n], len(nums) = n
def findMissing(nums):

    # visited method:
    # for i in range(len(nums)):
    #     index = abs(nums[i])
    #     if nums[index-1] > 0:
    #         nums[index-1] *= -1
    # for i in range(len(nums)):
    #     if nums[i] > 0:
    #         print(i+1,end=" ")

    # sorting + swapping method:
    i = 0
    while i < len(nums):
        index = nums[i]-1
        if nums[i] != nums[index]:
            nums[i], nums[index] = nums[index], nums[i]
        else:
            i += 1
    for i in range(len(nums)):
        if nums[i] != i+1:
            print(i+1, end=" ")
    print()

a = [1,3,5,3,4]
findMissing(a)
b = [1,3,5,3,5]
findMissing(b)

