import mysql.connector

def connect_to_mysql():
    try:
        db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '@Abdo010',
        )
        print("Successfully connected to MySQL database")
    except mysql.connector.Error as er:
        print(f"Error connecting to MySQL database: {er}")
        return None
    
    mycursor = db.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    db.commit()
    print("Database 'alx_book_store' created successfully!")
    mycursor.close()
    db.close()

connect_to_mysql()

