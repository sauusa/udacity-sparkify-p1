import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *

def process_song_file(cur, filepath):
    # open song file
    df = pd.read_json(filepath,typ="series")

    # insert song record
    song_data = (df.song_id,df.title,df.artist_id,df.year,df.duration)
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = (df.artist_id,df.artist_name,df.artist_location,df.artist_latitude,df.artist_longitude)
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    # open log file
    df = pd.read_json(filepath,lines=True)

    # filter by NextSong action
    df = df[df['page']=='NextSong']

    # convert timestamp column to datetime
    t = pd.to_datetime(df['ts'], unit='ms')
    
    # insert time data records
    time_data = (t, t.dt.hour, t.dt.day, t.dt.weekofyear, t.dt.month, t.dt.year, t.dt.weekday)
    column_labels = ('timestamp','hour','day','week of year', 'month', 'year', 'weekday')

    time_df = {column_labels[0] : time_data[0],
               column_labels[1] : time_data[1],
               column_labels[2] : time_data[2],
               column_labels[3] : time_data[3],
               column_labels[4] : time_data[4],
               column_labels[5] : time_data[5],
               column_labels[6] : time_data[6]
              }
    time_df = pd.DataFrame.from_dict(time_df)

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_data = {'user_id' : df.userId,
                 'first_name' : df.firstName,
                 'last_name' : df.lastName,
                 'gender' : df.gender,
                 'level'  : df.level
                }
    user_df = pd.DataFrame.from_dict(user_data)

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    songplayid = 1
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        t = pd.to_datetime(row.ts, unit='ms')
        
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (songplayid, t, row.userId, row.level, songid, artistid, row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)
        songplayid = songplayid + 1

def process_data(cur, conn, filepath, func):
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()