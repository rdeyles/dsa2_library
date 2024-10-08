def UserArray(list):
    print("Please provide an ordered list of numbers one at a time.")
    n=int(input("How many numbers do you wish to add to the list? "))
    for i in range(0,n):
        element=int(input("Enter a number: "))
        list.append(element)
    return list
