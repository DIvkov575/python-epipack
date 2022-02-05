import vlc
import pandas as pd
from pandas import DataFrame
import os

# import sys
import time
from mutagen.mp4 import MP4


def get_names() -> list:
    # makes sure names are not only " " or "/"
    # returns list of all song names ^^
    list_song_names = os.listdir("Assets")
    final_list_song_names = []

    for song in list_song_names:
        if " " in song:
            char_list = list(song)
            char_list = set(char_list)
            if len(char_list) == 1:
                print("file w/ ' ' char only")
                print(song)
            else:
                final_list_song_names.append(song)

        if "/" in song:
            char_list = set(list(song))
            if len(char_list) == 1:
                print("file w/ '/' char only")
                print(song)
            else:
                final_list_song_names.append(song)
        else:
            final_list_song_names.append(song)
    return final_list_song_names


def convert_names_to_path(song_list, rename_asset=True) -> list:
    # return song names cleaned -> usable paths
    path_list_out = []
    for song_in in song_list:
        if " " or "/" in song_in:
            song_out = song_in.replace(" ", "")
            song_out = song_out.replace("/", "")
            path_list_out.append(song_out)
            if rename_asset:
                os.rename(
                    os.path.join("Assets", song_in), os.path.join("Assets", song_out)
                )

    return path_list_out


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
        "name": get_names(),
        "path": convert_names_to_path(get_names()),
        "bpm": ["NA" for _ in range(len(get_names()))],
        "scale": ["NA" for _ in range(len(get_names()))],
        "genre": ["NA" for _ in range(len(get_names()))],
        "mood": ["NA" for _ in range(len(get_names()))],
        "energy": ["NA" for _ in range(len(get_names()))],
        "artist": ["NA" for _ in range(len(get_names()))],
        "album": ["NA" for _ in range(len(get_names()))],
        "sub-genre": ["NA" for _ in range(len(get_names()))],
    }
)


def update_archive(current_archive) -> DataFrame:
    # compare for new files in archive against current-archive (df1)
    #
    df_output = DataFrame
    current_path_list = current_archive["path"]
    current_name_list = current_archive["name"]
    assets_drive = convert_names_to_path(get_names())

    for i in range(len(assets_drive)):
        if assets_drive[i] not in current_path_list:
            print("added")
            df_temp = pd.DataFrame(
                    {
                        "name": assets_drive[i],
                        "path": convert_names_to_path(assets_drive[i], rename_asset=False),
                        "bpm": "",
                        "scale": "",
                        "genre": "",
                        "mood": "",
                        "energy": "",
                        "artist": "",
                        "album": "",
                        "sub-genre": "",
                    }
                )
            df_output.append(df_temp)

    print(df_output)


update_archive(df1)
