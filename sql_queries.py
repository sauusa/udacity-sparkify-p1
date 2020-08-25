# DROP TABLES

songplay_table_drop = "drop table if exists songplays"
user_table_drop = "drop table if exists users"
song_table_drop = "drop table if exists songs"
artist_table_drop = "drop table if exists artists"
time_table_drop = "drop table if exists time"

# CREATE TABLES

songplay_table_create = ("create table if not exists songplays(songplay_id int, \
                          starttime timestamp, user_id varchar, level varchar, song_id varchar, \
                          artist_id varchar, session_id varchar, location varchar, user_agent varchar)")

user_table_create = ("create table if not exists users(user_id varchar, first_name varchar, \
                      last_name varchar, gender varchar, level varchar)")

song_table_create = ("create table if not exists songs(song_id varchar, title varchar, artist_id varchar, \
                      year int, duration float)")

artist_table_create = ("create table if not exists artists(artist_id varchar, name varchar, location varchar, \
                        latitude varchar, longitude varchar)")

time_table_create = ("create table if not exists time(start_time timestamp, hour float, day int, week int, \
                      month int, year int, weekday int)")

# INSERT RECORDS

songplay_table_insert = ("insert into songplays(songplay_id,starttime,user_id,level,song_id, artist_id, \
                          session_id, location, user_agent) \
                          values(%s,%s,%s,%s,%s,%s,%s,%s,%s) ")
                         #values('1',100,'101','1','S1','A1','SSN1','Virginia',NULL)")

user_table_insert = ("insert into users(user_id, first_name, last_name, gender, level) \
                      values(%s,%s,%s,%s,%s) ")
                     #values('101','Saurabh','Sahu','M','1')")

song_table_insert = ("insert into songs(song_id,title,artist_id,year,duration) \
                      values(%s,%s,%s,%s,%s)")
                     #values('S1','Listem to your heart','A1',1980,4.28)")

artist_table_insert = ("insert into artists(artist_id, name, location, latitude, longitude) \
                        values(%s,%s,%s,%s,%s)")
                       #values('A1','Roxette','California',NULL,NULL)")


time_table_insert = ("insert into time(start_time,hour,day,week,month,year,weekday) \
                      values(%s,%s,%s,%s,%s,%s,%s)")
                     #values(10,5,14,2,2,2020,3)")

# FIND SONGS

song_select = ("select songs.song_id, artists.artist_id from songs, artists where songs.artist_id = artists.artist_id \
                and songs.title = %s and artists.name = %s and songs.duration = %s ")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]