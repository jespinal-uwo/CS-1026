# Assignment #1 - Juan Espinal Comp Sci 1026 A
# Student Number - 251214614
# Oct 20th, 2021 - This program takes a string of numbers from the user and determines
#                  whether it is a valid Basic, Position, or UPC code.
#                  It then prints a summary of all the codes.


# Imports all of the functions from code_check
from code_check import checkBasic, checkUPC, checkPosition

# Initializes the list Variables
lstBasic = []
lstPosition = []
lstUPC = []
lstNone = []
# Asks for user input

user = input("Please enter code (digits only) (enter 0 to quit) ")
while user != "0":

    # Creates temporary lists
    tempLstBasic = [0] * (len(user))
    tempLstPosition = [0] * (len(user))
    tempLstUPC = [0] * (len(user))
    tempLstNone = [0] * (len(user))

    # Stores user input into 4 lists
    for i in range(len(user)):
        tempLstBasic[i] = user[i]
        tempLstPosition[i] = user[i]
        tempLstUPC[i] = user[i]
        tempLstNone[i] = user[i]

    # Call the functions to check if user input is a Basic, Positional, or UPC code
    # Appends it to a list if it finds it's from one of three kinds
    if checkBasic(user) == True:
        print("-- code: %s valid Basic code." % (user))
        lstBasic.append(tempLstBasic)

    if checkPosition(user) == True:
        print("-- code: %s valid Position code." % (user))
        lstPosition.append(tempLstPosition)

    if checkUPC(user) == True:
        print("-- code: %s valid UPC code." % (user))
        lstUPC.append(tempLstUPC)

    if checkBasic(user) == False and checkPosition(user) == False and checkUPC(user) == False:
        print("-- code: %s not Basic, Position, or UPC code." % (user))
        lstNone.append(tempLstNone)

    # Exits the loop if the user enters 0
    user = input("Please enter code (digits only) (enter 0 to quit) ")

# Details the summary by printing the contents of the list
print("")
print("Summary")

print("Basic : ", end="")
if (len(lstBasic) == 0):
    print("None")
else:
    for i in range(len(lstBasic)):
        if i == (len(lstBasic) - 1):
            print(*lstBasic[i], sep='')
        else:
            print(*lstBasic[i], sep='', end=", ")

print("Position : ", end="")
if (len(lstPosition) == 0):
    print("None")
else:
    for i in range(len(lstPosition)):
        if i == (len(lstPosition) - 1):
            print(*lstPosition[i], sep='')
        else:
            print(*lstPosition[i], sep='', end=", ")

print("UPC : ", end="")
if (len(lstUPC) == 0):
    print("None")
else:
    for i in range(len(lstUPC)):
        if i == (len(lstUPC) - 1):
            print(*lstUPC[i], sep='')
        else:
            print(*lstUPC[i], sep='', end=", ")

print("None : ", end="")
if (len(lstNone) == 0):
    print("None")
else:
    for i in range(len(lstNone)):
        if i == (len(lstNone) - 1):
            print(*lstNone[i], sep='')
        else:
            print(*lstNone[i], sep='', end=", ")





