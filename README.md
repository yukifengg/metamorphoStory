# metamorphoStory by metamorphosis
## Yuki Feng, Pd 8, PM
## Maya Mori, Pd 8
## Sasha Shifrina, Pd 8
## Eric Sohel, Pd 8
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
### How to Clone/Install
1. Clone this repository onto your machine: `git clone [ssh]`
2. Get into running directory: `cd app`
3. Run Flask app: `python3 __init__.py`