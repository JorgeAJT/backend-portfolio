import psycopg2
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("database")


def db_connection() -> psycopg2.extensions.connection:
    logger.info("Connecting with the db ...")

    conn = psycopg2.connect(
        dbname=os.environ.get("dbname", "postgres"),
        user=os.environ.get("user", "postgres"),
        password=os.environ.get("password", "1234"),
        host=os.environ.get("host", "127.0.0.1"),
        port=5432
    )

    logger.info("Successful connection!")
    return conn
