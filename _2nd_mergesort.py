
def Merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
            print(left)
        else:
            result.append(right[j])
            j += 1

            # print(right)
            result += left[i:]
            result += right[j:]

            return result

#Original List
print ("How long is the length of the list?")
arrLen = int(input())
arr = []

for x in range (0, arrLen):
        print ("Please input the list")
        OListInput = int(input())
        arr.append(OListInput)
        print ("This is the list that was entered", arr)

#arr = [8,4]
print(MergeSort(arr))




#        if arr[0]<=arr[1]:
#            return [arr[0], arr[1]]

#        else:
#            return [arr[1], arr[0]]


# if arr[0]<=arr[1]:
# return [arr[0], arr[1]]

# else:
# return [arr[1], arr[0]]
