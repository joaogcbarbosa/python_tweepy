import tweepy
import uvicorn
from fastapi import FastAPI
from keys import *

app = FastAPI()
client = tweepy.Client(bearer_token=BEARER_TOKEN, consumer_key=API_KEY, consumer_secret=API_KEY_SECRET,
                       access_token=ACCESS_TOKEN, access_token_secret=ACCESS_SECRET_TOKEN)


@app.get('/')
def home():
    return {'to get your twitters id (necessary for methods below)': '/twitter-id/your_twitter_username',
            'to access your timeline': '/timeline/',
            'to access your liked tweets': '/liked-tweets/your_twitter_id',
            'to access your tweets': '/user-tweets/your_twitter_id',
            'to access tweets by subject': '/recent-tweets/subject'
            }


@app.get('/twitter-id/{username}')
def twitter_id(username):
    user = client.get_user(username=username)
    return f"Your twitter's id: {user[0]['id']}"


@app.get('/timeline/')
def timeline():
    timeline = client.get_home_timeline().data
    return [tweets['text'] for tweets in timeline]


@app.get('/liked-tweets/{id}')
def liked_tweets(id):
    liked_tweets = client.get_liked_tweets(id=id, max_results=20).data
    return [tweets['text'] for tweets in liked_tweets]


@app.get('/user-tweets/{id}')
def user_tweets(id):
    user_tweets = client.get_users_tweets(id=id, max_results=20).data
    return [tweets['text'] for tweets in user_tweets]


@app.get('/recent-tweets/{query}')
def recent_tweet(query):
    recent_tweets = client.search_recent_tweets(query=query, max_results=20).data
    return [tweets['text'] for tweets in recent_tweets]


uvicorn.run(app, port=5000)
