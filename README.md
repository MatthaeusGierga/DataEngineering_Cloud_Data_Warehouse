# Introduction

A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in two ``S3 Buckets``, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

The data is stored in two public S3 buckets. One bucket contains data about songs and artists that are getting listened to. The other bucket contains data about the activities of the users, e.g. the songs a user was listening to. To store the data efficiently we are using a cloud data warehouse which is widely used. We are going to store the data in a ``Redshift Cluster`` and combine it with the ``STAR schema`` which will support answering analytical questians like:   
* what song would a user of Sparkify like to hear next based on his song history (what he was listening to)
* what kind of songs would a user of Sparkify like to listen to depending on the time of the day or region
* do the payed and free user behave differently regarding songs and artists?
* a lot of more business cases... 

# Approach
Instead of using JSON-Files to store the data, it is recomended to create a cloud database to store the data and to be able to process analytical querys. An efficiant way to do it is the STAR schema. The STAR schema consists of one fact table and multiple dimension tables, which are connected to the fact table. In this specific szenario we created the following tables:

### Fact table: 
**songplays**: consists the keys to each dimension table and facts 

### Dimension tables:
**users**, **song**, **artist**, **time**: each dimension table consist of one primary key which is linked to the fact table and attributes that discribe the data of the specific table - for example all the necessary data of an song like name, artist and year.

### ETL pipeline
1. sql_queries.py
Consists of all the necessary functions and sql-querys for deleting existing tables, creating new tables and insert data into the defined tables. All the fact-, dimension tabeles and insert querys are defined in this file.

2. create_tables.py
Basic python file for dropping existing tables and create new tables that are defined in the 'sql_queries.py'.

3. dwh.cfg
Config file with all the necessary configuration atributes for connectiong to the S3 buckets and processing the data into Redshift. 

4. etl.py
Loads all log- and song data from the S3 buckets into Redshift staging tables and inserts the data into the fact and dimension tables that are defined in the 'sql_queries.py'.

5. run.ipynb
Final python file to call the **create_tables.py** and **etl.py**.

### Prerequirements
To be able to run the script it is necassary to have some prerequirements. 
The data is getting provided via two ``S3 Buckets``, but to store the data it is required to have a ``AWS Redshift Cluster`` created and running. 
Additionaly you will need to use an ``IAM Role`` authirozation role with ``AmazonS3ReadOnlyAccess``. All this information needs to be entered and stoerd into the ``dqh.cfg`` file. 