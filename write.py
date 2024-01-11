# creating a function named updateStock()
def updateStock(actualLaptopDetails):
    '''
    Takes one value as parameter: actualLaptopDetails (2D list)

    Returns nothing

    updateStock() function updates the stock in laptopStock.txt file after any purchase or sale is made
    '''
    # opening the laptopStock.txt file in write mode
    with open("laptopStock.txt", "w") as file:
        # looping through each index in length of range of actualLaptopDetails
        for i in range(len(actualLaptopDetails)):
            # looping through each index in length of range of actualLaptopDetails 
            for j in range(len(actualLaptopDetails[i])):
                # converting the elements from the list to string an storing it in value
                value = str(actualLaptopDetails[i][j])
                if j == 2:
                    # adding the $ sign to value and writing it in the file
                    value1 = "$" + value
                    file.write(value1)
                else:
                    # writing value in the file
                    file.write(value)

                # adding a ", " after every element except for the last element in that line
                if j != len(actualLaptopDetails[i])-1:
                    file.write(', ')
            # adding a new line after every line
            if i != len(actualLaptopDetails)-1:
                file.write('\n')

# creating a function named generateInvoice()
def generateInvoice(laptopList, name, currentDate, currentTime, todayDateTime, value):
    '''
    Takes six values as parameter: laptopList (2D list), name (String), currentDate (String), currentTime (String), todayDateTime (datetime), value (integer)

    Returns nothing
    
    generateInvoice() function displays the invoice in the terminal after any purchase or sale is made and also creates a new text file to store the invoices in their respective folder. 
    '''
    # calculating the value for number of spaces to display in format of table
    dateLength = 71-len(currentDate)
    timeLength = 71-len(currentTime)
    nameLength = 60-len(name)
    # Data for generating manufacturer's invoice
    if value == 0:
        netAmount = 0
        vatAmount = 0
        grossAmount = 0
        tempVAT = 0
        for i in range(len(laptopList)):
            for j in range(len(laptopList[i])):
                if j == 4:
                    netAmount += int(laptopList[i][j])

        # calculating tempVAT, vatAmount and grossAmount
        tempVAT = 0.13 * netAmount
        vatAmount = "%.2f" % tempVAT
        grossAmount = "%.2f" % (netAmount + float(vatAmount))

    # Data for generating customer's invoice
    if value == 1:
        totalAmount = 0
        shippingCost = 0
        # looping through 
        for i in range(len(laptopList)):
            for j in range(len(laptopList[i])):
                if j == 4:
                    totalAmount += int(laptopList[i][j])

        shipLoop = True
        # looping while the condition is True
        while shipLoop:
            # asking if the products need to be delivered or not
            ship = input("Do you want your products to be delivered?(Y/N): ").lower().lstrip().rstrip()
            # checking for condition to ship
            if ship == "y":
                while True:
                    # asking whether the products need to be delivered inside or outside kathmandu valley
                    valley = input("Enter whether you are inside or outside of kathmandu valley(in/out):  ").lower().lstrip().rstrip()
                    # setting the shipping cost, calculating the total amount with shipping cost, setting shipLoop to False and breaking the loop
                    if valley == "out":
                        shippingCost = 100
                        totalAmountWithShippingCost = totalAmount + shippingCost
                        shipLoop = False
                        break
                    elif valley == "in":
                        shippingCost = 50
                        totalAmountWithShippingCost = totalAmount + shippingCost
                        shipLoop = False
                        break
                    else:
                        print()
                        print("----------Such option is not available----------")
                        print()
                    
            elif ship == "n":
                # calculating total amount with shipping cost and setting shipLoop to False
                totalAmountWithShippingCost = totalAmount + shippingCost
                shipLoop = False
            else:
                print()
                print("----------Command not available!!----------")
                print()

    # generating date and time for filename
    fileDate = todayDateTime.strftime("%Y-%m-%d")
    fileTime = todayDateTime.strftime("%H-%M-%S")
    if value == 0:
        fileName = "./distributerInvoice/"+name+"-"+ fileDate+"-"+fileTime+".txt"
    if value == 1:
        fileName = "./customerInvoice/"+name+"-"+fileDate+"-"+fileTime+".txt"

    # opening the bill file (fileName) in write mode
    with open(fileName, "w") as file:
        # writing the bill in file and displaying the bill in the terminal
        print("="*81)
        file.write(f"{'='*81}\n")
        print(f"|{' '*32}IT LAPTOP STORE{' '*32}|")
        file.write(f"|{' '*32}IT LAPTOP STORE{' '*32}|\n")
        print("="*81)
        file.write(f"{'='*81}\n")
        print(f"|  Date: {currentDate}{' '*dateLength}|")
        file.write(f"|  Date: {currentDate}{' '*dateLength}|\n")
        print(f"|  Time: {currentTime}{' '*timeLength}|")
        file.write(f"|  Time: {currentTime}{' '*timeLength}|\n")
        print("="*81)
        file.write(f"{'='*81}\n")
        if value == 0:
            print(f"|  Distributer's Name: {name}{' '*(nameLength-3)}|")
            file.write(f"|  Distributer's Name: ")
            file.write(f"{name}{' '*(nameLength-3)}|\n")
        if value == 1:
            print(f"|  Customer's Name: {name}{' '*nameLength}|")
            file.write(f"|  Customer's Name: ")
            file.write(f"{name}{' '*nameLength}|\n")
        print("="*81)
        file.write(f"{'='*81}\n")
        print("|  Laptop Name          Laptop Brand        Quantity      Rate       Price      |")
        file.write("|  Laptop Name          Laptop Brand        Quantity      Rate       Price      |\n")
        print("="*81)
        file.write(f"{'='*81}\n")
        for i in range(len(laptopList)):
            print("|  ", end="")
            file.write("|  ")
            length = 0
            for j in range(len(laptopList[i])):
                if j == 0:
                    length = 21 - len(laptopList[i][j])
                    print(laptopList[i][j] + (" " * length), end="")
                    file.write(laptopList[i][j] + (" " * length))
                if j == 1:
                    length = 20 - len(laptopList[i][j])
                    print(laptopList[i][j] + (" " * length), end="")
                    file.write(laptopList[i][j] + (" " * length))
                if j == 2:
                    length = 14 - len(laptopList[i][j])
                    print(laptopList[i][j] + (" " * length), end="")
                    file.write(laptopList[i][j] + (" " * length))
                if j == 3:
                    length = 11 - len(laptopList[i][j])
                    print("$" + laptopList[i][j] + (" " * (length-1)), end="")
                    file.write("$" + laptopList[i][j] + (" " * (length-1)))
                if j == 4:
                    length = 11 - len(laptopList[i][j])
                    print("$" + laptopList[i][j] + (" " * (length-1)) + "|", end="")
                    file.write("$" + laptopList[i][j] + (" " * (length-1)) + "|")
            print()
            file.write("\n")
        
        print("="*81)
        file.write(f"{'='*81}\n")
        if value == 0:
            netAmountBackSpace = 10 - len(str(netAmount))
            vatAmountBackSpace = 10 - len(str(vatAmount))
            grossAmountBackSpace = 10 - len(str(grossAmount))
            print(f"|{' '*55}Net Amount:  ${netAmount}{' '*netAmountBackSpace}|")
            file.write(f"|{' '*55}Net Amount:  ${netAmount}{' '*netAmountBackSpace}|\n")
            print(f"|{' '*55}VAT Amount:  ${vatAmount}{' '*vatAmountBackSpace}|")
            file.write(f"|{' '*55}VAT Amount:  ${vatAmount}{' '*vatAmountBackSpace}|\n")
            print(f"|{' '*53}Gross Amount:  ${grossAmount}{' '*grossAmountBackSpace}|")
            file.write(f"|{' '*53}Gross Amount:  ${grossAmount}{' '*grossAmountBackSpace}|\n")
        if value == 1:
            amountBackSpace = 10 - len(str(totalAmount))
            shippingCostBackSpace = 10 - len(str(shippingCost))        
            totalAmountBackSpace = 10 - len(str(totalAmountWithShippingCost))
            print(f"|{' '*59}Amount:  ${totalAmount}{' '*amountBackSpace}|")
            file.write(f"|{' '*59}Amount:  ${totalAmount}{' '*amountBackSpace}|\n")
            print(f"|{' '*52}Shipping Cost:  ${shippingCost}{' '*shippingCostBackSpace}|")
            file.write(f"|{' '*52}Shipping Cost:  ${shippingCost}{' '*shippingCostBackSpace}|\n")
            print(f"|{' '*28}Total Amount(including Shipping Cost):  ${totalAmountWithShippingCost}{' '*totalAmountBackSpace}|")
            file.write(f"|{' '*28}Total Amount(including Shipping Cost):  ${totalAmountWithShippingCost}{' '*totalAmountBackSpace}|\n")
        
        print("="*81)
        file.write(f"{'='*81}\n")
        file.write("---------------------------Thank you for visiting us.----------------------------")

    