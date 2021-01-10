import tweepy
from secrets import *
from intellectuals import intellectual_names
from sylco import sylco
import random
from song_template import player_songs_dict, get_song_lyrics

def post_tweet(tweet_content):
    auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
    auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
    api = tweepy.API(auth)

    api.update_status(tweet_content)
    return f"posted tweet: {tweet_content}"

def get_name_tuple(name):
    name_list = name.split(' ')
    name_tuple = ()
    for name_part in name_list:
        name_tuple += (sylco(name_part),)
    return name_tuple

def get_player_song(name):
    en_name = intellectual_names.get(name, 'NaN')
    name_tuple = get_name_tuple(en_name)
    selected_song = random.choice(player_songs_dict.get(name_tuple, ['אין שיר']))
    name1, name2 = name.split(' ')

    song_lyrics = get_song_lyrics(selected_song, name1, name2)

    return (f"""
     שיר השחקן של {name} הוא {selected_song}

     {song_lyrics}
    """)
