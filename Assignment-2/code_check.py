# Checks if the string of number is of Basic type
def checkBasic(numUserBasic):
    sumBasic = 0
    noLastBasic = numUserBasic[0:-1]  # Removes the last character in the string of numbers

    # computes the sum of the string of numbers
    for digitBasic in noLastBasic:
        sumBasic += int(digitBasic)

    checkDigitBasic = int(numUserBasic[-1])

    if sumBasic % 10 == checkDigitBasic:  # compares if sum modulus 10 is equal to the check digit
        return True
    else:
        return False


# Checks if the string of numbers is of Position type
def checkPosition(numUserPosition):
    sumPosition = 0
    indexPostion = 1
    noLastPosition = numUserPosition[0:-1]  # Removes the last character in the string of numbers

    # Computes the sum of multiplying each digit by its index in the base identification number
    for digitPosition in noLastPosition:
        sumPosition += (int(digitPosition) * indexPostion)
        indexPostion += 1

    checkDigitPosition = int(numUserPosition[-1])
    # Checks if sum modulus 10 is equal to the check digit
    if sumPosition % 10 == checkDigitPosition:
        return True
    else:
        return False


# Checks if the string of numbers are of UPC type
def checkUPC(numUserUPC):
    sumUPC = 0
    indexUPC = 1
    noLastUPC = numUserUPC[0:-1]  # Removes the last character in the string of numbers

    for digitUPC in noLastUPC:
        if indexUPC % 2 == 0:  # Checks if index number is even
            sumUPC += 1 * int(digitUPC)
        else:  # Checks if index number is odd
            sumUPC += 3 * int(digitUPC)
        indexUPC += 1

    checkDigitUPC = int(numUserUPC[-1])
    # Computes the number that is used to check if it's equal to the check Digit
    if sumUPC % 10 == 0:
        check = 0
    else:
        check = 10 - (sumUPC % 10)

    # checks if the sum is equal to the check digit
    if check == checkDigitUPC:
        return True
    else:
        return False




