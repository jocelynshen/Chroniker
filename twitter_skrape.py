# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##############################################################################

"""
This twitter_skrape.py script contains functions to pull your twitter data

Todo:
    * For module TODOs


Methods to implement:
- get tweet by \date(range)?\
    - extract image, text



"""

import tweepy
from Media import Media
import datetime
from datetime import datetime
import time
import requests
import re
import urllib.request
import http.client
import urllib.parse
from urllib.request import urlopen
from bs4 import BeautifulSoup


class TwitterAccessor():
    def __init__(self, keyfile):
        with open("twitter_keys.txt", "r") as f:
            consumer_key = f.readline().strip()
            consumer_secret = f.readline().strip()
            access_token = f.readline().strip()
            access_token_secret = f.readline().strip()
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def get_tweets_in_date_range(self, start, end):
        # tweets = self.api.user_timeline()
        tweets = tweepy.Cursor(self.api.user_timeline).items()
        return []

    def clean_tweet(self, tweet):
        text = re.sub(' https://t.co/[A-Za-z0-9]{10}', '', tweet.text)
        try:
            # tweet.entities['media']
            images = [t['media_url'] for t in tweet.entities['media'] if t['type']=='photo']
        except:
            images = []
        time_posted = tweet.created_at #datetime.strptime(tweet.created_at, "%a %b %d %H:%M:%S %z %Y")
        return {'time':time_posted, 'text':text, 'images':images}


# ====================================================================

def get_my_info(api):
    return 'My information:' + str(api.me().name)

def get_friend_names(api):
    friends = []
    for friend in tweepy.Cursor(api.friends).items():
        friends.append(str(friend.name))
    return 'My friends:' + str(friends)

def get_tweets_by_date(api, username):
    tweets = api.user_timeline(username)
    dates = []
    for tweet in tweets:
        if str(tweet.created_at)[0:10] not in dates:
            dates.append(str(tweet.created_at)[0:10])
    tweets_timestamped = []
    for date in dates:
        a = []
        for tweet in tweets:
            if str(tweet.created_at)[0:10] == str(date):
                a.append(tweet.text.encode('utf-8'))
        tweets_timestamped.append(a)
    return dates, tweets_timestamped

def get_my_tweets(api):
    tweets = []
    for t in tweepy.Cursor(api.user_timeline).items():
        tweets.append(str(t.text.encode("utf-8")))
    return tweets

def get_tweet_images(api, username):
    tweets = api.user_timeline(username)
    for tweet in tweets:
        name = str(tweet.created_at)
        print(name, tweet.text.encode('utf-8'), "\n")
        find_src = re.search("(?P<url>https?://[^\s]+)", str(tweet.text.encode('utf-8')))
        if find_src is not None:
            print(find_src.group('url'))

def build_media_objects(dates, tweets_timestamped):
    media_objects = []
    for i in range(0, len(dates)):
        media_objects.append(Media('Twitter', dates[i], tweets_timestamped[i]))
    return media_objects

def unshorten_url(url):
    session = requests.Session()  # so connections are recycled
    resp = session.head(url, allow_redirects=True)
    return resp.url

