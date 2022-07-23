from turtle import title
from urllib.parse import urlparse
from flask import Flask, flash, redirect, render_template, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from app import app
from app.forms import LoginForm
from app.models import User
from werkzeug.urls import url_parse
from app import db



@app.route('/')
@app.route('/index')
def index():
    
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
@app.route('/logout')
def logout():
    logout_user()
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

