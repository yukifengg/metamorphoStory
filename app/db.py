import sqlite3, random as rand

DB_FILE = "data.db"

db = None

def db_connect():
    global db 
    db = sqlite3.connect(DB_FILE)
    return db.cursor()

def db_close():
    db.commit()
    db.close()
    
def db_table_inits(): #creates stories and user tables if they don't exist
    c = db_connect()
    c.execute("CREATE TABLE IF NOT EXISTS stories (id int, title text, creator text)")
    c.execute("CREATE TABLE IF NOT EXISTS story_info (id int, story_part int, story text, contributor text)")
    c.execute("CREATE TABLE IF NOT EXISTS users (username text, password text)")
    db_close()
    
#for signing up
def check_user_not_exists(username): #checks if user doesn't exist, returns True if they don't exist
    c = db_connect()
    c.execute('SELECT username FROM users WHERE username=?',(username,))
    user = c.fetchone()
    db_close()
    print(user)
    print(username)
    if user:
        return False
    return True

#for signing up
def create_new_user(username, password): #creates new user
    c = db_connect()
    c.execute('INSERT INTO users VALUES (?,?)',(username, password))
    c.execute("SELECT * from users")
    print(len(c.fetchall()))
    db_close()


#for logging in
def check_credentials(username, password): #checks if there exists username and password in db, returns True if there is
    c = db_connect()
    c.execute('SELECT username,password FROM users WHERE username=? AND password=?',(username, password))
    user = c.fetchone()
    db_close()
    if user:
        return True
    return False