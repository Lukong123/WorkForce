"""Customer File"""

#remember to import necessary packages here

# I added these lines
class Customer(db.Model):
    """"Customer table"""
    first_name = db.Column(db.String(50))
    email = db.Column(db.String(50))

# end of added lines


class customerForm(FlaskForm):
	firstname = StringField('Input your first name')
	email = StringField('Input your email')



@app.route('/customer')
def add_customers():
     customer = customerForm()

	if customer.validate_on_submit():
		user = Customer(first_name=firstname, email=email)
        	db.session.add(user)
		db.session.commit()
		return render_template(customer.html)

    	return render_template(customer.html, customer=customer)
