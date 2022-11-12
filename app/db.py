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
    c.execute("CREATE TABLE IF NOT EXISTS stories (id int, title text)")
    # c.execute("CREATE TABLE IF NOT EXISTS story_info (id int, story text, story_part text")
    c.execute("CREATE TABLE IF NOT EXISTS users (username text, password text)")
    db_close()

def check_story_not_exists(story):
    return True

def create_new_story(title, username, text):
    if check_story_not_exists(title):
        c = db_connect()
        contributer_table_name = title + "_contributors"
        story_part = title + "_parts"
        c.execute('INSERT INTO stories VALUES (?,?)',(23, title))
        c.execute(f'CREATE TABLE IF NOT EXISTS {contributer_table_name} (contributors text)')
        c.execute(f'CREATE TABLE IF NOT EXISTS {story_part} (story_part text)')
        c.execute(f'INSERT INTO {contributer_table_name} VALUES (\'{username}\')')
        c.execute(f'INSERT INTO {story_part} VALUES (\'{text}\')')
        # add_to_story(title, username, text)
        db_close()

def add_to_story(title, username, text): 
    c = db_connect()
    
    # c.execute('INSERT INTO story_info VALUES (?,?,?,?)',(23, username, ))

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