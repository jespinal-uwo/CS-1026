# Function that reads the file names
def readFiles (fileName):
   inFile = open (fileName, "r", encoding='utf-8')
   return inFile

# Function that reads the keyword files and stores the keywords in a set
def readKeywords (keywordFiles, check):
   # Each set represent different keywords depending on their sentiment values
   negative = set ()
   positive = set ()
   neutral = set ()
   expressions = set ()

   # Iterates through each line in keyword file
   for line in keywordFiles:
       sentimentValue = line.split(",") # split each line by the comma
       sentimentValue [1] = int (sentimentValue [1].rstrip("\n")) # Getting rid of whitespace and obtaining the sentiment value
       if sentimentValue [1] == 10:
           positive.add (sentimentValue[0])
       elif sentimentValue [1] == 1:
           negative.add (sentimentValue[0])
       elif sentimentValue [1] == 7:
           neutral.add (sentimentValue[0])
       else:
           expressions.add (sentimentValue[0])

   # Closes the file before iterating through each line in the file again
   keywordFiles.close()

    # returns the keyword sets
   if check == 1:
       return positive
   elif check == 2:
       return negative
   elif check == 3:
       return neutral
   else:
       return expressions

# This function determines the timezone/region the tweet came from
def getTimeZone (tweetFiles):
    timeZoneList = []


    for line in tweetFiles:
        line = line.strip() # Strips off any whitespace from either end of each tweet
        splitLine = line.split("]") # splits the tweet into the latitude/longitude and the rest of the tweet
        splitLine.pop (1)
        for word in splitLine:
            word = word.lstrip("[") # gets rid of the left bracket
            word = word.split(", ")
            if len(word) == 2:
                latitude = float (word [0])
                longitude = float (word [1])
                # Determines the region of the tweet based on the latitude/longitude
                if 24.660845 <= latitude < 49.189787:
                    if -87.518395 <= longitude < -67.444574:
                        timeZoneList.append("Eastern")
                    if -101.998892 <= longitude < -87.518395:
                        timeZoneList.append("Central")
                    if -115.236428 <= longitude < -101.998892:
                        timeZoneList.append("Mountain")
                    if -125.242264 <= longitude < -115.236428:
                        timeZoneList.append("Pacific")
                else:
                    timeZoneList.append("None")
    return timeZoneList

# Function that returns the happiness score of every single tweet, each element corresponds
#  to the happiness score from a single tweet in the file
def readTweets (tweetsFiles,positiveWords,negativeWords,neutralWords,expressionWords):
   numberofKeywords = 0
   PUNC = ".?!#@"
   sentiment = 0
   sentimentLst = []

   for line in tweetsFiles:
       line = line.strip() # Strips off any whitespace from either end of each tweet
       splitLine = line.split() # splits the tweet into words based off whitespace

       for word in splitLine:
           word = word.strip () # Strips off any whitespace from either end of each word
           word = word.strip(PUNC) # Removes any punctuation from beginning and end of the word
           word = word.lower() # Converts the word into lower case letters
           if word in positiveWords:
               sentiment += 10
               numberofKeywords +=1
           if word in neutralWords:
               sentiment += 7
               numberofKeywords += 1
           if word in negativeWords:
               sentiment += 1
               numberofKeywords += 1
           if word in expressionWords:
               sentiment += 5
               numberofKeywords += 1
       if numberofKeywords!= 0:
            sentimentLst.append(sentiment//numberofKeywords)
       else:
            sentimentLst.append(-1)
       sentiment = 0
       numberofKeywords = 0
   return sentimentLst

# Function that returns the tuple for each region containing:
# The average happinness value
# Number of keywords tweets
# Number of tweets
def regionTuple (happinessScoreTweets,time_zones, check2):
    sumEasternHappinessScore = 0
    sumCentralHappinessScore = 0
    sumMountainHappinessScore = 0
    sumPacificHappinessScore = 0

    numEasternKeywordTweets = 0
    numCentralKeywordTweets = 0
    numMountainKeywordTweets = 0
    numPacificKeywordTweets = 0


    numEasternTweets = 0
    numCentralTweets = 0
    numMountainTweets = 0
    numPacificTweets = 0

    index = 0

    # Adds the sum of the happiness score for each region and counts the number of tweets in that region
    for region in time_zones:
        if region == "Eastern":
            if happinessScoreTweets [index] != -1:
                sumEasternHappinessScore +=  happinessScoreTweets [index]
                numEasternKeywordTweets+=1
                numEasternTweets +=1
            else:
                numEasternTweets+=1

        if region == "Central":
            if happinessScoreTweets [index]!=-1:
                sumCentralHappinessScore += happinessScoreTweets[index]
                numCentralKeywordTweets += 1
                numCentralTweets+=1
            else:
                numCentralTweets+=1
        if region == "Mountain":
            if happinessScoreTweets [index]!= -1:
                sumMountainHappinessScore+= happinessScoreTweets[index]
                numMountainKeywordTweets += 1
                numMountainTweets +=1
            else:
                numMountainTweets +=1
        if region == "Pacific":
            if happinessScoreTweets [index]!= -1:
                sumPacificHappinessScore += happinessScoreTweets [index]
                numPacificKeywordTweets += 1
                numPacificTweets +=1
            else:
                numPacificTweets +=1
        index +=1

    # Computes the average happiness value for each region
    if numEasternKeywordTweets!=0:
        averageEasternHappinnesValue = sumEasternHappinessScore/numEasternKeywordTweets
    else:
        averageEasternHappinnesValue = 0
    if numCentralKeywordTweets != 0:
        averageCentralHappinnesValue = sumCentralHappinessScore/numCentralKeywordTweets
    else:
        averageCentralHappinnesValue = 0
    if numMountainKeywordTweets!= 0:
        averageMountainHappinessValue = sumMountainHappinessScore/numMountainKeywordTweets
    else:
        averageMountainHappinessValue = 0
    if numPacificKeywordTweets!=0:
        averagePacificHappinessValue = sumPacificHappinessScore/numPacificKeywordTweets
    else:
        averagePacificHappinessValue = 0

    # returns the tuple with the three aforementioned parameters (check comment above the function)
    easternTuple = (averageEasternHappinnesValue,numEasternKeywordTweets,numEasternTweets)
    centralTuple =  (averageCentralHappinnesValue,numCentralKeywordTweets,numCentralTweets)
    mountainTuple = (averageMountainHappinessValue,numMountainKeywordTweets,numMountainTweets)
    pacificTuple = (averagePacificHappinessValue,numPacificKeywordTweets,numPacificTweets)

    if check2 == 1:
        return easternTuple
    if check2 == 2:
        return centralTuple
    if check2 == 3:
        return mountainTuple
    if check2 == 4:
        return pacificTuple



# processes the tweets using all the above function
def compute_tweets(fileTweets,fileKeywords):

    # returns an empty list if a file not found exception was found
   emptylist = [(0,0,0),(0,0,0),(0,0,0),(0,0,0)]
   try:
       # Stores keywords and their sentiment values into 4 sets
       positiveSet = readKeywords(readFiles(fileKeywords), 1)
       negativeSet = readKeywords(readFiles(fileKeywords), 2)
       neutralSet = readKeywords(readFiles(fileKeywords), 3)
       expressionSet = readKeywords(readFiles(fileKeywords), 4)
   except:
       return emptylist


    # list that contains the happiness score of every single tweet, each element corresponds
    # to a happiness score from a single tweet in the file
   tweetsHappinesScore = readTweets(readFiles(fileTweets),positiveSet,negativeSet,neutralSet,expressionSet)

   # list that contains the timezones of every single tweet, each element corresponds to
   # a timezone froma single tweet in the file
   timezones =  getTimeZone(readFiles(fileTweets))

    # Returns a tuple with average happiness value for that region
    # along with the number of tweets in that region with keywords
    # along with the number of tweets in that region overall
   eastern = regionTuple(tweetsHappinesScore,timezones,1)
   central = regionTuple(tweetsHappinesScore,timezones,2)
   mountain = regionTuple(tweetsHappinesScore,timezones,3)
   pacific = regionTuple(tweetsHappinesScore,timezones,4)

   lst = [eastern,central,mountain,pacific]
   return lst








