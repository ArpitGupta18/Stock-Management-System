# Importing modules
import datetime
import read
import write
import operations

# Starting a while loop with True as condition
while True:
    # try block
    try:
        # calling readFile() function from read module and storing the value in actualLaptopDetails
        actualLaptopDetails = read.readFile()
        # calling display() function from operations
        operations.display(actualLaptopDetails)
        # displaying the choices to perform further action 
        print()
        print("1. Order a laptop from the manufacturer")
        print("2. Sell a laptop to the customer")
        print("3. Exit from the program")
        print()
        # asking for input for the choices
        inputNumber = int(input("What do you want to do?(1-3): "))

    # code to execute incase of any error in try block
    except ValueError:
        print()
        print("------Please enter a number. String values, symbols and empty spaces are not allowed.------")
        print()
    
    # code to execute in case of no error in try block
    else:
        # Selection of choice 1
        if inputNumber == 1:
            # creating an empty list and setting counter to 0
            totalLaptopOrdered = []
            counter = 0
            # starting a while loop with True as condition
            while True:
                # asking for distributer's name
                distributerName = input("Enter the name of the distributer: ").lstrip().rstrip()
                # checking for distributer's name
                if distributerName == "":
                    # displaying message if distributer's name is empty
                    print()
                    print("----------------Invalid Distributer Name!!-----------------")
                    print()
                else:
                    # breaking when distributer's name is valid
                    break

            # Starting a while loop with True as condition
            while True:
                # creating an empty list and setting laptopExist to 0
                laptopExist = 0
                orderedLaptopList = []
                print()
                # Starting a while loop with True as condition
                while True:
                    # asking for laptop name
                    laptopName = input("Enter the laptop to be ordered: ").lower().lstrip().rstrip()
                    # checking for valid laptop name
                    if laptopName == "":
                        # displaying message if laptop name is empty
                        print()
                        print("----------Admin, Please enter a laptop name----------")
                        print()
                    else:
                        # breaking when laptop name is valid
                        break

                # looping throught the 2D list
                for i in range(len(actualLaptopDetails)):
                    # checking if laptop ordered is in the stock list
                    if laptopName == actualLaptopDetails[i][0].lower():
                        # setting laptopExist to 1 and then breaking
                        laptopExist = 1
                        break
                
                if laptopExist == 1:
                    # Starting a while loop with True as condition
                    while True:
                        # try block
                        try:
                            # asking laptopQuantity as input
                            laptopQuantity = int(input("Enter the quantity of laptop to order(0 to order none): "))
                        # code to execute in case of error in try block
                        except ValueError:
                            # displaying a message
                            print()
                            print("------Admin, Please enter a number. String values, symbols and empty spaces are not allowed.------")
                            print()
                        # code to execute incase of no error in try block
                        else:
                            # checking the condition of laptopQuantity that was taken as input
                            if laptopQuantity < 0:
                                # displaying a message when quantity is not valid
                                print()
                                print("------Admin, Quantity must not be in negative. Enter a positive value.------")
                                print()
                            else:
                                # Breaking the loop when quantity is valid
                                break

                    # calling orderLaptop() function from operations module and storing the value that it returns
                    laptopOrderPrice, laptopBrand, laptopQuantity, individualPrice, updateStockDetails = operations.orderLaptop(actualLaptopDetails, laptopName, laptopQuantity)
                    # calling updateStock() function from write module
                    write.updateStock(updateStockDetails)
                    # Checking the condition of laptopQuantity
                    if laptopQuantity != 0:
                        # increasing the counter and adding the laptop details to a new empty list 
                        counter += 1
                        orderedLaptopList.append(laptopName)
                        orderedLaptopList.append(laptopBrand)
                        orderedLaptopList.append(str(laptopQuantity))
                        orderedLaptopList.append(str(individualPrice))
                        orderedLaptopList.append(str(laptopOrderPrice))
                        # adding the list to another list
                        totalLaptopOrdered.append(orderedLaptopList)
                
                # checking conditon for laptopExist
                if laptopExist == 0:
                    # Displaying a message
                    print()
                    print("----------Admin, We don't have such laptop.----------")
                    print()

                # Starting a while loop with True as condition
                while True:
                    # asking for input to order again and storing in laptop_order
                    laptop_order = input("Do you want to order again? (Y/N): ").lower().lstrip().rstrip()
                    print()
                    # when input is "n"
                    if laptop_order == "n":
                        # checking the counter variable
                        if counter != 0:
                            # calling removeCommonLaptop() function from operations module to append the quantity of same kind of laptop ordered
                            updateLaptopOrder = operations.removeCommonLaptop(totalLaptopOrdered)
                            # accessing current date and time
                            todayDateTime = datetime.datetime.now()
                            currentDate = todayDateTime.strftime("%B %d, %Y")
                            currentTime = todayDateTime.strftime("%H:%M:%S")
                            # calling generateInvoice() function from write module 
                            write.generateInvoice(updateLaptopOrder, distributerName , currentDate, currentTime, todayDateTime, 0)
                        else:
                            # displaying a message
                            print()
                            print("--------------------------------No laptop ordered.-------------------------------")
                            print()
                        # breaking the loop
                        break
                    # when input is "y"
                    elif laptop_order == "y":
                        # breaking the while loop
                        break
                    else:
                        # dislaying a message
                        print("----------Command not available!!----------")
                        print()
                        
                if laptop_order == "n":
                    print("---------------------------Thank you for visiting us.----------------------------")
                    print()
                    # breaking the while loop
                    break
        
        # Selection of choice 2
        elif inputNumber == 2:
            # creating an empty list and setting the counter1 to 0
            totalLaptopSold = []
            counter1 = 0
            # Starting a while loop with True as condition
            while True:
                # asking for customer's name as input
                customerName = input("Enter the name of the customer: ").lstrip().rstrip()
                # checking the validity of customer name
                if customerName == "":
                    # displaying a message when empty
                    print()
                    print("----------------Invalid Customer Name!!-----------------")
                    print()
                else:
                    # breaking the while loop
                    break
            
            # Starting a while loop with True as condition
            while True:
                # creating an empty list setting laptopExist and laptopFound to 0
                laptopExist = 0
                laptopFound = 0
                soldLaptopList = []
                # Starting a while loop with True as condition
                while True:
                    # asking for laptop name to be sold
                    laptopName = input("Enter the laptop to be sold: ").lower().lstrip().rstrip()
                    # checking the validity of laptop name
                    if laptopName == "":
                        # Displaying a messaeg when empty
                        print()
                        print("----------Please enter a laptop name----------")
                        print()
                    else:
                        # breaking the while loop
                        break
                
                # starting a loop with range of length of actualLaptopDetails
                for i in range(len(actualLaptopDetails)):
                    # checking if laptop is in the stock or not
                    if laptopName.lower() == actualLaptopDetails[i][0].lower():
                        # setting laptopFound to 1 and retrieving the quantity and converting it to integer
                        laptopFound = 1
                        availableQuantity = int(actualLaptopDetails[i][3])
                        # checking in quantity is available for that laptop
                        if availableQuantity == 0:
                            print()
                            print("------Admin, We don't have that laptop available in stock currently!!------")
                            laptopExist = 1
                            laptopFound = 0
                        # breaking the for looop
                        break


                if laptopFound == 1:
                    # Starting a while loop with True as condition
                    while True:
                        # try block
                        try:
                            # asking for quantity of laptop to purchase
                            laptopQuantity = int(input("Enter the quantity of laptop to be sold(0 to sell none): "))
                        # code to execute incase of error in try block
                        except ValueError:
                            print()
                            print("------Admin, Please enter a number. String values, symbols and empty spaces are not an option.------")
                            print()
                        # code to execute incase of no error in try block
                        else:
                            # checking the laptopQuantity and displaying suitable message according to the conditions
                            if laptopQuantity < 0:
                                print()
                                print("------Admin, Quantity must not be in negative. Enter a positive value.------")
                                print()
                            
                            elif laptopQuantity > availableQuantity:
                                print()
                                print(f"------Admin, We have {availableQuantity} available. Enter quantity less than {availableQuantity}.------")
                                print()
                            else:
                                # breaking the for loop
                                break 
                    # calling sellLaptop() function from operations module and storing the values that it returns
                    laptopSoldPrice, laptopBrand, laptopQuantity, individualPrice, updateStockDetails = operations.sellLaptop(actualLaptopDetails, laptopName, laptopQuantity)
                    # calling updateStock() function from write module
                    write.updateStock(updateStockDetails)
                    if laptopQuantity != 0:
                        # Increasing the counter value by 1
                        counter1 += 1
                        # adding laptop details to an empty list
                        soldLaptopList.append(laptopName)
                        soldLaptopList.append(laptopBrand)
                        soldLaptopList.append(str(laptopQuantity))  
                        soldLaptopList.append(str(individualPrice))  
                        soldLaptopList.append(str(laptopSoldPrice))
                        # adding that list to a new list
                        totalLaptopSold.append(soldLaptopList)


                if laptopFound == 0:
                    if laptopExist == 0:
                        print()
                        print("----------Admin, We don't have such laptop----------")
                        
                # Starting a while loop with True as condition
                while True:
                    print()
                    # asking for any more laptop to sell and storing the value in laptop_sold
                    laptop_sold = input("Is there any laptop to be sold? (Y/N): ").lower().lstrip().rstrip()
                    print()
                    # checking the conditions for laptop_sold and performing actions related to it
                    if laptop_sold == "n":
                        if counter1 != 0:
                            # calling removeCommonLaptop() function from operations module and storing the value it returns in updatelaptopSold
                            updateLaptopSold = operations.removeCommonLaptop(totalLaptopSold)
                            # accessing the current date and time
                            todayDateTime = datetime.datetime.now()
                            currentDate = todayDateTime.strftime("%B %d, %Y")
                            currentTime = todayDateTime.strftime("%H:%M:%S")
                            # calling generateInvoice() function from write module
                            write.generateInvoice(updateLaptopSold, customerName, currentDate, currentTime, todayDateTime, 1)
                        else:
                            print()
                            print("---------------------------------No laptop sold.---------------------------------")
                            print()
                        break
                    elif laptop_sold == "y":
                        # breaking from the while loop
                        break
                    else:
                        print()
                        print("----------Command not available!!----------")
                        print()
                
                if laptop_sold == "n":
                    print("---------------------------Thank you for visiting us.----------------------------")
                    print()
                    break
        # Selection of choice 3
        elif inputNumber == 3:
            print()
            print("---------------------------Thank you for visiting us.----------------------------")
            print()
            break
        # Selection of non-existing choice
        else:
            print()
            print("------Please Choose a number between 1 and 3. Other options doesn't exist.------")
            print()
