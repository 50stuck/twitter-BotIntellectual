import random
from intellectuals import intellectual_names
from process import post_tweet, get_player_song

# Choose name
selected_name = random.choice(list(intellectual_names.keys()))

# Find a song
selected_song = get_player_song(selected_name)

# Tweet tweet
post_tweet(selected_song)
