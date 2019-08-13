# Sparkify Data Analysis
## Purpose
The entire data of Sparkify resides in JSON Files which makes it difficult to query and interpret. Also, it is difficult to handle conditions like missing values, duplicates, etc. To make this easy, we will use a Star Schema to store the data in various dimensional tables and one fact table that has consolidated data. 

## Schema
Two sources of data are given in form of JSON. One is the song data which has information regarding songs and artists. The other data source has log information regarding songs played by different users. These data sources are aggregated and a start schema is developed with 
- Fact Table: Songplay
- Dimensional Tables:
    - Users
    - Songs
    - Artists
    - Time
 
The data is stored in **PostgreSQL** RDBMS. 

## How to Run? 
All the code has been written in python. 
This repository has 3 scripts 
- sql_queries.py: This script has all the create, drop and insert queries. This will be imported in other two scripts and helps in modularizing the project.  
- create_tables.py: This script has to be run before executing any other script. We first obtain a PostgreSQL DB connection and a cursor. We then drop the database if it exists and create a new one. Tables are first dropped if they exist and then created. This prepares our database for the ETL operations we do. 
- etl.py: This script is used in extracting the data from JSON files and inserting them into respective tables. 

## Results
### Before ETL - Sample input JSON Data

#### Songs Data - 
![Image of Song JSON Data](/images/songs_json.png)  

#### Log Data - 
![Image of Log JSON Data](/images/log_json.png)  


### After ETL - Sample data from tables

#### Songs Table - 
![Image of Songs Data](/images/songs.png) 

#### Artists Table - 
![Image of Artists Data](/images/artists.png) 

#### Time Table - 
![Image of Time Data](/images/time.png) 

#### Users Table - 
![Image of User Data](/images/users.png) 

#### SongPlay Fact Table - 
![Image of SongPlay Fact Data](/images/songplays.png) 

