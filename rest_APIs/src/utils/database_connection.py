import psycopg2
from .logger import setup_logger

logger = setup_logger("database")

def database_connection() -> psycopg2.extensions.connection:
    logger.info("Connecting with the db ...")

    conn = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='1234',
    )
    logger.info("Successful connection!")
    return conn
