# creating a function named readFile()
def readFile():
    '''
    Takes no value as parameter.

    Returns a value: actualLaptopDetails (2D list)
    
    readFile() function reads the laptopStock.txt file and stores all the values in a 2D list.
    The price has a $ sign which is also removed and the data are stored in the new 2D list removing the $ sign from price. 
    Finally the 2D list without the $ sign is returned.
    '''
    # opening the laptopStock.txt file in read mode
    with open("laptopStock.txt", "r") as file:
        # spliting the file by lines and storing each line as an element of list named fileData
        fileData = file.read().splitlines()

    # creating an empty list
    laptopDetails = []
    # looping through each element (list) of fileData
    for i in fileData:
        # splitting the line in terms of ", " and appending it to laptopDetails
        laptopData = i.split(", ")
        laptopDetails.append(laptopData)

    # creating an empty list
    actualLaptopDetails = []
    # looping through each index i in the range of length of laptopDetails
    for i in range(len(laptopDetails)):
        # creating an empty list
        temporaryStoringList = []
        # looping through each index j in the range of length of laptopDetails[i]
        for j in range(len(laptopDetails[i])):
            # removing the $ sign from laptopDetails[i][j] and adding it to the new list
            temporaryStoringList.append(laptopDetails[i][j].replace("$", ""))
        # adding the new list to the actualLaptopList
        actualLaptopDetails.append(temporaryStoringList)

    # returning actualLaptopDetails
    return actualLaptopDetails