import pandas as pd
from pandas import DataFrame
import os

# import sys
import time
from mutagen.mp4 import MP4


def get_asset_names(directory="Assets") -> list:
    # pulls all file paths from director
    # removes spaces from all paths
    return os.listdir(directory)


def get_asset_paths(song_name_list, rename_origin_asset=False) -> list:
    # return song names cleaned -> usable paths
    path_list_out = []
    for song_in in song_name_list:
        if " " or "/" in song_in:
            song_out = song_in.replace(" ", "")
            song_out = song_out.replace("/", "")
            path_list_out.append(song_out)

            if rename_origin_asset:
                os.rename(
                    os.path.join("Assets", song_in), os.path.join("Assets", song_out)
                )
    return path_list_out


# does not work
def update_archive(current_archive=DataFrame()) -> DataFrame:
    # compare for new files in archive against current-archive (df1)
    # currently unusable -- checks auto-update df1 : updated view of `assets`
    df_output = DataFrame()
    current_path_list = current_archive["path"]
    paths_in_assets = get_asset_names()

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

# df1.to_csv('Tables/song-list-a.csv')
# df2 = pd.read_csv("Tables/song-list-a.csv")
# print(df2.columns)
# print([df2[a] for a in df2.columns])
