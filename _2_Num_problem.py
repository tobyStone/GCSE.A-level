
nums = [-1, 3, 3, 4, -4]
target = 0

def two_sums(nums):
    for i in nums:
        for j in range(i + 1, len(nums) -1):
            if nums[i] + nums[j] == target:
                print("Summed to 0")
                return True
    return False
    

#def two_sums(nums):
#    nums.sort()
#    left, right = 0, len(nums)-1
#    while left < right:
#        total = nums[left] + nums[right]
#        if total == target:
#            print("Summed to 0")
#            return True
#        else:
#            left = left + 1
#            right = right -1
#        return False   
    

#def two_sums(nums):
#    numsSet = set()
#    for num in nums:
#        if -num in numsSet:
#            print("Summed to 0")
#            return True
#        numsSet.add(num)
#    return False






two_sums(nums)


