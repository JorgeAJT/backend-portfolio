import psycopg2
import logging

def database_connection() -> psycopg2.extensions.connection:
    logging.info("Connecting with the db ...")

    conn = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='1234',
    )
    logging.info("Successful connection!")
    return conn