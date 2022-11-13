from flask import Flask,render_template,session,request
import secrets
from db import *


app = Flask(__name__)

# app.secret_key = secrets.token_bytes(32)
app.secret_key = b"foo"

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
    return render_template('create.html')

@app.route('/create', methods=["GET"])
def create():
    return render_template('create.html')

@app.route('/story/<story_name>', methods=["POST"])
def add_story(story_name):
    print("Title: "+story_name)
    username = session['username']
    text = request.form['content']
    add_to_story(story_name, username, text)
    #return render_template('frontpage.html')
    return render_template('add.html',title=story_name,last_addition=get_last_addition(story_name))

@app.route('/story/<story_name>', methods=["GET"])
def add(story_name):
    return render_template('add.html',title=story_name,last_addition=get_last_addition(story_name))

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

    return render_template('profile.html', username = username,readable_stories=readable_stories(username), editable_stories=editable_stories(username))

@app.route('/story', methods=["POST"])
def story():
    return render_template('create.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
