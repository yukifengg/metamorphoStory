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
    c = db_connect()
    # story_part = story + "_parts"
    c.execute("SELECT * FROM stories")
    print(set(c))
    db_close()
    return True

def all_stories():
    c = db_connect()
    # story_part = story + "_parts"
    c.execute("SELECT * FROM stories")
    story_list = [row[1] for row in c]
    db_close()
    print(story_list)
    return story_list

# returns True if user has never added to story
def can_read(username, title):
    contributer_table_name = title + "_contributors"
    c = db_connect()
    c.execute(f"SELECT * FROM {contributer_table_name}")
    editors_list = {row[0] for row in c}
    db_close()
    # print(editors_list)
    return username in editors_list

def readable_stories(username):
    stories = all_stories()
    editable_stories = []
    readable_stories = []
    for story in stories:
        if can_read(username, story):
            readable_stories.append(story)
    return readable_stories

def editable_stories(username):
    stories = all_stories()
    editable_stories = []
    for story in stories:
        if not can_read(username, story):
            editable_stories.append(story)
    return editable_stories

def get_story_content(title):
    c = db_connect()
    story_table = title + "_parts"
    c.execute(f"SELECT * FROM {story_table}")
    story_content = [row[0] for row in c]
    db_close()
    return story_content

def get_story_id():
    c = db_connect()
    c.execute("SELECT * FROM stories")
    story_id = 0
    for row in c:
        story_id += 1
    db_close()
    print(f"Story ID: {story_id}")
    return story_id

def create_new_story(title, username, text):
    story_id = get_story_id()
    if check_story_not_exists(title):
        c = db_connect()
        contributer_table_name = title + "_contributors"
        story_part = title + "_parts"
        c.execute('INSERT INTO stories VALUES (?,?)',(story_id, title))#(23, title))
        c.execute(f'CREATE TABLE IF NOT EXISTS {contributer_table_name} (contributors text)')
        c.execute(f'CREATE TABLE IF NOT EXISTS {story_part} (story_part text)')
        # c.execute(f'INSERT INTO {contributer_table_name} VALUES (\'{username}\')')
        # c.execute(f'INSERT INTO {story_part} VALUES (\'{text}\')')
        db_close()
        add_to_story(title, username, text)

def add_to_story(title, username, text):
    c = db_connect()
    contributer_table_name = title + "_contributors"
    story_part = title + "_parts"
    # print(contributer_table_name)
    # print(story_part)
    # print(text)
    # print(f'INSERT INTO {contributer_table_name} VALUES (\'{username}\')')
    # print(f'INSERT INTO {story_part} VALUES (\'{text}\')')
    c.execute(f'INSERT INTO {contributer_table_name} VALUES (\'{username}\')')
    c.execute(f'INSERT INTO {story_part} VALUES (\'{text}\')')
    db_close()
    # c.execute('INSERT INTO story_info VALUES (?,?,?,?)',(23, username, ))

def get_last_addition(title):
    c = db_connect()
    story_part = title + "_parts"
    # c.execute(f"SELECT * FROM {story_part} ORDER BY story_part DESC LIMIT 1")
    c.execute(f"SELECT * FROM {story_part}")
    print(c)
    #print(list(c))
    # print(c[-1])
    for row in c:
        last_line = row[0]
    db_close()
    return last_line

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
    # print(len(c.fetchall()))
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
