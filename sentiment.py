import json
from textblob import TextBlob
import numpy as np
import matplotlib.pyplot as plt
import math

def main():
    polarity = []
    subjectivity = []
    #open the tweets_small file in read mode, call file tweetFile
    tweetFile = open("tweet_small.json", "r")
    #using json library, load data from tweetFile, save in tweetFile
    tweetData = json.load(tweetFile)
    #close file since done reading
    tweetFile.close()
    for i in range(len(tweetData)):
        theTweet = TextBlob(tweetData[i]['text'])
        polarity.append(theTweet.sentiment.polarity)
        subjectivity.append(theTweet.sentiment.subjectivity)

    avg_subject = sum(subjectivity)/len(subjectivity)
    avg_polarity = sum(polarity)/len(polarity)
    polarity.sort()
    print(polarity[0])
    print(polarity[len(polarity)-1])
    print(avg_subject)
    print(avg_polarity)

    plt.hist(polarity, bins=[-0.6,0,0.5,1.1])
    plt.xlabel("Polarity")
    plt.ylabel("Number Of Tweets")
    plt.title("Polarity vs. Tweets")
    plt.axis([-0.6, 1.1, 0, 100])
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()


'''
	for tweet in TweetData:
        tweet_text = tweet['text']
        tweet_tb = textBlob(tweet_text)
        sent = tweet_tb.sentiment
        subjecivity.append(sent.subjectivity)
        polarity.append(sent.polarity)

    avg_subject = sum(subjectivity)/len(subjecivity)
    avg_polarity = sum(polarity)/len(polarity)

    print(avg_subject)
    print(avg_polarity)
'''
    #for each tweet:
        # make a TextBlob xxxxx
        # to make a variable v that is a textblob from xxxxx
        #   a string variable called s, you would do: xxxxx
        #       v = TextBlob(s) xxxx
        # to get a sentiment object from v, do:
        #       v_sentiment = v.sentiment
        # to get the polarity or subjectivity:
        #      v_sentiment.polarity
        #       v_sentiment.subjectivity
        #then you'd want to add the values to your list
    # get average of each list
