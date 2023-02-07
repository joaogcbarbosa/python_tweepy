import tweepy
from keys import *

client = tweepy.Client(bearer_token=BEARER_TOKEN, consumer_key=API_KEY, consumer_secret=API_KEY_SECRET,
                       access_token=ACCESS_TOKEN, access_token_secret=ACCESS_SECRET_TOKEN)


def visualiza(msg):
    print('=' * 50)
    print(msg)
    print('=' * 50)
    print()


#Retorna informações do usuário inserido como parâmetro
user = client.get_user(username='Johnnygcb')
print(user)


#
# #Retorna os tweets curtidos do usuário
# liked_tweets = client.get_liked_tweets(id=1884689629, max_results=100)
# for liked_tweet in liked_tweets.data:
#     visualiza(liked_tweet)
#
# # Retorna as menções do usuário
# user_mentions = client.get_users_mentions(id=1884689629, max_results=100)
# for user_mention in user_mentions.data:
#     visualiza(user_mention)
#
# #Busca tweets recentes por assunto
# recent_tweets = client.search_recent_tweets(query='Andre Matos', max_results=10).data
# for tweets in recent_tweets:
#     visualiza(tweets)
#
# #Retorna os tweets do id passado como parâmetro
# user_tweets = client.get_users_tweets(id=800916529, max_results=100)
# for tweet in user_tweets.data:
#     visualiza(tweet)
