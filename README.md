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
