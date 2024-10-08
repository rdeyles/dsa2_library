#Code for merge sort using recursion
'''def MergeSort(arr):
    
    if len(arr)==1:
        return arr    
    else:
        mid=len(arr)//2
        arr_left=arr[:mid]
        arr_right=arr[mid:]
        sorted_left=MergeSort(arr_left)
        sorted_right=MergeSort(arr_right)
        return MergeArr(sorted_left,sorted_right)


def MergeArr(arr1,arr2):
    merged_arr=[]
    i=j=0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<=arr2[j]:
            merged_arr.append(arr1[i])
            i+=1
        else:    
            merged_arr.append(arr2[j])
            j+=1
    return merged_arr

arr=[9,8,0,7,3,2]
result=MergeSort(arr)
print(result)''' #doesn't work

#working code, copied from W3Schools
def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    return merge(sortedLeft, sortedRight)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
sortedArr = mergeSort(unsortedArr)
print("Sorted array:", sortedArr)
