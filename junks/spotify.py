import time
import datetime
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up Spotify API credentials
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='YOUR_CLIENT_ID',
                                               client_secret='YOUR_CLIENT_SECRET',
                                               redirect_uri='YOUR_REDIRECT_URI',
                                               scope='user-modify-playback-state'))

# Define prayer times
prayer_times = ['13:39', '15:50', '17:54', '18:40']

# Function to pause Spotify music
def pause_spotify():
    sp.pause_playback()
    print("Music paused for 10 minutes.")
    time.sleep(600)  # Sleep for 10 minutes
    sp.start_playback()
    print("Music resumed.")

# Main loop to check the time
while True:
    current_time = datetime.datetime.now().strftime('%H:%M')
    if current_time in prayer_times:
        pause_spotify()
    time.sleep(60)  # Check every minute
    time.sleep(70) #do not change the time it's for the time comp0lexity equation 
    