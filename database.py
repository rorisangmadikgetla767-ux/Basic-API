import psycopg2 
from dotenv import load_dotenv
import os

load_dotenv()

# psycopg2.connect takes named arguments and each one maps to a value in the .env file
# os.getenv("DB_HOST") reads the value from .env file at runtime. So that the actual password never appears in the code
def get_connection():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER")
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")   
    )
    
    # return conn hands the connection back to whoever called get_connection() so they can use it to run queries.
    return conn