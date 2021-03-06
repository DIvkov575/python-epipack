import pandas as pd
from pandas import DataFrame
import os
import random
from bisect import bisect_left

df1 = pd.read_csv("Tables/song-list-a.csv")


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


def countfrequency(my_list):
    freq = {}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1

    return (freq)
    print(freq)

    #-----------------------------------------#
    #-----------------------------------------#

def sort_b(song_index=df1,
           sort_type='linear-increase',
           sort_by='aggresion',
           parameter=[],
           repeat_songs=True,
           mid_point_threshhold=65,

           generic_length=10,
           increase_length=0,
           decay_length=0,
           mid_point='hold',
           hold_length='NA',
           sine_cycle_count='NA',
           sine_cycle_length='NA',
           sine_high_count='NA',
           sine_low_count='NA') -> list:
    list_of_song_names = song_index['names']
    list_of_song_paths = song_index['paths']
    #     possible_sort_types = ['linear-increase', 'linear-decrease', 'parabola-fliped', 'sine', 'built-sine']
    possible_sort_by = ['aggression', 'energy', 'ambience']
    collapsed_sort_by_values = countfrequency(song_index[sort_by])
    song_sort_by_length = len(collapsed_sort_by_values.keys)
    queue = []
    increase_queue = DataFrame()
    decrease_queue = DataFrame()
    midpoint_queue = DataFrame()
    songs_upper_thresh = DataFrame()
    songs_lower_thresh = DataFrame()


    if mid_point.lower() == 'hold':
        sine_cycle_count = 'NA'
        sine_cycle_length = 'NA'
        sine_high_count = 'NA'
        sine_low_count = 'NA'
    if mid_point.lower() == 'sine':
        hold_length = 'NA'

    # append row if value in sort by, below threshhold
    for row in song_index:
        if row[sort_by] < mid_point_threshhold:
            songs_lower_thresh.append(row)
        elif row[sort_by] >= mid_point_threshhold:
            song_lower_thresh.append(row)
        else:
            raise "bad sort by, in row"


if len(songs_lower_thresh) > 0:
    if len(song_lower_threshhold) < increase_length + decrease_length:
        if len(song_lower_threshhold) == increase_length:
            increase_queue = song_lower_threshhold.sort_by(Sort_by, axis=1, kind='merge_sort')
        if len(song_lower_threshhold) > increase_length:
            min_val = min(song_lower_threshhold[sort_by])
            max_val = max(song_lower_threshhold[sort_by])
            minmaxavg = (max_val-min_val)//increase_length
            _val_list = [i*minmaxavg for i in range(increase_length)]
            

            
        if len(song_lower_threshhold) == decrease_length:
            increase_queue = song_lower_threshhold.sort_by(Sort_by, axis=1, ascending=False, kind='merge_sort')
