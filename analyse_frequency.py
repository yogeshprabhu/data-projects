import sys
import json

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
            tweet_text=tweetj["text"].encode('utf-8')
            tweets.append(tweet_text)
  		

    return tweets
    
def unique_list(tweetlist):
    length=len(tweetlist) 
    tweetword_list=[]
    for term in range(length):
        wordlist=tweetlist[term].split(' ')
        for word in wordlist:
            tweetword_list.append(word)
            
    uniquelist=set(tweetword_list)
    total_words=len(tweetword_list)
    
    for uniqueword in uniquelist:
        word_freq=tweetword_list.count(uniqueword)
        frequency = float(word_freq) / float(total_words)
        print uniqueword + " " + str(frequency)
        
        
        
    
    


def main():
    tweetlist = get_tweets(sys.argv[1])
    termlist = unique_list(tweetlist)



if __name__ == '__main__':
    main()
