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

import facebook
#from Media import Media
#from db_handler import DB_Handler
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

class FacebookAccessor():
    def __init__(self, keyfile="facebook_keys.txt"):
        with open(keyfile, "r") as f:
            consumer_key = f.readline().strip()
        graph = facebook.GraphAPI(access_token=consumer_key, version="2.1")
        self.api = graph
        #self.dbhandler = DB_Handler()

    def get_post_time(self, post_id):
        post = self.api.get_object(id = post_id, fields = 'created_time')
        return (post['created_time'])

    def clean_tweet(self, tweet):
        text = re.sub(' https://t.co/[A-Za-z0-9]{10}', '', tweet.text)
        try:
            images = [t['media_url'] for t in tweet.entities['media'] if t['type']=='photo']
        except:
            images = []
        time_posted = tweet.created_at #datetime.strptime(tweet.created_at, "%a %b %d %H:%M:%S %z %Y")
        return {'time':time_posted, 'text':text, 'images':images}

    def get_clean_tweets_in_date_range(self, start, end):
        tweets = tweepy.Cursor(self.api.user_timeline).items()
        return [self.clean_tweet(t) for t in tweets if self.clean_tweet(t)['time'] > start and self.clean_tweet(t)['time'] < end]

    def get_tweets_in_date_range(self, start, end):
        tweets = tweepy.Cursor(self.api.user_timeline).items()
        return [t for t in tweets if clean_tweet(t)['time'] > start and clean_tweet(t)['time'] < end]

    def get_my_info(self):
        profile = self.api.get_object('me')
        return profile

    def get_friend_names(self):
        friends = self.api.get_connections(id='me', connection_name='friends')
        return friends

    def get_my_posts(self):
        profile = self.get_my_info()
        count = 10
        query_string = 'posts?limit={0}'.format(count)
        posts = self.api.get_connections(profile['id'], query_string)
        for post in posts:
            print(post.encode('utf-8'))

    def add_to_database(self, tweet):
        self.dbhandler.add_media('t', time_posted=tweet['time'], text=tweet['text'], image=None) # update this (!)

fba = FacebookAccessor()
(fba.get_my_posts())
