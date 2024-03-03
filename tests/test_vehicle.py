import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
import unittest

from supply_be.vehicle import Vehicle

#This class contains mehtods to test the methods inside the vehicle class
class TestVehicle(unittest.TestCase):
    
    #setting up initial values for the tests
    @classmethod
    def setUpClass(cls):

        #Vehicle 1
        cls.expected_vehicle_id = None
        cls.expected_registration_number = "1233432"
        cls.expected_model = "carolla"
        cls.expected_make = "toyota"
        cls.expected_year = "2007"
        cls.expected_status = "en_route"
        cls.expected_latitude = "30.23221116694423"
        cls.expected_longitude = "-97.75837626905304"
        cls.expected_vehicle_type = "car"
        cls.expected_is_responding = True

        #creating an instance of vehicle class with the expected values
        cls.actual_vehicle = Vehicle(
            _id=cls.expected_vehicle_id,
            registration_number=cls.expected_registration_number,
            model=cls.expected_model,
            make=cls.expected_make,
            year=cls.expected_year,
            status=cls.expected_status,
            latitude=cls.expected_latitude,
            longitude=cls.expected_longitude,
            vehicle_type=cls.expected_vehicle_type,
            is_responding = cls.expected_is_responding
        )

        #Vehicle 2
        cls.expected_vehicle_id_2 = None
        cls.expected_registration_number_2 = "1234567"
        cls.expected_model_2 = "pilot"
        cls.expected_make_2 = "honda"
        cls.expected_year_2 = "2005"
        cls.expected_status_2 = "in_maitenence"
        cls.expected_latitude_2 = "30.23221116694423"
        cls.expected_longitude_2 = "-97.75837626905304"
        cls.expected_vehicle_type_2 = "car"
        cls.expected_is_responding_2 = False

    #creating an instance of vehicle class with the expected values
        cls.actual_vehicle_2 = Vehicle(
            _id=cls.expected_vehicle_id_2,
            registration_number=cls.expected_registration_number_2,
            model=cls.expected_model_2,
            make=cls.expected_make_2,
            year=cls.expected_year_2,
            status=cls.expected_status_2,
            latitude=cls.expected_latitude_2,
            longitude=cls.expected_longitude_2,
            vehicle_type=cls.expected_vehicle_type_2,
            is_responding = cls.expected_is_responding_2

        )

    #Testing the creation of Vehicle instance
    def test_vehicle_creation(self):

        #Vehicle 1
        self.assertEqual(self.actual_vehicle.get_vehicle_id(), self.actual_vehicle._id)
        self.assertEqual(self.actual_vehicle.get_registration_number(), self.expected_registration_number)
        self.assertEqual(self.actual_vehicle.get_model(), self.expected_model)
        self.assertEqual(self.actual_vehicle.get_make(), self.expected_make)
        self.assertEqual(self.actual_vehicle.get_year(), self.expected_year)
        self.assertEqual(self.actual_vehicle.get_status(), self.expected_status)
        self.assertEqual(self.actual_vehicle.get_latitude(), self.expected_latitude)
        self.assertEqual(self.actual_vehicle.get_longitude(), self.expected_longitude)
        self.assertEqual(self.actual_vehicle.get_vehicle_type(), self.expected_vehicle_type)
        self.assertEqual(self.actual_vehicle.get_is_responding(), self.expected_is_responding)

        #Vehicle 2
        self.assertEqual(self.actual_vehicle_2.get_vehicle_id(), self.actual_vehicle_2._id)
        self.assertEqual(self.actual_vehicle_2.get_registration_number(), self.expected_registration_number_2)
        self.assertEqual(self.actual_vehicle_2.get_model(), self.expected_model_2)
        self.assertEqual(self.actual_vehicle_2.get_make(), self.expected_make_2)
        self.assertEqual(self.actual_vehicle_2.get_year(), self.expected_year_2)
        self.assertEqual(self.actual_vehicle_2.get_status(), self.expected_status_2)
        self.assertEqual(self.actual_vehicle.get_latitude(), self.expected_latitude_2)
        self.assertEqual(self.actual_vehicle.get_longitude(), self.expected_longitude_2)
        self.assertEqual(self.actual_vehicle_2.get_vehicle_type(), self.expected_vehicle_type_2)
        self.assertEqual(self.actual_vehicle_2.get_is_responding(), self.expected_is_responding_2)

    #Testing the to_dict method of the Vehicle class
    def test_to_dict(self):
        expected_dict = {
            "_id" : self.actual_vehicle.get_vehicle_id(),
            "registration_number" : self.expected_registration_number,
            "model" : self.expected_model,
            "make" : self.expected_make,
            "year" : self.expected_year,
            "status" : self.expected_status,
            "latitude" : self.expected_latitude,
            "longitude" : self.expected_longitude,
            "vehicle_type" : self.expected_vehicle_type,
            "is_responding" : self.expected_is_responding

        }
        actual_dict = self.actual_vehicle.to_dict()
        self.assertEqual(actual_dict, expected_dict)

    #Testing the from_dict method of the Vehicle class
    def test_from_dict(self):
        expected_vehicle = self.actual_vehicle
        dict_vehicle = expected_vehicle.to_dict()
        actual_vehicle = Vehicle.from_dict(dict_vehicle)
        self.assertEqual(actual_vehicle.__dict__, expected_vehicle.__dict__)

    #Testing the save and get_vehicle methods of the Vehicle class
    def test_save_and_get_vehicle(self):
        expected_vehicle = self.actual_vehicle
        expected_vehicle.save()
        id = expected_vehicle.get_vehicle_id()
        actual_vehicle = Vehicle.get_vehicle(id)
        self.assertEqual(actual_vehicle.__dict__, expected_vehicle.__dict__)
        expected_vehicle.delete()

    #Testing the getters and setters of the Vehicle Class
    def test_getters_and_setters(self):
        actual_vehicle = Vehicle(_id=None, registration_number="place_holder", model="place_holder", make="place_holder", year="place_holder", vehicle_type="place_holder", latitude="place_holder", longitude="place_holder", status="place_holder", is_responding=True)

        actual_vehicle.set_registration_number("1234567")
        actual_vehicle.set_model("carolla")
        actual_vehicle.set_make("toyota")
        actual_vehicle.set_year("2007")
        actual_vehicle.set_status("en_route")
        actual_vehicle.set_latitude("30.23221116694423")
        actual_vehicle.set_longitude("-97.75837626905304")
        actual_vehicle.set_vehicle_type("car")
        actual_vehicle.set_is_responding(True)

        self.assertEqual(actual_vehicle.get_vehicle_id(), actual_vehicle._id)
        self.assertEqual(actual_vehicle.get_registration_number(), "1234567")
        self.assertEqual(actual_vehicle.get_model(), "carolla")
        self.assertEqual(actual_vehicle.get_make(), "toyota")
        self.assertEqual(actual_vehicle.get_year(), "2007")
        self.assertEqual(actual_vehicle.get_status(), "en_route")
        self.assertEqual(actual_vehicle.get_latitude(), "30.23221116694423")
        self.assertEqual(actual_vehicle.get_longitude(), "-97.75837626905304")
        self.assertEqual(actual_vehicle.get_vehicle_type(), "car")
        self.assertEqual(actual_vehicle.get_is_responding(), True)

if __name__ == '__main__':
    unittest.main()
