

def MergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = MergeSort(arr[:mid])
    right = MergeSort(arr[mid:])
#    print(arr)
    return merge(left, right)


def merge(left, right):
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
            print(right)
    result += left[i:]
    result += right[j:]
    return result
#print("9, 4, 3, 5, 5, 1, 7")
print(MergeSort([9, 4, 3, 5, 5, 1, 7]))