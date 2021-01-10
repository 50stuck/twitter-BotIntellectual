import tweepy
import random
from secrets import *
from sylco import sylco
from intellectuals import intellectual_names
from song_template import player_songs_dict, get_song_lyrics
from process import post_tweet, get_name_tuple, get_player_song

def intellectuals_with_missing_songs():
    missing_songs = 0
    missing_songs_names = []

    for name in intellectual_names:
        en_name = intellectual_names.get(name, 'NaN')
        name_tuple = get_name_tuple(en_name)
        selected_song = random.choice(player_songs_dict.get(name_tuple, ['אין שיר']))

        if selected_song == 'אין שיר':
            missing_songs += 1
            missing_songs_names.append(name)

    return missing_songs, missing_songs_names

def songs_with_missing_lyrics():
    missing_lyrics = 0
    missing_lyrics_songs = []

    for syls in player_songs_dict:
        for song in player_songs_dict[syls]:
            test_lyrics = get_song_lyrics(song, 'test', 'test')

            if test_lyrics == '':
                missing_lyrics += 1
                missing_lyrics_songs.append(song)

    return missing_lyrics, missing_lyrics_songs

def main():
    print("looking for intellectuals_with_missing_songs")
    num_intell, detail_intell = intellectuals_with_missing_songs()
    print(f"found {num_intell} intellectuals with no song to match: {detail_intell}")

    print("looking for songs_with_missing_lyrics")
    num_songs, detail_songs = songs_with_missing_lyrics()
    print(f"found {num_songs} songs with no lyrics to match: {detail_songs}")

main()
