from flask import Flask, render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

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

if __name__ == '__main__':
    app.run(debug=True)

