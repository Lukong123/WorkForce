from flask import flash, redirect, render_template, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
import os, sys
sys.path.insert(0, os.path.abspath("."))
from app import app
from .forms import LoginForm, RegistrationForm, CompanyRegistrationForm, SectorForm, LoginCompany
from app.models import User, Sector
from app import db


@app.route('/')
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
    return render_template('login.html', title='Sign In', form=form)


@app.route('/employers/login', methods=['GET', 'POST'])
def login_emp():
    if current_user.is_authenticated:
        flash('You are already signed in', 'warning')
        return redirect(url_for('emp_dashboard'))
    form = LoginCompany()
    if form.is_submitted():
        comp = User.query.filter_by(email=form.email.data).first()
        if not comp or not comp.check_password(form.password.data):
            flash('Invalid email or password', 'error')
            return redirect(url_for('login_emp'))
        login_user(comp, remember=form.remember_me.data)
        if current_user.is_active:
            flash(f'You successfully logged in as {current_user.name}', 'success')
            return redirect(request.args.get("next") or url_for("emp_dashboard"))
    return render_template('login_emp.html', title='Log In', form=form, User=User)


@app.route('/signup_user', methods=['GET', 'POST'])
def signup_user():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(name=form.username.data, email=form.email.data, role='Candidate')
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        if user.is_authenticated:
            flash('Congratulations, you just created an account', 'success')
            return redirect(url_for('user_jobs'))
    return render_template('signup_user.html', form=form)


@app.route('/employers/new', methods=['GET', 'POST'])
def signup_emp():
    form = CompanyRegistrationForm()
    if form.is_submitted():
        comp = User(name=form.name.data, tel=form.tel.data, email=form.email.data)
        comp.role = 'Employer'
        comp.set_password(form.password.data)
        db.session.add(comp)
        db.session.commit()
        login_user(comp)
        if comp.is_active:
            flash('Congratulations, you just created an employer account', 'success')
            return redirect(url_for('emp_dashboard'))
        else:
            flash('Unable to create account')
    return render_template('signup_emp.html', form=form, title='New Employer Account')


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

@app.route('/company/dashboard')
def emp_dashboard():
    return render_template('emp_dashboard.html', title='Employers Dashboard')

@app.route('/sectors')
def sectors():
    return render_template('sectors.html', title='Sector')

@app.route('/new_sector', methods=['GET', 'POST'])
def new_sector():
    form = SectorForm()
    if form.validate_on_submit():
        sector = Sector(sectorname=form.sectorname.data, description=form.description.data)
        db.session.add(sector)
        db.session.commit()
        db.create_all()
        return redirect(url_for('sectors'))
    return render_template('new_sector.html',  title='New Sector', form=form)

if __name__ == '__main__':
    app.run(debug=True)

