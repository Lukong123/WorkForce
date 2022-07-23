#!/usr/bin/env python
"""## Contact Page
- Handles message validation and submission via Flask Mail
Using Google Mail
"""

from flask import Flask, render_template, url_for, flash, redirect
from wtforms import StringField, SubmitField, TextAreaField, BooleanField
from flask_wtf import FlaskForm
import random
from flask_mail import Mail, Message
import os
from wtforms.validators import InputRequired

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'no one can guess this key im using'

messages = []


class Contact(FlaskForm):
    """Creates and validates message"""
    save = BooleanField('Save my email for later messages')
    email = StringField('Your Email Address', [InputRequired])
    subject = StringField()
    message = TextAreaField('Type in your message')
    submit = SubmitField('Submit Message')


@app.route('/contact', methods=('GET', 'POST'))
def contact():
    """Contact Page Interaction handler"""

    form = Contact()

    if form.validate_on_submit():
        """Get the data from the form and clear it"""
        
        return redirect(url_for('contact'))

    return render_template('contact.html', form=form)


if __name__ == '__main__':
    app.run()
