import math

def get(nums):
    maxSoFar = float("-inf")
    maxEndingHere = 0

    for i in range(len(nums)):
        maxEndingHere += nums[i]

        if (maxSoFar < maxEndingHere):
            maxSoFar = maxEndingHere

        elif (maxEndingHere < 0):
            maxEndingHere = 0

    return maxSoFar

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(get(nums))
