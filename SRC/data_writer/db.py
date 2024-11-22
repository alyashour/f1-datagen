import logging

import mysql.connector
from mysql.connector.abstracts import MySQLConnectionAbstract

from SRC.data_generator.models import MainRace, PitStop, QualificationRace
from SRC.data_writer.sql_commands import *
from SRC.data_writer.util import read_sql_file, info
from SRC.secrets import db_pswd
from SRC.util import DRIVERS, CIRCUITS, CONSTRUCTORS, DRIVER_ENTRIES, GRAND_PRIX, MAIN_RACES, PIT_STOPS, QUALIFICATION_RACES, QUALIFYING_RESULTS, \
    RACE_RESULTS, SEASONS

DB_NAME = 'test'
EXPECTED_NUM_TABLES = 11

def create_db(auto_delete=False) -> MySQLConnectionAbstract:
    # create connection
    with mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=db_pswd
    ) as connection:
        try:
            # try to create db
            with connection.cursor() as c:
                c.execute(f'CREATE DATABASE {DB_NAME}')
        except mysql.connector.errors.DatabaseError:
            info('Cannot create database, db already exists.')

            # ask the user to drop or no
            if not auto_delete:
                yorn = input('Drop & continue? (y/n): ')
                if yorn.lower() != 'y':
                    raise Exception("Database exists, cannot continue.")
            else:
                print(f'AUTO DELETE ON!', end=' ')
            print('Deleting and recreating db...')

            # delete the old db & create a new one
            # effectively resetting the data
            with connection.cursor() as c:
                c.execute(f'DROP DATABASE {DB_NAME}')
                c.execute(f'CREATE DATABASE {DB_NAME}')
        return mysql.connector.connect(
            host="localhost",
            user="root",
            passwd=db_pswd,
            database=DB_NAME
        )

def create_tables(connection: MySQLConnectionAbstract) -> None:
    commands = read_sql_file('ex2.sql')

    with connection.cursor() as cursor:
        cursor.execute(f'USE {DB_NAME}')
        for command in commands.split(';'):
            if 'CREATE TABLE' in command:
                cursor.execute(command)

    count = 0
    connection.reconnect()
    with connection.cursor() as cursor:
        # Query to list all tables
        cursor.execute("SHOW TABLES;")

        # Fetch and print all tables
        for _ in cursor:
            count += 1
        print('- TABLE COUNT: ', count)
        assert count == EXPECTED_NUM_TABLES, 'Incorrect number of generated tables'

def populate(connection: MySQLConnectionAbstract, data) -> None:
    connection.reconnect()
    with connection.cursor() as cursor:
        # to reduce updates insert data in order of increasing dependency
        # INSERT independent data (drivers, constructors, seasons, circuits)
        # CIRCUITS
        print('- circuits...', end='')
        # get data
        vals = [(circuit.id, circuit.name, circuit.country) for circuit in data[CIRCUITS]]
        # execute commands
        cursor.executemany(INSERT_CIRCUIT, vals)
        print('done ✅')

        # CONSTRUCTORS
        print('- constructors...', end='')
        # get data
        vals = [(c.id, c.name, c.country, c.date_of_first_debut, c.total_championships, c.total_race_entries, c.total_race_wins, c.total_points)
                for c in data[CONSTRUCTORS]]
        # execute commands
        cursor.executemany(INSERT_CONSTRUCTOR, vals)
        print('done ✅')

        # DRIVERS
        print('- drivers...', end='')
        # get data
        vals = [(driver.id, driver.name, driver.dob, driver.dod, driver.gender,
                 driver.country_of_birth, driver.total_championships, driver.total_race_entries,
                 driver.total_race_wins, driver.total_points) for driver in data[DRIVERS]]
        # execute commands
        cursor.executemany(INSERT_DRIVER, vals)
        print('done ✅')

        # SEASONS
        print('- seasons...', end='')
        # get data
        vals = [(s.id, s.driver_winner, s.constructor_winner) for s in data[SEASONS]]
        # execute commands
        cursor.executemany(INSERT_SEASON, vals)
        print('done ✅')

        # INSERT FIRST LEVEL DATA (DRIVER ENTRIES AND GRAND PRIX)

        # DRIVER ENTRIES
        print('- driver entries...', end='')
        # get data
        vals = [(de.id, de.driver_id, de.constructor_id, de.season_id, de.start_date, de.end_date, de.driver_role) for de in data[DRIVER_ENTRIES]]
        # execute commands
        cursor.executemany(INSERT_DRIVER_ENTRY, vals)
        print('done ✅')

        # GRAND PRIX
        print('- grand prix...', end='')
        # get data
        vals = [(gp.id, gp.circuit_id, gp.season_id, gp.qual_id, gp.race_id, gp.name, gp.qualifying_format.__str__()) for gp in data[GRAND_PRIX]]
        # execute commands
        cursor.executemany(INSERT_GRAND_PRIX, vals)
        print('done ✅')

        # INSERT SECOND LEVEL DATA (QUALIFYING RACE AND MAIN RACE)

        # QUALIFICATION RACE
        print('- qualification races...', end='')
        # get data
        vals = [(qr.id, qr.grand_prix_id, qr.date) for qr in data[QUALIFICATION_RACES]]
        # execute commands
        cursor.executemany(INSERT_QUALIFICATION_RACE, vals)
        print('done ✅')

        # MAIN RACE
        print('- main races...', end='')
        # get data
        vals = [(mr.id, mr.grand_prix_id, mr.date) for mr in data[MAIN_RACES]]
        # execute commands
        cursor.executemany(INSERT_MAIN_RACE, vals)
        print('done ✅')

        # INSERT THIRD LEVEL DATA (QUALIFYING RESULT AND RACE RESULT

        # QUALIFYING RESULTS
        print('- qualifying results...', end='')
        # get data
        vals = [(qr.id, qr.driver_id, qr.qualifying_id, qr.best_time, qr.gap, qr.position) for qr in data[QUALIFYING_RESULTS]]
        # execute commands
        cursor.executemany(INSERT_QUALIFYING_RESULT, vals)
        print('done ✅')

        # RACE RESULT
        print('- race results...', end='')
        # get data
        vals = [(rr.id, rr.race_id, rr.driver_id, rr.constructor_id, rr.position, rr.points_gain_loss, rr.total_pit_stops) for rr in data[RACE_RESULTS]]
        # execute commands
        cursor.executemany(INSERT_RACE_RESULT, vals)
        print('done ✅')

        # INSERT FOURTH LEVEL DATA (PIT STOP)
        # PIT STOPS
        print('- pit stops...', end='')
        # get data
        vals = [(ps.id, ps.race_id, ps.driver_id, ps.lap_number, ps.time_in_pit) for ps in data[PIT_STOPS]]
        # execute commands
        cursor.executemany(INSERT_PIT_STOP, vals)
        print('done ✅')

    # commit results
    connection.commit()

def main(data):
    connection = None
    try:
        print('connecting to server...')
        connection = create_db(auto_delete=True)

        print('adding tables...')
        create_tables(connection)

        print('populating data...')
        populate(connection, data)
    except Exception as e:
        print('Error:', e)
        print('rolling back...')
        connection.rollback()
    finally:
        print('closing connection...')
        connection.close()

if __name__ == '__main__':
    main()