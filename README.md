# MediaSkrape

MediaSkrape is an open source library that contains functions for pulling data from various social media platforms, including Facebook, Twitter and Instagram, as well as Gmail, Google Photos, and Google Calendars. This data could take the form of events, pictures, videos, or text posts. The library can be used to easily collect and clean data from these platforms and contains a variety of other functions.

It is often very difficult to find large datasets for studying posts on social media platforms, since these platforms are disparate and tied to various private companies. MediaSkrape aims to find cleaner, faster ways of pulling data from these sites in order to help data scientists find better social media datasets. This library could also be used, say, to aggregate data across platforms and better understand a social media users’ daily activities across platforms.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them

```
pip install tweepy
pip install python-instagram
pip install datetime
pip install requests
pip install urllib3
pip install httplib2
pip install bs4
```

### Installing

A step by step series of examples that tell you how to get a development env running

Clone or Download Repository

Create twitter app at [apps.twitter.com](apps.twitter.com)

![alt text](https://github.com/jocelynshen/MediaSkrape/blob/master/img/twitter_api_1.png "Create app")

Find consumer keys

![alt text](https://github.com/jocelynshen/MediaSkrape/blob/master/img/twitter_api_2.png "Consumer keys")

Generate access tokens

![alt text](https://github.com/jocelynshen/MediaSkrape/blob/master/img/twitter_api_3.png "Access keys")

Run twitter_skrape.py to generate your twitter account information

## Usage and Structure

MediaSkrape currently collects three types of media:
  1. tweets
  2. instagram posts
  3. facebook posts

Each one has two fields: *image* and *text*. Either may be null.

TODO: add more


## Built With

* [Tweepy](http://www.tweepy.org/) - Used to gather account information from Twitter
* [Twitter API](https://developer.twitter.com/en/docs) - Used to generate keys
* [Python-Instagram](https://github.com/facebookarchive/python-instagram) - Used to gather account information from Instagram
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) - Used to pull images from social media sites

## Contributing

Please read [CONTRIBUTING.md](https://github.com/jocelynshen/MediaSkrape/blob/master/CONTRIBUTING.md) for details on the process of submitting pull requests to this project.


## Authors

* **Jocelyn Shen** - *Initial work* - [GitHub Profile](https://github.com/jocelynshen)

See also the list of [contributors](https://github.com/jocelynshen/MediaSkrape/graphs/contributors) who participated in this project.

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE.md](LICENSE.md) file for details
