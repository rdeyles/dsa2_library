import UserArray as up
list=[]
numbers = up.UserArray(list)
target=int(input("Please enter an integer to search for: "))
found = False
while not found and len(numbers)>0:
    if numbers[int(len(numbers)/2)]==target:
        print("I found the number "+str(target)+" in the array.")
        found = True
    if numbers[int(len(numbers)/2)]< target:
        numbers=numbers[int(len(numbers)/2)+1:len(numbers)]
    elif numbers[int(len(numbers)/2)]>target:
        numbers=numbers[0:int(len(numbers)/2)]



