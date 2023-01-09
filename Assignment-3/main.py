# Assignment #3 - Juan Espinal Comp Sci 1026 A
# Student Number - 251214614
# Nov 16th, 2021 - This program analyzes twitter information and determines the average happiness score for each region/timezone

from sentiment_analysis import compute_tweets
# inputs the file name from the user
inputFile = input("Please enter the file containing the tweets: ")
inputFile2 = input("Please enter the file containing the keywords: ")


easternRegion = compute_tweets(inputFile, inputFile2)[0]
centralRegion = compute_tweets(inputFile, inputFile2)[1]
mountainRegion = compute_tweets(inputFile, inputFile2)[2]
pacificRegion = compute_tweets(inputFile, inputFile2)[3]

print("Eastern Region --- Happiness score: {:.2f}, Keyword Tweets: {}, Total Tweets: {}\n".format(easternRegion[0],
                                                                                                  easternRegion[1],
                                                                                                  easternRegion[2]))
print("Central Region --- Happiness score: {:.2f}, Keyword Tweets: {}, Total Tweets: {}\n".format(centralRegion[0],
                                                                                                  centralRegion[1],
                                                                                                  centralRegion[2]))
print("Mountain Region --- Happiness score: {:.2f}, Keyword Tweets: {}, Total Tweets: {}\n".format(mountainRegion[0],
                                                                                                   mountainRegion[1],
                                                                                                   mountainRegion[2]))
print("Pacific Region --- Happiness score: {:.2f}, Keyword Tweets: {}, Total Tweets: {}\n".format(pacificRegion[0],
                                                                                                  pacificRegion[1],
                                                                                                  pacificRegion[2]))


