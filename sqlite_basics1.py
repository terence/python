#!/usr/local/bin/python3

print ("Hello World")

import sys
print (sys.path)
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()


def create_table(conn, create_table_sql):
# create a table from the create_table_sql statement
# :param conn: Connection object
# :param create_table_sql: a CREATE TABLE statement
# :return:
	try:
		c = conn.cursor()
		c.execute(create_table_sql)
		print ("Table created")
	except Error as e:
		print(e)



def main():
    database = "data/sqlite1.db"
 
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """
 
    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    priority integer,
                                    status_id integer NOT NULL,
                                    project_id integer NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text NOT NULL,
                                    FOREIGN KEY (project_id) REFERENCES projects (id)
                                );"""
 
    # create a database connection
    #conn = create_connection("data/sqlite1.db")
    conn = sqlite3.connect(database)
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)
        # create tasks table
        create_table(conn, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")

 
if __name__ == '__main__':
	main()






