import psycopg2
import sys


def db_connect():
    try:
        conn = psycopg2.connect(database='placeholder', user='placeholder')

    except psycopg2.OperationalError as e:
        print('Unable to connect!')
        print(e)
        sys.exit(1)

    return conn.cursor()

