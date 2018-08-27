#import json library since working with json
import json
#open the tweets_small file in read mode, call file tweetFile
tweetFile = open("tweet_small.json", "r")
#using json library, load data from tweetFile, save in tweetFile
tweetData = json.load(tweetFile)
#close file since done reading
tweetFile.close()

print(tweetData[0]['favorite_count'])

if "in_reply_to_screen_name" in tweetData[25].keys():
    print('yes')
else:
    print('no')
