from flask import Flask, redirect, url_for
application = Flask(__name__)

@application.route('/')
def hello_admin():
    return 'Hello Admin'

@application.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest

@application.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest = name))

