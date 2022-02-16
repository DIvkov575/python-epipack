import vlc
import pandas as pd
from pandas import DataFrame
import os

import sys
import time
from mutagen.mp4 import MP4


def play_song(path):
    try:
        song = MP4(path)
        song_duration = song.info.length
    except Exception as e:
        print(e)
        song_duration = 180
    try:
        song = vlc.MediaPlayer(path)
        song.play()
        time.sleep(song_duration)
    except Exception as e:
        print(e)


df1 = pd.DataFrame(
    {
        "name": ["NA" for _ in range(len(get_asset_names()))],
        "path": get_asset_names(),
        "bpm": ["NA" for _ in range(len(get_asset_names()))],
        "scale": ["NA" for _ in range(len(get_asset_names()))],
        "genre": ["NA" for _ in range(len(get_asset_names()))],
        "mood": ["NA" for _ in range(len(get_asset_names()))],
        "energy": ["NA" for _ in range(len(get_asset_names()))],
        "artist": ["NA" for _ in range(len(get_asset_names()))],
        "album": ["NA" for _ in range(len(get_asset_names()))],
        "sub-genre": ["NA" for _ in range(len(get_asset_names()))],
    }
)

a = range(len(get_asset_names()))
df1 = pd.DataFrame(
    {
        "name": ["NA" for _ in a],
        "path": get_asset_paths(get_asset_names()),
        "bpm": ["NA" for _ in a],
        "genre": ["NA" for _ in a],
        "mood": ["NA" for _ in a],
        "energy": ["NA" for _ in a],
        "artist": ["NA" for _ in a],
        "album": ["NA" for _ in a],
        "sub-genre": ["NA" for _ in a],
    }
)
df3 = pd.DataFrame(
    {
        "name": ["NA" for _ in a],
        "Artist": ["NA" for _ in a],
        "path": get_asset_paths(get_asset_names()),
        "bpm": ["NA" for _ in a],
        "genre": ["NA" for _ in a],
        "sub-genre": ["NA" for _ in a],
        "agression": ["NA" for _ in a],

    }
)


def sort_a(song_index=df1,
           sort_type='linear-increase',
           sort_by='aggresion',
           parameter=[],
           repeat_songs=True,
           increase_time=6,
           increase_length=2,
           hold_time=20,
           hold_length=5,
           sine_cycle_count=3,
           sine_cycle_length=5,
           sine_high_count=2,
           sine_low_count=3,
           decay_time=10,
           decay_length=3, ):

    list_of_song_names = song_index['names']
    possible_sort_types = ['linear-increase', 'linear-decrease', 'parabola-fliped', 'sine', 'built-sine']
    possible_sort_by = ['aggression', 'energy', 'ambience']
    # Possible_parameters = [increase - time, increase - length, hold, sine, decrease - length, decrease - time,
    #                        sine - cylce]

    collapsed_sort_by_values = countfrequency(song_index[sort_by])
