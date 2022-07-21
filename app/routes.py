from turtle import title
from urllib.parse import urlparse
from flask import Flask, flash, redirect, render_template, url_for, request
from app import app
from app.forms import LoginForm
from app.models import User
from werkzeug.urls import url_parse
from app import db



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')



@app.route('/logout')
def logout():
    return redirect(url_for('index'))


@app.route('/user_jobs')
def user_jobs():
    return render_template('user_jobs.html')

@app.route('/user_profile')
def user_profile():
    return render_template('user_profile.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup_emp')
def signup_emp():
    return render_template('signup_emp.html')

@app.route('/signup_user')
def signup_user():
    return render_template('signup_user.html')

if __name__ == '__main__':
    app.run(debug=True)

