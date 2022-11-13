from flask import Flask,render_template,session,request
import secrets
from db import *


app = Flask(__name__)

app.secret_key = secrets.token_bytes(32)

@app.route('/')
def home():
    if 'username' in session:
        return render_template('profile.html')
    return render_template('frontpage.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('username')
    return render_template('frontpage.html')

@app.route('/create', methods=["POST"])
def create_story():
    db_table_inits()
    title = request.form['title']
    username = session['username']
    text = request.form['content']
    print(title)
    print(username)
    print(text)
    create_new_story(title, username, text)
    # return render_template('create.html')
    return add(get_story_id()-1)

@app.route('/create', methods=["GET"])
def create():
    return render_template('create.html')

@app.route('/story/<story_id>', methods=["POST"])
def add_story(story_id):
    print("ID: "+story_id)
    username = session['username']
    text = request.form['content']
    add_to_story(story_id, username, text)
    #return render_template('frontpage.html')
    return add(story_id)
    # return render_template('add.html',title=story_name,last_addition=get_last_addition(story_name))

@app.route('/story/<story_id>', methods=["GET"])
def add(story_id):
    if can_read(session['username'],story_id):
        return render_template('display-story.html',title=story_id,story_content=get_story_content(story_id))
    return render_template('add.html',title=story_id,last_addition=get_last_addition(story_id))

@app.route('/profile', methods=['GET','POST'])
def profile():
    if request.method == 'POST':
        if 'username' in request.form:
            username = request.form['username']
            password = request.form['password']
        print(request.form)
        if 'login' in request.form:
            db_table_inits()
            correct_credentials = check_credentials(username, password)
            if correct_credentials:
                session['username'] = username
            else:
                return render_template('login.html', error = True)
        elif 'signup' in request.form:
            db_table_inits()
            no_user_exists = check_user_not_exists(username)
            if no_user_exists:
                create_new_user(username, password)
                session['username'] = username
            else:
                return render_template('signup.html', error = True)

    username = session['username']
    # for story in all_stories():
    #     print(f"{username} {story} {can_read(username,story)}")
    get_story_id()

    return render_template('profile.html', username = username,readable_stories=readable_stories(username), editable_stories=editable_stories(username))

if __name__ == '__main__':
    app.debug = True
    app.run()
