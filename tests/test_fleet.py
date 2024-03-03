import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
import unittest
from supply_be.fleet import Fleet

class TestFleet(unittest.TestCase):

    #setting up initial values for tests
    @classmethod
    def setUpClass(cls):
        
        #Fleet 1
        cls.expected_id = None
        cls.expected_vehicles = ["89f3b131d4994f8b8f394c65c2d934c9", "e03c1e605e0b45299d9470de8b7bda38", "7c0e17d88f7c483fba1402b0c3a2222a"]
        cls.expected_type = "Blood Transport"

        #creating an instance of fleet class with the expected values
        cls.actual_fleet = Fleet(
            _id=cls.expected_id,
            vehicles=cls.expected_vehicles,
            type=cls.expected_type
        )

        #Fleet 2
        cls.expected_id_2 = None
        cls.expected_vehicles_2 = ["89f3b131d4994f7b8f394c65c2d934c9", "e03c1e605e0b45297d9470de8b7bda38", "7c7e17d88f7c483fba1402b0c3a2222a"]
        cls.expected_type_2 = "Syringe Transport"

        #creating an instance of fleet class with the expected values
        cls.actual_fleet_2 = Fleet(
            _id=cls.expected_id_2,
            vehicles=cls.expected_vehicles_2,
            type=cls.expected_type_2
        )

    #Testing the creation of fleet instance
    def test_fleet_creation(self):
        self.assertEqual(self.actual_fleet.get_vehicles(), self.actual_fleet.vehicles)
        self.assertEqual(self.actual_fleet_2.get_vehicles(), self.actual_fleet_2.vehicles)


    #Testing the to_dict method of the Fleet class
    def test_to_dict(self):
        expected_dict = {
            "_id" : self.actual_fleet.get_fleet_id(),
            "vehicles" : self.expected_vehicles,
            "type" : self.expected_type
        }
        actual_dict = self.actual_fleet.to_dict()
        self.assertEqual(actual_dict, expected_dict)

    #Testing the from_dict method of the Fleet class
    def test_from_dict(self):
        expected_fleet = self.actual_fleet
        dict_fleet = expected_fleet.to_dict()
        actual_fleet = Fleet.from_dict(dict_fleet)
        self.assertEqual(actual_fleet.__dict__, expected_fleet.__dict__)

    #Testing the save and get_fleet methods of the Fleet class
    def test_and_save_get_fleet(self):
        expected_fleet = self.actual_fleet
        expected_fleet.save()
        id = expected_fleet.get_fleet_id()
        actual_fleet = Fleet.get_fleet(id)
        self.assertEqual(actual_fleet.__dict__, expected_fleet.__dict__)
        expected_fleet.delete()

   #Testing the getters and setters of the Fleet class
    def test_getters_and_setters(self):
        actual_fleet = Fleet(_id=None, vehicles = ["placeholder"], type="placeholder")   

        actual_fleet.set_vehicles(["89f3b131d4994f8b8f394c65c2d934c9", "e03c1e605e0b45299d9470de8b7bda38", "7c0e17d88f7c483fba1402b0c3a2222a"])
        actual_fleet.set_type("Blood Transport")

        self.assertEqual(actual_fleet.get_fleet_id(), actual_fleet._id)
        self.assertListEqual(actual_fleet.get_vehicles(), actual_fleet.vehicles)
        self.assertEqual(actual_fleet.get_type(), actual_fleet.type)

if __name__ == '__main__':
    unittest.main()