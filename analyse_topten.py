import sys
import json
import re

def get_tweets(tweetfile):
    file2 = open(tweetfile)
    tweets=[]
    for tweet in file2:

        #tweets will be in json format
        tweetj=json.loads(tweet)
        #To determine the keys in the available input file
        #print tweetj.keys()

        #Condition to check if tweets has the key 'text' or else program will throw error
        #some tweets does not have the text key
        if 'text' in tweetj.keys():
            tweets.append(tweetj)


    return tweets


def get_hashtags(tweetlist):
    length=len(tweetlist) 
    hashlist = []
    for tweet in tweetlist:
        if 'entities' in tweet.keys() and "hashtags" in tweet["entities"]:
            for hashtag in tweet["entities"]["hashtags"]:
                hashtext=hashtag["text"].encode('utf-8')
                hashlist.append(hashtext)
    return hashlist
    
def topten(hashlist):
    toptenlist=[]
    for hashtag in hashlist:
        count =  hashlist.count(hashtag)
        count = str(float(count))
        hash_count = [hashtag , count]
        if hash_count not in toptenlist:
            toptenlist.append(hash_count)
            
    sortedlist=sorted(toptenlist,key=lambda htag: htag[1] , reverse=True)
    
    for item in range(0,10):
        print sortedlist[item][0] + " " + sortedlist[item][1]
        


def main():
    tweetlist = get_tweets(sys.argv[1])
    hashlist = get_hashtags(tweetlist)
    hashes = topten(hashlist)



if __name__ == '__main__':
    main()
