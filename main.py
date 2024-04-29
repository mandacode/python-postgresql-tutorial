import os

import psycopg2
import dotenv

dotenv.load_dotenv()

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')


def main():

    with psycopg2.connect(
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT
    ) as connection:
        cursor = connection.cursor()
        cursor.execute("DROP TABLE employees;")
        cursor.execute(
            "CREATE TABLE employees "
            "(id SERIAL PRIMARY KEY, first_name VARCHAR(50), last_name VARCHAR(50), email VARCHAR(100), hire_date DATE);"
        )
        print("Table 'employees' has been created.")


if __name__ == "__main__":
    main()
