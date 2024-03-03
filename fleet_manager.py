from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from supply_be.vehicle import Vehicle
import uuid


#Handles the backend and data for Fleet Managers
class FleetManager():

    fleet_manager_collection = db["fleet_manager"]


    #constructor for fleet manager class
    def __init__(self, _id, first_name, last_name, email, password, fleet_id):
        if _id == None:
            self.set_id()
        else:
            self._id = _id
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_email(email)
        self.password = password
        self.set_fleet_id(fleet_id)

    
    #selects a vehicle based on a desired service type
    def select_vehicle(self, service_type):
        return service_type
    
    #inserts dict into library
    def to_dict(self):
     return self.__dict__
    
    #retrieves dict from library
    def from_dict(dict):
        fm = FleetManager(
            first_name=dict.get("first_name"),
            last_name=dict.get("last_name"),
            email=dict.get("email"),
            password=dict.get("password"),
            fleet_id=dict.get("fleet_id"),
            _id=dict.get("_id")
        )
        return fm
    
    #stores fleet_manager object into mongoDB
    def save(self):
        self.fleet_manager_collection.insert_one(self.to_dict())

    #deletes fleet_manager object from mongoDB
    def delete(self):
        self.fleet_manager_collection.delete_one({'email':self.get_email()})

    #updates fleet_manager object in mongoDB
    def update(self):
        self.fleet_manager_collection.update_one({'_id': self.get_id()}, {'$set': self.to_dict()})
    

    #retireves fleet_manager object from mongoDB
    def get_fleet_manager(email):

        fleet_manager_collection = db["fleet_manager"]

        #Selects object in mongo via email
        from_mongo = fleet_manager_collection.find_one({'email': email})

        #creates fm object using info retrieved from mongoDB
        fleet_manager = FleetManager.from_dict(from_mongo)

        #returns fm object
        return fleet_manager
    
    #Retrieves information regarding vehicle via vehicle_id
    def get_vehicle_info(vehicle_id):
        #calls get_vehicle from vehicle class
        vehicle = Vehicle.get_vehicle(vehicle_id)

        return vehicle
    
    #FM Getters 
    def get_id(self):
        return self._id

    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def get_email(self):
        return self.email
    
    def get_password(self):
        return self.password
    
    def get_fleet_id(self):
        return self.fleet_id
    

    #FM Setters
    def set_id(self):
        self._id = uuid.uuid4().hex
    
    def set_first_name(self, first_name):
        self.first_name = first_name.capitalize()

    def set_last_name(self, last_name):
        self.last_name = last_name.capitalize()

    def set_email(self, email):
        self.email = email.lower()

    def set_password(self, password):
        # Hashes the customer password with sha256
        self.password = generate_password_hash(password, method='sha256')

    def set_fleet_id(self, fleet_id):
        self.fleet_id = fleet_id

    # Checks that that the password being passed in (e.g login) is the same as the hashed password
    def check_password(self, password):
        return check_password_hash(self.password, password)


