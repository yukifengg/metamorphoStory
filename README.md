# metamorphoStory by metamorphosis

## Roles
* Yuki Feng: PM
* Maya Mori: Backend + HTML of add.html, create.html, display-story.html, frontpage.html
* Eric Sohel: Back End: Databases, HTML of profile.html, login.html, signup.html
* Sasha Shifrina: Backend + HTML of add.html, create.html, display-story.html

### Notable Notes
* The usage of SQLITE to store data allows us to keep track of our users that visit our site, and cookies can help them keep their info on the site upon return
* our `db.py` program holds functions for adding, editing stories, and user log in/sign ups.
* `__init.py__` loads the Flask app and routes users to different pages in our site.
### User Information
* SQLITE database to store username and respective password
* Landing page serves choice of signing up or logging in
### Storytelling Website
* Upon log in or creation of account, the user will be able to view, edit, and add their own stories to the site
* A user can only see the last contribution made to a story and then after submitting an edit, the user can see the entirety of the story.


# Launch Codes:

Step 0: Clone our repository

   gitclone git@github.com:yukifengg/metamorphoStory.git

Step 1: Change directory into our repository

    cd metamorphostory

Step 2: Run the Flask Server

    python3 app/__init__.py

Step 3: Open the link to the local host

    http://127.0.0.1:5000

Our project was created under these conditions; if the project is not working properly, update to the following conditions.

```
click==8.1.3
Flask==2.2.2
importlib-metadata==5.0.0
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.1
Werkzeug==2.2.2
zipp==3.10.0
```
