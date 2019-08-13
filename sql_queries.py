# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS SONGPLAY"
user_table_drop = "DROP TABLE IF EXISTS USERS"
song_table_drop = "DROP TABLE IF EXISTS SONG"
artist_table_drop = "DROP TABLE IF EXISTS ARTIST"
time_table_drop = "DROP TABLE IF EXISTS TIME"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS SONGPLAYS(
SONGPLAY_ID SERIAL PRIMARY KEY,
START_TIME TIME NOT NULL,
USER_ID INT NOT NULL,
LEVEL TEXT,
SONG_ID TEXT,
ARTIST_ID TEXT,
SESSION_ID INT,
LOCATION TEXT,
USER_AGENT TEXT
)
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS USERS(
USER_ID INT PRIMARY KEY,
FIRST_NAME TEXT,
LAST_NAME TEXT,
GENDER CHAR(1),
LEVEL TEXT
)
""")


artist_table_create = ("""
CREATE TABLE  IF NOT EXISTS ARTISTS(
ARTIST_ID TEXT PRIMARY KEY,
NAME TEXT,
LOCATION TEXT,
LATITUDE DECIMAL,
LONGITUDE DECIMAL
)
""")


song_table_create = ("""
CREATE TABLE  IF NOT EXISTS SONGS(
SONG_ID TEXT PRIMARY KEY,
TITLE TEXT,
ARTIST_ID TEXT ,
YEAR INT,
DURATION DECIMAL NOT NULL
)
""")

time_table_create = ("""
CREATE TABLE  IF NOT EXISTS TIME(
START_TIME TIMESTAMP PRIMARY KEY,
HOURS INT,
DAY INT,
WEEK INT,
MONTH INT,
YEAR INT,
WEEKDAY TEXT
)
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO SONGPLAYS VALUES(DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING
""")

user_table_insert = ("""
INSERT INTO USERS VALUES(%s, %s, %s, %s, %s)
ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level
""")

song_table_insert = ("""
INSERT INTO SONGS VALUES(%s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING
""")

artist_table_insert = ("""
INSERT INTO ARTISTS VALUES(%s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING
""")


time_table_insert = ("""
INSERT INTO TIME VALUES(%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING
""")

# RETRIEVE SONG_ID AND ARTIST_ID BASED ON GIVEN PARAMETERS

song_select = ("""
SELECT S.song_id, A.artist_id
FROM SONGS S JOIN ARTISTS A on
S.ARTIST_ID = A.ARTIST_ID
WHERE S.title = %s and A.NAME = %s and S.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, artist_table_create, song_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
