from flask import Flask, render_template, request, session, redirect

import os

app = Flask(__name__)

app.secret_key = os.urandom(32)
username = 'bob'
password = 'mob123'

# displaying the homepage
@app.route('/', methods=['GET'])
def index():
    if 'username' in session:
        return render_template('response.html',username=session["username"])
    return render_template('login.html',has_error=False)

# if user tried to login in
@app.route('/', methods=['POST'])
def login():
    # if everything matches
    if request.form['username'] == username and request.form['password'] == password:
        # add session
        session['username'] = request.form['username']
        return render_template('response.html',username=session["username"])

    # handle cases when username/password in wrong
    error_type = ''     # error message
    if request.form['username'] != username:
        error_type='Username not found'
    elif request.form['password'] != password:
        error_type = 'Wrong password'
    return render_template('login.html',has_error=True,error=error_type)

@app.route('/logout',methods=['POST'])
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return render_template('login.html')

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        # check if the inputs are correct
        # If not, display error message
        
        # else:
        return redirect('/')        # brings user back to login page

if __name__ == "__main__": 
    app.debug = True
    app.run()