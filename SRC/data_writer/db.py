import mysql.connector
from mysql.connector.abstracts import MySQLCursorAbstract, MySQLConnectionAbstract

from SRC.data_generator import generate_all
from SRC.data_writer.util import read_sql_file, info
from SRC.secrets import db_pswd

DB_NAME = 'test'

def create_db(auto_delete=False) -> (MySQLConnectionAbstract, MySQLCursorAbstract):
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd=db_pswd
        )
        c = db.cursor()
        c.execute(f'CREATE DATABASE {DB_NAME}')
        return db, c
    except mysql.connector.errors.DatabaseError as e:
        info('Cannot create database, db already exists.')
        if not auto_delete:
            yorn = input('Drop & continue? (y/n): ')
            if yorn.lower() != 'y':
                raise Exception("Database exists, cannot continue.")

        print('Deleting and recreating db...')
        c.execute(f'DROP DATABASE {DB_NAME}')
        c.execute(f'CREATE DATABASE {DB_NAME}')
        return db, c

def create_tables(cursor: MySQLCursorAbstract) -> None:
    command = read_sql_file('ex2.sql')
    cursor.execute(f'USE {DB_NAME}')
    cursor.execute(command)

def populate(cursor: MySQLCursorAbstract, data) -> None:
    print(data)

def main(data):
    try:
        print('connecting to server...')
        connection, cursor = create_db(auto_delete=True)

        print('adding tables...')
        create_tables(cursor)

        print('populating data...')
        populate(cursor, data)
    except Exception as e:
        print(e)
        print('rolling back...')
        connection.rollback()
    finally:
        print('closing connection...')
        cursor.close()
        connection.close()

if __name__ == '__main__':
    main()