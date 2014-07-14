from __future__ import division
import sys
import json

def parsetweet(tf):
    frequencywords = {}
    totalwordcount = 0
    for line in tf:  
       dicttweet= json.loads (line)
       if 'text' in dicttweet:
            words = dicttweet["text"].split()
            for word in words:
                totalwordcount += 1
                if word in frequencywords:
                    frequencywords[word] += 1
                else:    
                    frequencywords[word] = 1
    for word in frequencywords:
        frequencywords[word] = frequencywords[word]/totalwordcount
    return frequencywords 

def main():
    twitter_file = open(sys.argv[1])
    frequency = parsetweet(twitter_file)
    for word in frequency:
        print word.encode('utf-8') + " " + str(frequency[word])
    

if __name__ == '__main__':
    main()
