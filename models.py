
# We import the function we just wrote
from database import get_connection

# A function we call only once to setup the database
def create_tables():
    
    # Opens the connection to POSTgreSQL using thecredentialsin .env file
    conn = get_connection()
    
    #  the cursor is responsible for writing and reading the contents in the database.
    cursor = conn.cursor()
    
    # This sends a raw SQL command to POSTgreSQL . The """ allows us to write across multiple lines cleanly
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            email VARCHAR(255) UNIQUE NOT NULL,
            hashed_password VARCHAR(255) NOT NULL,
            is_active BOOLEAN DEFAULT TRUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
         )
    """)
    
    # Saves the changes to the database, without this line , nothing ever gets saved to the database, I once had this bug in QuotesAPI 
    conn.commit()
    cursor.close()
    conn.close()
    print("Tables created ka katleho")

if __name__ == "__main__":
    create_tables()
    