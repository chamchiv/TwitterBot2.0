import tweepy
import time
import random
#info for the keys and secret
from info import *


#authorisation stuff
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(key,secret)
api = tweepy.API(auth)

#paths to the image folder and the images
path= 'C:/TweepyMedia/'
picture = 'gigachad.jpg'
filename = path + picture



name_list = 'last_seen.txt'
#these functions are to open the last seen id to avoid duplication of replies
def read_last_seen(name_list):
    file_read = open(name_list,'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id
def store_last_seen(name_list,last_seen_id):
    file_write = open(name_list,'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return


def lyrics_reply():
    #this is to grab the tweet
    tweet = api.mentions_timeline(since_id=read_last_seen(name_list))
    lines = open("Lyrics").read().splitlines()
    plines=open("proverbs").read().splitlines()
    rand_plines = random.choice(plines)
    rand_lines = random.choice(lines)
    for tweets in (tweet):
        if "#lyrics" in tweets.text.lower():
         print(str(tweets.id) + "" + tweets.text)
         api.update_status_with_media("@" + tweets.user.screen_name + " " + rand_lines,filename, in_reply_to_status_id = tweets.id_str)
        if "proverbs" in tweets.text.lower():
         print(str(tweets.id) + "" + tweets.text)
         api.update_status_with_media("@" + tweets.user.screen_name + " " + rand_plines, filename, in_reply_to_status_id=tweets.id_str)

        store_last_seen(name_list, tweets.id)

while True:
    lyrics_reply()
    time.sleep(15)