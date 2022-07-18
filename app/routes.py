from turtle import title
from flask import Flask, render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested  ro user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('/index'))

    return render_template('login.html', title='Login', form=form)

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

