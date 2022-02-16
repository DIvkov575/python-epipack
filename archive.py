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
