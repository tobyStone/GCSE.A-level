import math

def get(nums):
    SoFar = float("+inf")
    EndingHere = 0


    for i in range(len(nums)):
        EndingHere += nums[i]

        if (SoFar > EndingHere):
            SoFar = EndingHere

        elif (EndingHere > 0):
            EndingHere = 0

    return SoFar

nums = [-2,1,-3,-4,1,2,1,5,4]
print(get(nums))
