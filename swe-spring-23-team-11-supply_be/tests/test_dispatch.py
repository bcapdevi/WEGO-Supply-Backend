import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
import unittest

from supply_be.dispatch import Dispatch

# This class contains functions for testing the dispatch class
class TestDispatch(unittest.TestCase):

    #Tests if a valid order can be fulfilled
    def test_request_vehicle_for_valid_order(self):
        good_order_json = {"id":"01892763","pickup_location":"3001 South Congress Ave, Austin, Texas 76033", "dropoff_location":"521 Congress Ave, Austin, Texas 76033","duration":"12","date":"12:12:2023 11:30","status":"requested","cost":"15.76","service_type":"Patient Transportation","vehicle_id":"","customer_id":"1"}
        self.assertEqual(True, Dispatch.request_vehicle(good_order_json))

    #Tests if a pickup not in Austin is declined
    def test_request_vehicle_for_invalid_pickup_location_order(self):
        bad_pickup_location_order_json = {"id":"01892763","pickup_location":"300 Reunion Blvd, Dallas, Texas, 75207", "dropoff_location":"521 Congress Ave, Austin, Texas 76033","duration":"12","date":"12:12:2023 11:30","status":"requested","cost":"15.76","service_type":"Patient Transportation","vehicle_id":"","customer_id":"1"}
        self.assertEqual(False, Dispatch.request_vehicle(bad_pickup_location_order_json))

    #Tests if a dropoff not in Austin is declined
    def test_request_vehicle_for_invalid_dropoff_location_order(self):
        bad_dropoff_location_order_json = {"id":"01892763","pickup_location":"3001 South Congress Ave, Austin, Texas 76033", "dropoff_location":"300 Reunion Blvd, Dallas, Texas, 75207","duration":"12","date":"12:12:2023 11:30","status":"requested","cost":"15.76","service_type":"Patient Transportation","vehicle_id":"","customer_id":"1"}
        self.assertEqual(False, Dispatch.request_vehicle(bad_dropoff_location_order_json))
