from flask import Flask, request, jsonify
from . import db
import uuid

#contains data and methods regarding vehicles used in TaaS
class Vehicle(): 

    #constructor for the vehicle class
    def __init__(self, _id, registration_number, model, make, year, status, longitude, latitude, vehicle_type, is_responding):
        if _id == None:
            self.set_vehicle_id()
        else:
            self._id = _id        
        self.set_registration_number(registration_number)
        self.set_model(model)
        self.set_make(make)
        self.set_year(year)
        self.set_status(status)
        self.set_longitude(longitude)
        self.set_latitude(latitude)
        self.set_vehicle_type(vehicle_type)
        self.set_is_responding(is_responding)

     #stores class info into mongoDB
    def to_dict(self):
     return self.__dict__
    
    #retrieves class info from mongoDB
    def from_dict(dict):
        v = Vehicle(
            _id=dict.get("_id"),
            registration_number=dict.get("registration_number"),
            model=dict.get("model"),
            make=dict.get("make"),
            year=dict.get("year"),
            status=dict.get("status"),
            longitude=dict.get("longitude"),
            latitude=dict.get("latitude"),
            vehicle_type=dict.get("vehicle_type"),
            is_responding=dict.get("is_responding")
        )
        return v

    #stores fleet_manager object into mongoDB
    def save(self):
        vehicle_collection = db["vehicle"]
        vehicle_collection.insert_one(self.to_dict())

    def delete(self):
        vehicle_collection = db["vehicle"]

        vehicle_collection.delete_one({'_id':self.get_vehicle_id()})

    #retireves fleet object from mongoDB
    def get_vehicle(_id):

        #establishes reference to fm database in mongoDB
        vehicle_collection = db["vehicle"]
        
        #Selects object in mongo via object id
        from_mongo = vehicle_collection.find_one({'_id': _id})

        #creates fm object using info retrieved from mongoDB
        vehicle = Vehicle.from_dict(from_mongo)

        #returns vehicle object
        return vehicle
    

    #getters and setters for vehicle class
    def get_vehicle_id(self):
        return self._id
    
    def get_registration_number(self):
        return self.registration_number
    
    def get_model(self):
        return self.model
    
    def get_make(self):
        return self.make
    
    def get_year(self):
        return self.year
    
    def get_status(self):
        return self.status
    
    def get_longitude(self):
        return self.longitude
    
    def get_latitude(self):
        return self.latitude
    
    def get_vehicle_type(self):
        return self.vehicle_type
    
    def get_is_responding(self):
        return self.is_responding
    
    def set_vehicle_id(self):
        self._id = uuid.uuid4().hex

    def set_registration_number(self, registration_number):
        self.registration_number = registration_number

    def set_model(self, model):
        self.model = model

    def set_make(self, make):
        self.make = make

    def set_year(self, year):
        self.year = year

    def set_status(self, status):
        self.status = status

    def set_longitude(self, longitude):
        self.longitude = longitude
    
    def set_latitude(self, latitude):
        self.latitude = latitude

    def set_vehicle_type(self, vehicle_type):
        self.vehicle_type = vehicle_type

    def set_is_responding(self, is_responding):
        self.is_responding = is_responding


    