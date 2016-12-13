import psycopg2
import sys
import json
from splitstream import splitfile


def db_connect():
    try:
        conn = psycopg2.connect(database='placeholder', user='placeholder')

    except psycopg2.OperationalError as e:
        print('Unable to connect!')
        print(e)
        sys.exit(1)

    return conn


def read_json():
    with open('file_name.json') as f:
        for json in splitfile(f, format='json'):
            yield str(json, 'utf-8')


def main():
    conn = db_connect()
    cur = conn.cursor()

    for line in read_json():
        data = json.loads(line)
        data['additional_field'] = True
        cur.execute("insert into table_name (field1, field2, additional_field) values (%(field1)s, %(field2)s, %(additional_field)s))", data)

    #cur.execute("select * from table_name")
    #rows = cur.fetchall()
    #rows = cur.rowcount
    #cur.execute('truncate table_name;')

    conn.commit()
    cur.close()
    #print(rows)


if __name__ == '__main__':

    main()

