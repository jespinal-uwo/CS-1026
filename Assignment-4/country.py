# Assignment #4 - Juan Espinal Comp Sci 1026 A
# Student Number - 251214614
# Dec 6th, 2021 - This program takes a list of countries and updates their population, area, and continent values given a file of records
#               - All succesful updates are then written to "output.txt"




# This class creates objects that stores the attributes of every single country

class Country:
    # Each country contains 4 attributes - name, population, area, and continent
    def __init__(self,name ="",pop="",area="",continent=""):
        self.countryName = name
        self.countryPopulation = pop
        self.countyArea = area
        self.countryContinent = continent

    # Getter methods that obtains the instance variables
    def getName(self):
        return self.countryName
    def getPopulation (self):
        return self.countryPopulation
    def getArea (self):
        return self.countyArea
    def getContinent(self):
        return self.countryContinent
    # Setter methods that set the instance variables to a value
    # (Initializes the attributes for the class)

    def setCountry (self,setCountryName):
        self.countryName = setCountryName
    def setPopulation (self, setCountryPop ):
        self.countryPopulation = setCountryPop
    def setArea(self, setCountryArea):
        self.countyArea = setCountryArea
    def setContinent(self, setCountryContinent):
        self.countryContinent = setCountryContinent

    # prints all the attributes for each country
    def __repr__(self):
        return str (self.countryName) + "(pop: " + str (self.countryPopulation) + ", size: " + str (self.countyArea) + ") in " + str (self.countryContinent)
