from flask import Flask, request, jsonify
from . import db
import uuid
# from supply_be import Vehicle

#stores information and contains methods regarding fleets
class Fleet(): 

    #constructor for the fleet class
    def __init__ (self, _id, vehicles, type):
        if _id == None:
            self.set_fleet_id()
        else:
            self._id = _id  
        self.set_vehicles(vehicles)
        self.set_type(type)


    #stores class info into mongoDB
    def to_dict(self):
     return self.__dict__
    
    #retrieves class info from mongoDB
    def from_dict(dict):
        f = Fleet(
            _id=dict.get("_id"),
            type=dict.get("type"),
            vehicles=dict.get("vehicles"),
        )
        return f

    #stores vehicle object into mongoDB
    def save(self):
        fleet_collection = db["fleet"]
        fleet_collection.insert_one(self.to_dict())

    #deletes vehicle object from mongoDB    
    def delete(self):
        fleet_collection = db["fleet"]
        fleet_collection.delete_one({'_id':self.get_fleet_id()})

    #updates vehicle object in mongoDB    
    def update(self):
        fleet_collection = db["fleet"]
        fleet_collection.update_one({'_id': self.get_fleet_id()}, {'$set': self.to_dict()})


    #retireves fleet object from mongoDB
    def get_fleet(fleet_id):
        #establishes reference to fm database in mongoDB
        fleet_collection = db["fleet"]
        #Selects object in mongo via object id
        from_mongo = fleet_collection.find_one({'_id': fleet_id})
        #creates fm object using info retrieved from mongoDB
        fleet = Fleet.from_dict(from_mongo)
        #returns vehicle object
        return fleet
    

    #getters and setters for fleet class
    def get_vehicles(self):
        return self.vehicles
    
    def get_type(self):
        return self.type
    
    def get_fleet_id(self):
        return self._id
    
    def set_vehicles(self, vehicles):
        self.vehicles = vehicles
    
    def set_type(self,type):
        self.type = type
    
    def set_fleet_id(self):
        self._id = uuid.uuid4().hex
    
    def get_vehicle_objects(self):
        vehicle_collection = db["vehicle"]
        fleet_vehicles = self.vehicles
        mongo_vehicles = vehicle_collection.find({'_id': {'$in': fleet_vehicles}})
        return mongo_vehicles