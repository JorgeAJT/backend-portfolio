import psycopg2


def db_connection() -> psycopg2.extensions.connection:
    print("Connecting with the db ...")

    conn = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='1234',
        host="127.0.0.1",
        port=5432
    )
    print("Successful connection!")
    return conn
