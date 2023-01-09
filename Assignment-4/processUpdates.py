# Assignment #4 - Juan Espinal Comp Sci 1026 A
# Student Number - 251214614
# Dec 6th, 2021 - This program takes a list of countries and updates their population, area, and continent values given a file of records
#               - All succesful updates are then written to "output.txt"

from country import Country
import re

from catalogue import CountryCatalogue

def processUpdates (cntryFileName,updateFileName,badUpdateFile = "badupdates.txt"):

    # opens a file were the statement "Update Unsuccesful" is written to
    unsuccesfulFile = open ("output.txt", "w")

    check = True
    check2 = True

    # opens a file object to write all the bad updates found in UpdateFileName
    saveFile = open (badUpdateFile,"w")

    # Asks the user to input the file name for country Data again if the file was not found
    while check2:
        try:
            catalogue = CountryCatalogue (cntryFileName)
            check2 = False
        except:
            print ("File doesn't exist for country data")
            userInput2 = input ("Would you like to quit? (\"Y\" (yes) or \"N\" (no) ): ")
            if userInput2.upper() == "N":
                cntryFileName = input ("Enter name of file with country data: ")
            elif userInput2.upper() == "Y":
                unsuccesfulFile.write("Update Unsuccessful\n")
                return (False,None)
            else:
                unsuccesfulFile.write("Update Unsuccessful\n")
                return (False,None)
    # Asks the user to input the file name for country updates if the file was not found
    while check:
        try:
            updateFile = open (updateFileName, "r")
            check = False
        except:
            print ("File doesn't exist for country updates")
            userInput = input("Would you like to quit? (\"Y\" (yes) or \"N\" (no) ): ")
            if userInput.upper() == "N":
                updateFileName = input("Enter name of file with country updates: ")
            elif userInput.upper() == "Y":
                unsuccesfulFile.write("Update Unsuccessful\n")
                return (False,None)
            else:
                unsuccesfulFile.write("Update Unsuccessful\n")
                return (False,None)

    # iterates through every single line in updateFile
    # Every time an invalid record is found for that line, it gets written to the bad updates file
    for line in updateFile:

        # strips the line of any whitespace
        line = line.strip()

        # skips the line if it's the empty line
        if len(line.strip()) == 0 :
            continue

        # Removes all whitespace between words
        line = re.sub(r"\s+", "", line, flags=re.UNICODE)

        # Counts the number of times ";" appears on each line
        if line.count (";") >= 0 and line.count(";")<=3:
            splitline = line.split(";")
        else:
            saveFile.write(line+"\n")
            continue


        # Checks to see if the line contains a country
        if splitline[0]== "":
            saveFile.write(line +"\n")
            continue
        # Checks to see if every country starts with a capital letter
        if splitline[0][0].isupper():
            country = splitline[0]
        else:
            saveFile.write(line+"\n")
            continue

        # Checks if there's more than one of “P=”, “A=”, “C=”;
        if  line.count ("A=") >1 or line.count("P=") >1 or line.count("C=") >1 :
            saveFile.write(line + "\n")
            continue

        # Checks if the first element contains any numbers
        if any(char.isdigit() for char in splitline[0]) == True:
            saveFile.write(line + "\n")
            continue


        #Adds that country to the catalogue of countries
        catalogue.addCountry(country)

        # Applies the updates to lines that contains only 1 update

        if len (splitline) >= 2:
            # Checks to see if the first element exists
            if len (splitline[1]) != 0:
                # Checks to see if the second character contains the equal sign
                if splitline [1][1]!= "=":
                    saveFile.write(line + "\n")
                    continue

                # Updates the population of the country
                if (splitline[1][0]) == "P":
                    population = splitline[1].replace("P=","")
                    if "," in population:
                        catalogue.setPopulationOfCountry(country,population)
                    else:
                        catalogue.removeCountry(country)
                        saveFile.write(line + "\n")
                        continue
                # Updates the area of a country
                if (splitline[1][0]) == "A":
                    area =  splitline [1].replace("A=","")
                    if "," in area:
                        catalogue.setAreaOfCountry(country,area)
                    else:
                        catalogue.removeCountry(country)
                        saveFile.write(line + "\n")
                        continue
                # Updates the continent of a country
                if (splitline[1][0]) == "C":
                    continent = splitline[1].replace("C=","")
                    if continent == "Africa" or continent == "Antarctica" or continent == "Arctic" or continent == "Asia" or continent == "Europe" or continent == "North_America" or continent == "South_America":
                        catalogue.setContinentOfCountry(country,continent)
                    else:
                        catalogue.removeCountry(country)
                        saveFile.write(line + "\n")
                        continue
        # Applies the updates to lines the contains two updates
        if len (splitline) >= 3:
            # Checks to see if the first element exists
            if len(splitline[2]) != 0:
                # Checks to see if the second character contains the equal sign
                if splitline[2][1]!= "=":
                    saveFile.write(line + "\n")
                    continue
                # Updates the population of the country
                if (splitline[2][0]) == "P":
                    population2 = splitline[2].replace("P=","")
                    if "," in population2:
                        catalogue.setPopulationOfCountry(country,population2)
                    else:
                        catalogue.removeCountry(country)
                        saveFile.write(line + "\n")
                        continue
                # Updates the area of the country
                if (splitline[2][0]) == "A":
                    area2 = splitline[2].replace("A=","")
                    if "," in area2:
                        catalogue.setAreaOfCountry(country,area2)
                    else:
                        catalogue.removeCountry(country)
                        saveFile.write(line + "\n")
                        continue
                # Updates the contient of the country
                if (splitline[2][0]) == "C":
                    continent2 = splitline[2].replace("C=","")
                    if continent2 == "Africa" or continent2 == "Antarctica" or continent2 == "Arctic" or continent2 == "Asia" or continent2 == "Europe" or continent2 == "North_America" or continent2 == "South_America":
                        catalogue.setContinentOfCountry(country,continent2)
                    else:
                        catalogue.removeCountry(country)
                        saveFile.write(line + "\n")
                        continue
        # Applies the updates to lines that contain three updates
        if len (splitline) >=4:
            # Checks to see if the first element exists
            if len(splitline[3])!= 0:
                # Checks if the second character contains the equal sign
                if splitline [3][1]!= "=":
                    saveFile.write(line + "\n")
                    continue
                # Updates the population of the country
                if (splitline[3][0]) == "P":
                    population3 = splitline[3].replace("P=","")
                    if "," in population3:
                        catalogue.setPopulationOfCountry(country,population3)
                    else:
                        catalogue.removeCountry(country)
                        saveFile.write(line + "\n")
                        continue

                # Updates the area of the country
                if (splitline[3][0]) == "A":
                    area3 = splitline[3].replace("A=","")
                    if "," in area3:
                        catalogue.setAreaOfCountry(country,area3)
                    else:
                        catalogue.removeCountry(country)
                        saveFile.write(line + "\n")
                        continue

                # Updates the continent of the country
                if (splitline[3][0]) == "C":
                    continent3 = splitline[3].replace("C=","")
                    if continent3 == "Africa" or continent3 == "Antarctica" or continent3 == "Arctic" or continent3 == "Asia" or continent3 == "Europe" or continent3 == "North_America" or continent3 == "South_America":
                        catalogue.setContinentOfCountry(country,continent3)
                    else:
                        catalogue.removeCountry(country)
                        saveFile.write(line + "\n")
                        continue

    # Adds the data to the output file
    catalogue.addData(cntryFileName)

    # Saves the catalogue of countries to output.txt
    catalogue.saveCountryCatalogue("output.txt")

    # Returns tuple with a True Boolean value and an object of the class CountryCatalogue
    tuple = (True, catalogue)
    return tuple