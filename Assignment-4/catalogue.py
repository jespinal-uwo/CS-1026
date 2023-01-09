# Assignment #4 - Juan Espinal Comp Sci 1026 A
# Student Number - 251214614
# Dec 6th, 2021 - This program takes a list of countries and updates their population, area, and continent values given a file of records
#               - All succesful updates are then written to "output.txt"


from country import Country

# class that contains all the countries
class CountryCatalogue ():
    def __init__(self, countryFile):

        # list that stores all the countries objects in a list
        self.countryCat = []
        # creates a country object of class Country ()
        self.countryObject = Country ()

        file = open (countryFile, "r")
        myFile = file.readlines()[1:] # Skips the first line

        # Goes through every line in the data file
        for line in myFile:
            # Strips the line based on whitespace
            line = line.strip()

            # Splits it into a list based on |
            splitLine = line.split("|")

            # Adds a country to the catalogue
            self.country = splitLine [0]
            self.continent = splitLine [1]
            self.population = splitLine [2]
            self.area = splitLine [3]

            self.addCountry(self.country,self.population,self.area,self.continent)
    # Adds all the countries in data.txt to the country catalogue
    def addData (self,countryFile):
        file = open (countryFile, "r")
        myFile = file.readlines()[1:] # Skips the first line

        for line in myFile:
            # Strips the line based on whitespace
            line = line.strip()
            splitLine = line.split("|")
            self.country = splitLine [0]
            self.continent = splitLine [1]
            self.population = splitLine [2]
            self.area = splitLine [3]

            self.addCountry(self.country,self.population,self.area,self.continent)


    def setPopulationOfCountry (self,setCountry, populationSet):
        # Goes through each element in the list of countries objects
        for i in range (len (self.countryCat)):
            # Finds if the country the user has input is equal to a country in the list
            if setCountry == self.countryCat[i].countryName:
                # set the population of the country as specified by the user
                self.countryCat[i].setPopulation (populationSet)



    def setAreaOfCountry (self, setCountry,areaSet):
        # Goes through each element in the list of countries objects
        for i in range (len(self.countryCat)):
            # Finds if the country the user has input is equal to a country in hte list
            if setCountry == self.countryCat[i].countryName:
                # sets the area of the country as specified by the user
                self.countryCat[i].setArea (areaSet)



    def setContinentOfCountry (self, setCountry, continentSet):
        for i in range (len(self.countryCat)):
            if setCountry == self.countryCat[i].countryName:
                self.countryCat[i].setContinent (continentSet)

    # Essentially removes any duplicates countries
    def findCountry (self,country):
        # Checks to see if an object of the Country Class is in the list of country objects Country Cat

        if (len(self.countryCat)) != 0:
            for i in range (len(self.countryCat)):
                if self.countryCat[i].countryName == country.countryName:
                    return country

        return None

    # Removes a country from the catalogue
    def removeCountry (self, country):

            for i in range (len (self.countryCat)):
                if self.countryCat[i].countryName == country:
                    self.countryCat.pop (i)
                    break

    # Adds a country to the catalogue
    def addCountry (self, countryName=  "", pop = "",area = "",cont = ""):
        self.countryObject = Country (countryName)
        self.countryObject.setPopulation(pop)
        self.countryObject.setArea(area)
        self.countryObject.setContinent(cont)

        # Appends an object of class Country to the CountryCat list
        # Essentially removes any duplicate countries
        if self.findCountry(self.countryObject) == None:
            self.countryCat.append(self.countryObject)


    # prints every single country objec
    def printCountryCatalogue (self):
        for i in self.countryCat:
            print(i)


    # Writes all the countries to a file, preferably called output.txt
    def saveCountryCatalogue (self,fname):
        saveFile = open (fname, "w")

        lstofSortedCountries = []
        lstofIndeces = []
        lstofCountries = []
        lstofPopulation = []
        lstofSize = []
        lstofContinents = []

        # puts all the names, continent, populations, and area of countries in the catalogue of countries into their respective lists
        for i in range (len(self.countryCat)):
            lstofCountries.append (self.countryCat[i].countryName)
            lstofContinents.append (self.countryCat[i].countryContinent)
            lstofPopulation.append(self.countryCat[i].countryPopulation)
            lstofSize.append(self.countryCat[i].countyArea)

        # Sorts the countries in alphabetical order
        for i in range (len(self.countryCat)):
            lstofSortedCountries.append (self.countryCat[i].countryName)
        # Sorts the countries in alaphabetical order
        lstofSortedCountries.sort()

        # Finds where the indeces of where the sorted countries are found in the original list of countries
        for i in range (len(self.countryCat)):
           lstofIndeces.append(lstofCountries.index (lstofSortedCountries[i]))

        for i in range (len(self.countryCat)):
            self.countryCat[i].setCountry(lstofSortedCountries[i])

        # Changes the continent, population, and area of each country in the catalogue to their respective sorted countries
        for i in range (len (self.countryCat)):
           self.countryCat[i].setContinent(lstofContinents[lstofIndeces[i]])
           self.countryCat[i].setPopulation (lstofPopulation[lstofIndeces[i]])
           self.countryCat[i].setArea (lstofSize[lstofIndeces[i]])


        saveFile.write ("Country|Continent|Population|Area\n")

        # writes the country name, continent, population,and area onto a file called output.txt
        for i in range (len(self.countryCat)):
            saveFile.write (self.countryCat[i].countryName+ "|"+self.countryCat[i].countryContinent + "|" + self.countryCat[i].countryPopulation+ "|" + self.countryCat[i].countyArea+ "\n")