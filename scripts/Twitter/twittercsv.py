#!/usr/bin/env python
from twitter import Twitter, OAuth
from secret import access_token, access_token_secret, consumer_key,consumer_secret
import csv
import string
import pprint


def search(keyword):
    """
    Search for tweets via a keyword and output the data to a csv file
    """
    # Initialize the Twitter API.
    t = Twitter(                                
    auth=OAuth(access_token,
     access_token_secret,
      consumer_key, consumer_secret)
      ) 
    print('please wait looking for tweets... ')

    # Input search criteria'
    s = t.search.tweets(q=keyword,             
                        tweet_mode='extended',
                        count=2000, lang='en')

    # Open csv file
    with open('tweets.csv', 'w') as outfile:
        fieldnames = ['Text', 'Name', 'Url']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for tweet in s['statuses']:
            unclean_text =  tweet['full_text']
            clean_text = [i.strip(string.punctuation) for i in unclean_text.split()] # Clean Tweet text from punctuation
            text = ' '.join(clean_text)
            name = tweet['user']['name']
            url = 'https://twitter.com/statuses/'+tweet['id_str']
            writer.writerow({'Text': text ,
            'Name': name ,
            'Url': url })

    print("Tweets successfully saved in a csv file!")

keyword = input("Put your keyword: ")
search(keyword)





