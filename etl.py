import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries

'''
loading of the data from the S3 buckets to Redshift.
"copy_table_queries" is getting used in "sql_ueries.py".
'''
def load_staging_tables(cur, conn):
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()

'''
Insert the data from the staging tables to the domension and fact tables.
"insert_table_queries" is getting used in "sql_ueries.py".
'''
def insert_tables(cur, conn):
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()