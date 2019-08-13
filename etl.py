import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *
import datetime as dt


def process_song_file(cur, filepath):
    """
    Summary: Process Song Data file and insert data into Songs and Artists tables.

    Parameters:
        cur (Object): Database cursor object.
        filepath (string): Path of the file
    """

    # Read the json file in filepath and store as a dataframe in variable df
    df = pd.read_json(filepath, lines=True)

    # Extract Song table attributes and insert into Songs Table
    song_data = [df['song_id'][0], df['title'][0], df['artist_id'][0], int(df['year'][0]), float(df['duration'][0])]
    cur.execute(song_table_insert, song_data)

    # Extract Artist table attributes and insert into Artists Table
    artist_data = [df['artist_id'][0], df['artist_name'][0], df['artist_location'][0], df['artist_latitude'][0], df['artist_longitude'][0]]
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """
    Summary: Process Log Data file and inserts data into Time, Users and Songplay tables.

    Parameters:
        cur (Object): Database cursor object.
        filepath (string): Path of the file.
    """

    # Read the json file in filepath and store as a dataframe in variable df.
    df = pd.read_json(filepath, lines=True)

    # Filtering songs by NextSong action.
    df2 = df[df.page == 'NextSong']

    # Converting timestamp value in milliseconds to readable format.
    t = df2['ts']/1000.0
    t = t.apply(dt.datetime.fromtimestamp)

    # Extracting time data and preparing to insert into a Dataframe.
    time_data = (t, t.dt.hour, t.dt.day, t.dt.week, t.dt.month, t.dt.year, t.dt.weekday)
    column_labels = ['Start_Time', 'Hours', 'Day', 'Week', 'Month', 'Year', 'Weekday']
    d={}
    for i,col in enumerate(column_labels):
       d[col] =  time_data[i]

    # Time Data is read from data frame row by row and inserted into table.
    time_df = pd.DataFrame(d)
    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # Extracting user data and preparing to insert into a Dataframe.
    user_df_ip = {"userId": df.userId, "firstName": df.firstName, "lastName": df.lastName, "gender": df.gender, "level": df.level}
    user_df = pd.DataFrame(user_df_ip)

    # Dropping any NaN.
    user_df = user_df.dropna()

    # Inserting into User table.
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # Insert data into Songplay table
    df = df.dropna()
    for i,row in df.iterrows():

        # Get song_id and artist_id by querying based on song_title, artist_name, song_duration
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()

        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # Insert into Songplay table
        songplay_data = (dt.datetime.fromtimestamp(row.ts/1000.0), row.userId, row.level, songid, artistid, row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)



def process_data(cur, conn, filepath, func):
    """
    Summary: Extract data residing in given filepath and apply given function

    Parameters:
        cur (Object): Database cursor object.
        conn (Object): Database connection object.
        filepath (string): Path of the file.
        func (function): Function to be applied on the data.
    """
    # Get all the files in the given path
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # Get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # Iterate over files and process and apply function specified
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
