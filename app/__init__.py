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
def create(): 
    return render_template('create.html')

@app.route('/create')
def add():
    return render_template('create.html')
    
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
    return render_template('profile.html', username = username)
    
@app.route('/story', methods=["POST"])
def story():
    return render_template('create.html')

if __name__ == '__main__':
    app.debug = True
    app.run()