def LinearSearch(numbers, target):
    for i in range (0,len(numbers)):
        if numbers[i]==target:
            return i
    return -1


numbers = [3,4,90,75,382,2,8,3,55,32,1,19,0,11]
target = int(input("Please enter the number you wish to search for: "))

result = LinearSearch(numbers, target)
if result==-1:
    print("The number "+str(target)+" cannot be found.")
else:
    print("I found the number "+str(target)+" in the index "+str(result)+ " of the array.")

