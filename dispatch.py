from flask import Flask, request, jsonify, Blueprint
import requests
import json

class Dispatch():
    
    #Receives the json of an Order object
   # and determines if it can be fulfilled
    def request_vehicle(order_obj_json):
        trip_fulfillable = True

        order_dict = order_obj_json
        # Once Fleets are populated in DB, we can 
        # check to see if this order can be fulfilled.
        # For now, just ensure that the order is in Austin.
        if 'austin' not in order_dict['pickup_location'].lower():
            trip_fulfillable = False
        if 'austin' not in order_dict['dropoff_location'].lower():
            trip_fulfillable = False
        return trip_fulfillable

