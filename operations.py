# creating a function named display()
def display(actualLaptopDetails):
    '''
    Takes one value as parameter: actualLaptopDetails (2D List)

    Returns nothing

    display() function displayes all the laptop available in the inventory along with brand name, price, quantity, CPU and GPU in a tabular format.
    '''
    # looping through the 2D list and displaying the data in tabular format
    print("")
    print(f"{'-' * 52}STOCK{'-' * 52}")
    print(f"{'=' * 109}")
    print("| Laptop Name     | Brand Name      | Price           | Quantity        | Processor       | Graphics Card   |")
    print(f"{'=' * 109}")
    for i in range(len(actualLaptopDetails)):
        print("|", end="")
        for j in range(len(actualLaptopDetails[i])):
            length_value = 16 - len(actualLaptopDetails[i][j])
            if j == 2:
                new_value = ' $' + actualLaptopDetails[i][j] + ((length_value-1) * ' ') + '|'
            else:
                new_value = ' ' + actualLaptopDetails[i][j] + (length_value * ' ') + '|'
            # displaying the data in the terminal and making sure not to print a new line after
            print(new_value, end="")
        # printing a new line
        print("")
    print(f"{'=' * 109}")

# creating a function named orderLaptop()
def orderLaptop(actualLaptopDetails, laptopName, laptopQuantity):
    '''
    Takes three values as parameter: actualLaptopDetails (2D List), laptopName (String), laptopQuantity (integer)

    Returns five values: laptopPrice, laptopBrand, laptopQuantity, individualPrice, actualLaptopDetails

    orderLaptop() function checks whether the laptop ordered is in the stock and check if the quatity meets the necessary conditions and returns some values accoring the values given in the parameter.
    '''
    # setting the variables to their values
    laptopPrice = 0
    individualPrice = 0
    isLaptopFound = False
    laptopBrand = ""
    # looping through the list and accessing the brand name, individual price and total price of the laptop and storing the values 
    for i in range(len(actualLaptopDetails)):
        if laptopName.lower() == actualLaptopDetails[i][0].lower():
            isLaptopFound = True
            laptopBrand = actualLaptopDetails[i][1]
            individualPrice = int(actualLaptopDetails[i][2])
            laptopPrice = laptopQuantity * int(actualLaptopDetails[i][2])
            actualLaptopDetails[i][3] = int(actualLaptopDetails[i][3]) + laptopQuantity
            # breaking the for loop
            break
            
    # displaying a message when laptop doesn't exist or is not in stock
    if not isLaptopFound:
        print(f"We don't have {laptopName} available")
        laptopQuantity = 0
    
    # returning the values
    return laptopPrice, laptopBrand, laptopQuantity, individualPrice, actualLaptopDetails

# creating a function named sellLaptop()
def sellLaptop(actualLaptopDetails, laptopName, laptopQuantity):
    '''
    Takes three values as parameter: actualLaptopDetails (2D List), laptopName (String), laptopQuantity (integer)

    Returns five values: laptopPrice, laptopBrand, laptopQuantity, individualPrice, actualLaptopDetails

    sellLaptop() function checks whether the laptop to be sold is in the stock and check if the quatity meets the necessary conditions and returns some values accoring the values given in the parameter.
    '''
    # setting the variable to their values
    laptopPrice = 0
    laptopAvailableQuantity = 0
    individualPrice = 0
    isLaptopSold = False
    laptopBrand = ""
    # looping through the list and accessing the brand name, individual price and total price of the laptop and storing the values 
    for i in range(len(actualLaptopDetails)):
        if laptopName.lower() == actualLaptopDetails[i][0].lower():
            if laptopQuantity <= int(actualLaptopDetails[i][3]):
                laptopAvailableQuantity = actualLaptopDetails[i][3]
                laptopBrand = actualLaptopDetails[i][1]
                individualPrice = int(actualLaptopDetails[i][2])
                laptopPrice = laptopQuantity * int(actualLaptopDetails[i][2])
                actualLaptopDetails[i][3] = int(actualLaptopDetails[i][3]) - laptopQuantity
                isLaptopSold = True
                # breaking the for loop
                break

    if not isLaptopSold:
        # checking for the quantity and displaying suitable message
        if laptopAvailableQuantity == 0:
            print("We don't have such laptop available")
        else:
            print(f"We don't have {laptopQuantity} {laptopName} available. We have {laptopAvailableQuantity} in stock currently!!")
        laptopQuantity = 0
    
    # returning the values
    return laptopPrice, laptopBrand, laptopQuantity, individualPrice, actualLaptopDetails


def removeCommonLaptop(laptopList):
    '''
    Takes one value as parameter: laptopList(2D list)

    Returns a value: finalLaptopList

    removeCommonLaptop() function check all the laptop name that are in common inside of the 2D list and appends the price and quantity of common laptop name and stores the values in another 2D list. Then it returns the new 2D list with updated price and quantity
    '''
    currentLaptop = ""
    updateLaptopList = []
    # looping through the range of length of laptopList
    for i in range(len(laptopList)):
        emptyList = []
        totalQuantity = 0
        totalPrice = 0
        currentLaptop = laptopList[i][0]
        k = 0
        # setting the condition for while loop
        while k < len(laptopList):
            # checking if the laptop ordered or sold are repeated and then adding their quantity and price
            if currentLaptop == laptopList[k][0]:
                totalQuantity += int(laptopList[k][2])
                totalPrice += int(laptopList[k][4])
            k += 1
        # append the details of laptop to the list named emptyList
        emptyList.append(laptopList[i][0])
        emptyList.append(laptopList[i][1])
        emptyList.append(str(totalQuantity))
        emptyList.append(str(laptopList[i][3]))
        emptyList.append(str(totalPrice))
        # append emptyList to updateLaptopList
        updateLaptopList.append(emptyList)
    
    finalLaptopList = []
    temporaryList = []
    # looping through the range of length of updateLaptopList
    for i in range(len(updateLaptopList)):
        laptop = updateLaptopList[i][0]
        # if laptop is not present in temporaryList then append them to their respective list
        if laptop not in temporaryList: 
            finalLaptopList.append(updateLaptopList[i])
            temporaryList.append(laptop)

    # return finalLaptopList
    return finalLaptopList
