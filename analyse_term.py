import sys
import json

def senti_dict(sentifile):
    file1 = open(sentifile)
    #Initialize the score dictionary
    senti_scores={}
    for ln in file1:
        word,score=ln.split("\t") #delimited by tab
        senti_scores[word]=int(score)
    return senti_scores


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

	
def cal_score(tweetlist,scoredict):
    length=len(tweetlist)    
    
    # To calculate the tweet score
    for item  in range(length):
        total=0
        wordlist=tweetlist[item].split(' ')
        #print word
        for word in wordlist:
            if word in scoredict.keys():
                word=word.lower()
                total += float(scoredict[word])
            else:
                total = total
     # To calculate the each word score in the list or not in the list       
        for word  in wordlist:
            if word in scoredict.keys():
	        term_score = float(scoredict[word.lower()])
                term_score = str(term_score)
                print word + " " + term_score
             else:
	        term_score = float(total/len(wordlist))
                term_score = str(term_score)
	        print word + " " + term_score






def main():
    scoredict = senti_dict(sys.argv[1])
    tweetlist = get_tweets(sys.argv[2])
    sentiscore = cal_score(tweetlist,scoredict)




if __name__ == '__main__':
    main()

