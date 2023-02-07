import tweepy
import uvicorn
from fastapi import FastAPI
from keys import *

app = FastAPI()
client = tweepy.Client(bearer_token=BEARER_TOKEN, consumer_key=API_KEY, consumer_secret=API_KEY_SECRET,
                       access_token=ACCESS_TOKEN, access_token_secret=ACCESS_SECRET_TOKEN)


@app.get('/{id}')
def home(id):
    user = client.get_user(id=id).data
    return f'Hello, {user}!'


@app.get('/timeline/')
def timeline():
    timeline = client.get_home_timeline().data
    return timeline


@app.get('/liked-tweets/{id}')
def liked_tweets(id):
    liked_tweets = client.get_liked_tweets(id=id, max_results=100).data
    return liked_tweets


uvicorn.run(app, port=5000)
