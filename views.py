from flask import Blueprint, render_template, session, redirect, url_for, flash, jsonify, request
from . import db
from .fleet_manager import FleetManager
from .fleet import Fleet
from .vehicle import Vehicle
import json
from config import Config
fleet_manager_collection = db["fleet_manager"]
fleet_collection = db["fleet"]
vehicle_collection = db["vehicle"]

# Define a Blueprint named 'views'
views = Blueprint('views', __name__)

# Renders the dashboard.html template passing a fleet list. If a user is not logged in, it redirects to the login page.
@views.route('/')
def home():
    if 'user_email' not in session:
        return redirect(url_for('auth.login'))
    user_email = session['user_email']
    user = fleet_manager_collection.find_one({'email': user_email})
    if not user:
        # If the user is not found in the database, clear the session and redirect to the login page
        session.clear()
        return redirect(url_for('auth.login'))

    # Return the home template with the current user's info
    fleet_manager = FleetManager.from_dict(user)
    manager_fleets = fleet_manager.get_fleet_id()
    fleets = fleet_collection.find({'_id': {'$in': manager_fleets}})
    class_fleets = []
    for dict_fleet in fleets:
        class_fleets.append(Fleet.from_dict(dict_fleet))
    return render_template("dashboard.html", fleets=class_fleets)

#Renders the fmMap.html template, which shows a map view of the fleet. If a user is not logged in, it redirects to the login page.
@views.route('/fleet-map')
def fleet_map():
    if 'user_email' not in session:
        return redirect(url_for('auth.login'))
    user_email = session['user_email']
    user = fleet_manager_collection.find_one({'email': user_email})
    if not user:
        # If the user is not found in the database, clear the session and redirect to the login page
        session.clear()
        return redirect(url_for('auth.login'))
    # Return the home template with the current user's info
    fleet_manager = FleetManager.from_dict(user)
    return render_template("fmMap.html") 


#Renders the fleetanalytics.html template, which shows some analytics of the fleet. If a user is not logged in, it redirects to the login page.
@views.route('/fleet-analytics')
def fleet_analytics():
    if 'user_email' not in session:
        return redirect(url_for('auth.login'))
    user_email = session['user_email']
    user = fleet_manager_collection.find_one({'email': user_email})
    if not user:
        # If the user is not found in the database, clear the session and redirect to the login page
        session.clear()
        return redirect(url_for('auth.login'))
    # Return the home template with the current user's info
    fleet_manager = FleetManager.from_dict(user)
    return render_template("fleetanalytics.html") 

#Renders the fleetDV.html template, which shows a chart view of the fleet. If a user is not logged in, it redirects to the login page.
@views.route('/fleet-chart')
def fleet_chart():
    if 'user_email' not in session:
        return redirect(url_for('auth.login'))
    user_email = session['user_email']
    user = fleet_manager_collection.find_one({'email': user_email})
    if not user:
        # If the user is not found in the database, clear the session and redirect to the login page
        session.clear()
        return redirect(url_for('auth.login'))
    # Return the home template with the current user's info
    fleet_manager = FleetManager.from_dict(user)
    return render_template("fleetDV.html") 


#A POST request that creates a new fleet with the given fleet type in the database and returns a JSON response. It expects a JSON data from the client-side with the fleet_type parameter.
@views.route('/create-fleet', methods=['POST'])
def create_fleet():
    data = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    fleet_type = data['fleet_type']
    user_email = session['user_email']
    user = fleet_manager_collection.find_one({'email': user_email})
    fleet_manager = FleetManager.from_dict(user)
    new_fleet = Fleet(_id=None, type=fleet_type, vehicles=[]) 
    new_fleet.save()
    manager_fleets = fleet_manager.fleet_id
    manager_fleets.append(new_fleet._id)
    fleet_manager.update()
    flash('Created a new Fleet', category='success')
    return jsonify({})


#: A POST request that adds a new vehicle to a fleet in the database and returns a JSON response. It expects a JSON data from the client-side with the fleet_id, make, year, and status parameters.
@views.route('/add-vehicle', methods=['POST'])
def add_vehicle():
    data = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    print(data)
    fleet_id = data['fleet_id']
    make = data['make']
    year = data["year"]
    status = data["status"]
    print(fleet_id)
    user_email = session['user_email']
    user = fleet_manager_collection.find_one({'email': user_email})
    fleet_manager = FleetManager.from_dict(user)
    manager_fleets = fleet_manager.get_fleet_id()
    for fleet_dict_id in manager_fleets:
        if fleet_dict_id == fleet_id:
            fleet_class = Fleet.get_fleet(fleet_id)
            new_vehicle = Vehicle(_id=None, registration_number="", model="", make=make, year=year, vehicle_type=fleet_class.get_type(), longitude="-97.758", latitude="30.232", status=status, is_responding=True)
            fleet_vehicles = fleet_class.vehicles
            fleet_vehicles.append(new_vehicle.get_vehicle_id())
            fleet_class.update()
            new_vehicle.save()
    return jsonify({})

#A POST request that deletes a vehicle from a fleet in the database and returns a JSON response. It expects a JSON data from the client-side with the vehicle_id parameter.
@views.route('/delete-vehicle', methods=['POST'])
def delete_vehicle():  
    data = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    vehicle_id = data['vehicle_id']
    user_email = session['user_email']
    user = fleet_manager_collection.find_one({'email': user_email})
    fleet_manager = FleetManager.from_dict(user)
    manager_fleets = fleet_manager.get_fleet_id()
    fleets = fleet_collection.find({'_id': {'$in': manager_fleets}})
    for fleet in fleets:
        fleet_class = Fleet.from_dict(fleet)
        if vehicle_id in fleet_class.get_vehicles():
            vehicle_class = Vehicle.get_vehicle(vehicle_id)
            vehicle_class.delete()

            fleet_class.get_vehicles().remove(vehicle_id)
            # print(fleet_class.get_vehicles())
            fleet_class.update()
    return jsonify({})


#A POST request that deletes a fleet with the given fleet id in the database and returns a JSON response. It expects a JSON data from the client-side with the fleet_id parameter.
@views.route('/delete-fleet', methods=['POST'])
def delete_fleet():  
    data = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    fleet_id = data['fleet_id']
    user_email = session['user_email']
    user = fleet_manager_collection.find_one({'email': user_email})
    fleet_manager = FleetManager.from_dict(user)
    manager_fleets = fleet_manager.get_fleet_id()
    if fleet_id in manager_fleets:
        fleet_class=Fleet.get_fleet(fleet_id)
        if len(fleet_class.get_vehicles()) != 0:
            for vehicle_id in fleet_class.get_vehicles():
                vehicle_class = Vehicle.get_vehicle(vehicle_id)
                vehicle_class.delete()
        fleet_manager.fleet_id.remove(fleet_id)
        fleet_class.delete()
        fleet_manager.update()
        flash('Deleted a fleet', category='error')
    return jsonify({})


# Handles a get request to serve the our mapbox api toke to the client-side
@views.route('/mapbox-token')
def mapbox_token():
    return jsonify({'access_token': Config.access_token})