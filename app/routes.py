from turtle import title
from urllib.parse import urlparse
from flask import Flask, flash, redirect, render_template, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
import os, sys
sys.path.insert(0, os.path.abspath("."))
from app import app
from .forms import LoginForm, RegistrationForm
from app.models import User
from werkzeug.urls import url_parse
from app import db



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return render_template(url_for('user_jobs'))
    return render_template('login.html', title='Sign In', form=form)
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/user_jobs')
@login_required
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

@app.route('/signup_user', methods=['GET', 'POST'])
def signup_user():
    form = RegistrationForm()
    if form.validate_on_submit():
        return render_template('user_jobs.html')
    return render_template('signup_user.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

if __name__ == '__main__':
    app.run(debug=True)

