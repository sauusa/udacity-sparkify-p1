# udacity-sparkify-p1
Udacity Data-Engineering nana-degree program project #1: Data Modeling (ETL) with Postgres - Sparkify DB

Programs:
 1. create_tables.py  - Main Python script for creating & connecting the database and schema
 2. etl.py            - Main Python script to run, for data extraction, transformation and load, from Sparkify JSON source files 
 3. sql_queries.py    - Python script for SQL queries (Create/Insert/Select)
 4. test.ipynb        - Jupyter python notebook to test the results
 5. input files       - input source files are at http://millionsongdataset.com/ folders: data/song_data, data/log_data
 
 Steps:
 1. Keep all the programs at one place
 2. Run the create_tables.py (in Jupyter notebook or any Python3 IDE) to create the sparify database and related tables.
 3. Run the main program  to do the following: 
    - fetch the song data from input JSON source and load into song and artist table in Postgres
    - fetch the log data from input JSON source and load into time, user and songplay table in Postgres.
 4. Test the results using test.ipynb sql queries. 
 
 Data Flow:
    JSON Source file --> ETL --> Postgres DB 
