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
This twitter_scrape.py script...

Attributes:
    module_level_variable1 (int): [description]

Todo:
    * For module TODOs
"""

import tweepy
from Media import Media
import datetime
import time
import requests
import re
import urllib.request
import http.client
import urllib.parse
from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_user_info():
    c_key = input("Consumer key: ")
    c_secret = input("Consumer secret: ")
    a_key = input("Access token: ")
    a_secret = input("Access token secret: ")
    auth = tweepy.OAuthHandler(c_key, c_secret, "https://google.com")
    auth.set_access_token(a_key, a_secret)
    api = tweepy.API(auth)
    return api

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

def build_media_objects(dates, tweets_timestamped):
    media_objects = []
    for i in range(0, len(dates)):
        media_objects.append(Media('Twitter', dates[i], tweets_timestamped[i]))
    return media_objects

def unshorten_url(url):
    session = requests.Session()  # so connections are recycled
    resp = session.head(url, allow_redirects=True)
    return resp.url

# def get_tweets(url):
#     r = requests.get(url)
#     data = r.text.encode('utf-8')
#     soup = BeautifulSoup(data, 'html.parser')
#     tweets = [p.text.encode('utf-8') for p in soup.findAll('p', class_ = 'tweet-text')]
#     print(tweets)
#     return tweets

def get_tweet_images(tweets):
    tweet_images = []
    for i in range(0, len(tweets)):
        tweet = str(tweets[i])
        print(re.search("(?P<url>https?://[^\s]+)", tweet).group("url"))
        if tweet.contains("pic.twitter.com"):
            tweet_images.add(tweets[i])
    unshortened_url = unshorten_url("http://pic.twitter.com/h7Hf2STehM")
    html = urlopen(unshortened_url)
    bsObj = BeautifulSoup(html.read());
    for link in bsObj.find_all('img'):
        print(link.get('src'))
    #urllib.request.urlretrieve("https://pbs.twimg.com/media/DPNbUiJUEAAiOra.jpg", "twitter1.jpg")

dates, tweets_timestamped = get_tweets_by_date(get_user_info(), 'nicholaszufelt')
print([str(x) for x in build_media_objects(dates, tweets_timestamped)])
