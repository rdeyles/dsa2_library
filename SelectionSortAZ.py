def SelSortAlpha(list):   
    result = []
    number_of_elements = len(list)
    n = number_of_elements
    number_of_steps = 0
    for i in range(0, number_of_elements):
        minimum_element = list[0]
        for j in range(0, n):
            if list[j] < minimum_element:
                minimum_element = list[j]
            number_of_steps +=1
        result.append(minimum_element)
        list.remove(minimum_element)
        n -=1
    print("")
    print("The list has been ordered alphabetically:")
    print(str(result))
    print("The list had " + str(number_of_elements) + " elements and I ordered it in " + str(number_of_steps) + " steps.")








