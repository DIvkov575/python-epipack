import vlc
import pandas as pd
from pandas import DataFrame
import os

# import sys
import time
from mutagen.mp4 import MP4


def get_paths(directory="Assets") -> list:
    # pulls all file paths from director
    # removes spaces from all paths
    return os.listdir(directory)
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
        "name": ["NA" for _ in range(len(get_paths()))],
        "path": get_paths(),
        "bpm": ["NA" for _ in range(len(get_paths()))],
        "scale": ["NA" for _ in range(len(get_paths()))],
        "genre": ["NA" for _ in range(len(get_paths()))],
        "mood": ["NA" for _ in range(len(get_paths()))],
        "energy": ["NA" for _ in range(len(get_paths()))],
        "artist": ["NA" for _ in range(len(get_paths()))],
        "album": ["NA" for _ in range(len(get_paths()))],
        "sub-genre": ["NA" for _ in range(len(get_paths()))],
    }
)


def update_archive(current_archive=df1) -> DataFrame:
    # compare for new files in archive against current-archive (df1)
    # currently unusable -- checks auto-update df1 : updated view of `assets`
    df_output = DataFrame()
    current_path_list = current_archive["path"]
    paths_in_assets = get_paths()

    for i in range(len(paths_in_assets)):
        if paths_in_assets[i] not in current_path_list:
            df_temp = pd.DataFrame(
                    {
                        "name": ["NA"],
                        "path": [paths_in_assets[i]],
                        "bpm": ["NA"],
                        "scale": ["NA"],
                        "genre": ["NA"],
                        "mood": ["NA"],
                        "energy": ["NA"],
                        "artist": ["NA"],
                        "album": ["NA"],
                        "sub-genre": ["NA"],
                    }
                )
            pd.concat([df_output, df_temp])

    print(df_output)


update_archive()
# update_archive(df1)
