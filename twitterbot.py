import tweepy
import time
import random
import os
#info for the keys and secret
from info import *
from datetime import datetime

#authorisation stuff
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(key,secret)
api = tweepy.API(auth)

#media folder basically read it and store it into a txt file
memes = os.listdir("C:/TweepyMemes")
random.choice(memes)


#media randomiser



#proverb randomiser
plines = open("proverbs").read().splitlines()
rand_plines = random.choice(plines)


#paths to the image folder and the images
path= 'C:/TweepyMedia/'
picture = 'gigachad'
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


def reply():
    #this is to grab the tweet
    tweet = api.mentions_timeline(since_id=read_last_seen(name_list))
    lines = open("Lyrics").read().splitlines()
    rand_lines = random.choice(lines)
    for tweets in (tweet):
        if "#lyrics" in tweets.text.lower():
         print(str(tweets.id) + " " + tweets.text) #basically this just shows that its receiving the tweet
         api.update_status_with_media("@" + tweets.user.screen_name + " " + rand_lines,filename, in_reply_to_status_id = tweets.id_str)
        if "#proverbs" in tweets.text.lower():
         print(str(tweets.id) + " " + tweets.text) #basically this just shows that its receiving the tweet
         api.update_status_with_media("@" + tweets.user.screen_name + " " + rand_plines, filename, in_reply_to_status_id=tweets.id_str)
        if "memes" in tweets.text.lower():
            api.update_status_with_media("@" + tweets.user.screen_name + " " , random.choice(memes),
                                         in_reply_to_status_id=tweets.id_str)
        store_last_seen(name_list, tweets.id)


#setting up the fucntion to check the time
minutes = datetime.now().minute
def Hourtweet(minutes):
     if minutes == 0:
         api.update_status_with_media(rand_plines,filename)


while True:
    reply()
    time.sleep(5)
    Hourtweet(minutes)
    time.sleep(5)
