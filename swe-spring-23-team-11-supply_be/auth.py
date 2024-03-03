from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from .fleet_manager import FleetManager
from . import db

fleet_manager_collection = db["fleet_manager"]

# Create an instance of Blueprint and name it auth
auth = Blueprint('auth', __name__)

# Define a route for login with both GET and POST methods
@auth.route('/login', methods=['GET', 'POST'])
def login():
   # If the request method is POST
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = fleet_manager_collection.find_one({'email': email})
        if user:
            # Return the FleetManager object if the user is found
            fleet_manager = FleetManager.from_dict(user)
            print(fleet_manager.to_dict())
            if fleet_manager.check_password(password):
                #  Flash a success message and log the user in
                flash('Logged in successfully!', category='success')
                session['user_email'] = str(fleet_manager.email)
                return redirect(url_for('views.home'))
            else:
                flash('Invalid email or password.', 'error')
        else:
            flash('Invalid email or password.', 'error')

    # Render the login template with the current user's info
    return render_template("login.html")



# Define a route for logout
@auth.route('/logout')
# @login_required
def logout():
    session.pop('user_email', None)
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    # If the request method is POST
    if request.method == 'POST':
        # Get email, first name, last name, and password from the submitted form
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        existing_fleet_manager = fleet_manager_collection.find_one({'email': email})

        # If customer with the same email already exists
        if existing_fleet_manager:
            flash('Email already exists.', category='error')
        # If email is too short
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        # If first name is too short
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        # If last name is too short
        elif len(last_name) < 2:
            flash('Last name must be greater than 1 character.', category='error')
        # If passwords don't match
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        # If password is too short
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        #If Everythin is valid
        else:
            # Get the customer with the given email
            fleet_manager = FleetManager(_id=None,first_name=first_name, last_name=last_name, email=email, password=password1, fleet_id=[])
            fleet_manager.set_password(password1)
            print(fleet_manager.to_dict())
            # Insert the new user into the fleet_managers collection in MongoDB
            fleet_manager.save()
            session['user_email'] = str(fleet_manager.email)
            return redirect(url_for('views.home'))


    return render_template("sign_up.html")