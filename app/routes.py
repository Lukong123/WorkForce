from turtle import title
from urllib.parse import urlparse
from flask import flash, redirect, render_template, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
import os, sys
sys.path.insert(0, os.path.abspath("."))
from app import app
from .forms import LoginForm, RegistrationForm, CompanyRegistrationForm, SectorForm
from app.models import Company, User, Sector
from werkzeug.urls import url_parse
from app import db


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('You are already signed in', 'warning')
        return redirect(url_for('user_jobs'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user or not user.check_password(form.password.data):
            flash('Invalid username or password', 'error')
            return redirect(url_for('login'))
        db.session.add(user)
        db.session.commit()
        login_user(user, remember=form.remember_me.data)
        if current_user.is_active:
            flash(f'You successfully logged in as {current_user.email}', 'success')
            return redirect(request.args.get("next") or url_for("user_jobs"))
        # return redirect(url_for('user_jobs'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/signup_user', methods=['GET', 'POST'])
def signup_user():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        db.create_all()
        login_user(user)
        if user.is_authenticated:
            flash('Congratulations, you just created an account', 'success')
            return redirect(url_for('user_jobs'))
            
    return render_template('signup_user.html', form=form)

@app.route('/signup_emp', methods=['GET', 'POST'])
def signup_emp():
    form = CompanyRegistrationForm()
    if form.validate_on_submit():
        comp = Company(companyname=form.companyname.data, phonenumber=form.phonenumber.data, email=form.email.data)
        comp.set_password(form.password.data)
        db.session.add(comp)
        db.session.commit()
        db.create_all()
        login_user(comp)
        if comp.is_authenticated:
            flash('Congratulations, you just created an employer account', 'success')
            return redirect(url_for('login'))
        else:
            flash('Unable to create account')
    return render_template('signup_emp.html', form=form)


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
        flash('Congratulations, you are now registered!')
        login_user(user)
        return redirect(url_for('user_jobs'))
    return render_template('register.html', title='Register', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You are now logged out')
    return redirect(url_for('index'))


@app.route('/user_jobs')
@login_required
def user_jobs():
    return render_template('user_jobs.html', title='Jobs')

@app.route('/user_profile')
@login_required
def user_profile():
    return render_template('user_profile.html', title='Your Profile')


@app.route('/signup')
def signup():
    return render_template('signup.html', title='Create Account')

@app.route('/company_dashboard')
def emp_dashboard():
    return render_template('emp_dashboard.html', title='Employers Dashboard')

@app.route('/sectors')
def sectors():
    return render_template('sectors.html', title='Sector')

@app.route('/create_sector', methods=('GET', 'POST'))
def create_sector():
    form = SectorForm()
    if form.validate_on_submit():
        sector = Sector(sectorname=form.sectorname.data, description=form.Description.data)
        db.session.add(sector)
        db.session.commit()
        db.create_all()
        return redirect(url_for('user_jobs'))
    return render_template('new_sector.html', form=form)

@app.route('/new_sector', methods=['GET', 'POST'])
def new_sector():
    form = SectorForm()
    if form.validate_on_submit():
        sector = Sector(sectorname=form.sectorname.data, description=form.description.data)
        db.session.add(sector)
        db.session.commit()
        db.create_all()
        return redirect(url_for('user_jobs'))
    return render_template('new_sector.html',  title='New Sector', form=form)

if __name__ == '__main__':
    app.run(debug=True)

