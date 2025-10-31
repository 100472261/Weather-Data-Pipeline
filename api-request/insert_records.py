import psycopg2
from api_request import fake_fetch_data, fetch_data

def connect_to_database():
    print("Connecting to the PostgreSQL database...")
    try:
        connection = psycopg2.connect(
            dbname="db",
            user="db_user",
            password="db_password",
            host="db",
            port=5432
        )
        return connection
    except psycopg2.Error as e:
        print(f"Error connecting to database: {e}")
        raise

def create_table(connection):
    print("Creating table if it doesn't exist...")
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE SCHEMA IF NOT EXISTS dev;
            CREATE TABLE IF NOT EXISTS dev.raw_weather_data (
                id SERIAL PRIMARY KEY,
                city TEXT,
                temperature FLOAT,
                weather_description TEXT,
                wind_speed FLOAT,
                time TIMESTAMP,
                inserted_at TIMESTAMP DEFAULT NOW(),
                utc_offset TEXT
            );
        """)
        connection.commit()
        print("Table was created successfully.")
    except psycopg2.Error as e:
        print(f"Error creating the table: {e}")
        raise

def insert_records(connection, data):
    print("Inserting weather data into the database...")
    try:
        weather = data['current']
        location = data['location']
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO dev.raw_weather_data (
                city,
                temperature,
                weather_description,
                wind_speed,
                time,
                inserted_at,
                utc_offset
            ) VALUES (%s, %s, %s, %s, %s, NOW(), %s)
        """,(
            location['name'],
            weather['temperature'],
            weather['weather_descriptions'][0],
            weather['wind_speed'],
            location['localtime'],
            location['utc_offset']
        ))
        connection.commit()
        print("Data were inserted successfully.")
    except psycopg2.Error as e:
        print(f"Error inserting data: {e}")
        raise

def main():
    try:
        data = fetch_data()
        connection = connect_to_database()
        create_table(connection)
        insert_records(connection, data)
    except Exception as e:
        print(f"An error has occurred during the execution: {e}")
    finally:
        if 'connection' in locals():
            connection.close()
            print("Database connection closed.")