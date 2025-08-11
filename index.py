#kano
import tweepy
import json
import time

api_key = ''
api_secret = ''
access_token = ''
access_token_secret = ''
BEARER_TOKEN = ''

# Autenticación con Twitter
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

ruta_archivo_tweets = 'tweets/tweets.js'

def leer_tweets(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
        contenido_json = contenido[contenido.index('['):]
        tweets = json.loads(contenido_json)
        return tweets

def eliminar_tweet(tweet_id):
    try:
        api.destroy_status(tweet_id)
        print(f"Eliminado tweet con ID: {tweet_id}")
    except tweepy.errors.NotFound:
        print(f"Tweet con ID {tweet_id} no encontrado o ya eliminado.")
    except tweepy.errors.Forbidden as e:
        print(f"No se puede eliminar el tweet con ID {tweet_id}. Error: {e}")
    except tweepy.errors.TweepyException as e:
        print(f"Error al eliminar tweet con ID: {tweet_id} - {e}")

if __name__ == "__main__":
    tweets = leer_tweets(ruta_archivo_tweets)

    for tweet in tweets:
        tweet_id = tweet['tweet']['id']
        eliminar_tweet(tweet_id)
        time.sleep(0.5)

    print("Proceso completado.")
