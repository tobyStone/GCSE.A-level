def MergeSort(arr):
    print("arr", arr)
    if len(Arr)<=1:
        return Arr

    else:
        print("Arr", Arr)
        middle = len(Arr)//2
        left = MergeSort(Arr[:middle])
        right = MergeSort(Arr[middle:])
#        print(left, "left", right, "right")
        return Merge(left, right)



def Merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
 #           print(left)
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
Arr = [] 

for x in range (0, arrLen):
        print ("Please input the list")
        OListInput = int(input())
        Arr.append(OListInput)
print ("This is the list that was entered", Arr)

#arr = [8,4]
print(MergeSort(Arr))
