#sort integers or strings in ascending order
arr=[]
has_swapped = True
while has_swapped == True:
    has_swapped = False
    for i in range(0,len(arr)-1):
        if arr[i]>arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            has_swapped = True
    i = 0
print(arr)

#sort strings in ascending order of string length
arr=[]
has_swapped = True
while has_swapped == True:
    has_swapped = False
    for i in range(0,len(arr)-1):
        if len(arr[i])>len(arr[i+1]):
            arr[i], arr[i+1] = arr[i+1], arr[i]
            has_swapped = True
    i = 0
print(arr)