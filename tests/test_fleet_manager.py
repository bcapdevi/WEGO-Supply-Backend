import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
import unittest
from supply_be.fleet_manager import FleetManager
from supply_be.vehicle import Vehicle

class TestFleetManager(unittest.TestCase):

    # Setting up initial values for the tests
    @classmethod
    def setUpClass(cls):

        #Fleet Manager 1
        cls.expected_first_name = "John"
        cls.expected_last_name = "Doe"
        cls.expected_email = "johndoe@example.com"
        cls.expected_password = "mypassword"
        cls.expected_fleet_id = None

        # Creating an instance of the FleetManager class with the expected values 
        cls.actual_fm = FleetManager(
            _id=None,
            first_name=cls.expected_first_name,
            last_name=cls.expected_last_name,
            email=cls.expected_email,
            password=cls.expected_password,
            fleet_id=cls.expected_fleet_id
        )
        cls.actual_fm.set_password(cls.expected_password)

        #Fleet Manager 2
        cls.expected_first_name_2 = "John"
        cls.expected_last_name_2 = "Doe"
        cls.expected_email_2 = "johndoe@example.com"
        cls.expected_password_2 = "mypassword"
        cls.expected_fleet_id_2 = None

        # Creating an instance of the FleetManager class with the expected values 
        cls.actual_fm_2 = FleetManager(
            _id=None,
            first_name=cls.expected_first_name_2,
            last_name=cls.expected_last_name_2,
            email=cls.expected_email_2,
            password=cls.expected_password_2,
            fleet_id=cls.expected_fleet_id_2
        )
        cls.actual_fm_2.set_password(cls.expected_password_2)

    # Testing the creation of the FleetManager instance
    def test_fleet_manager_creation(self):
        #Fleet Manager 1
        self.assertEqual(self.actual_fm.get_id(), self.actual_fm._id)
        self.assertEqual(self.actual_fm.get_first_name(), self.expected_first_name)
        self.assertEqual(self.actual_fm.get_last_name(), self.expected_last_name)
        self.assertEqual(self.actual_fm.get_email(), self.expected_email)
        self.assertTrue(self.actual_fm.check_password(self.expected_password))
        self.assertEqual(self.actual_fm.get_fleet_id(), self.expected_fleet_id)

        #Fleet Manager 2
        self.assertEqual(self.actual_fm_2.get_id(), self.actual_fm_2._id)
        self.assertEqual(self.actual_fm_2.get_first_name(), self.expected_first_name_2)
        self.assertEqual(self.actual_fm_2.get_last_name(), self.expected_last_name_2)
        self.assertEqual(self.actual_fm_2.get_email(), self.expected_email_2)
        self.assertTrue(self.actual_fm_2.check_password(self.expected_password_2))
        self.assertEqual(self.actual_fm_2.get_fleet_id(), self.expected_fleet_id_2)

    # Testing the to_dict method of the FleetManager class  
    def test_to_dict(self):
        expected_dict = {
            "_id": self.actual_fm.get_id(),
            "first_name": self.expected_first_name,
            "last_name": self.expected_last_name,
            "email": self.expected_email,
            "password": self.actual_fm.get_password(),
            "fleet_id": self.expected_fleet_id
        }
        actual_dict = self.actual_fm.to_dict()
        self.assertEqual(actual_dict, expected_dict)

    # Testing the from_dict method of the FleetManager class
    def test_from_dict(self):
        expected_fm = self.actual_fm
        dict_fm = expected_fm.to_dict()
        actual_fm = FleetManager.from_dict(dict_fm)
        self.assertEqual(actual_fm.__dict__, expected_fm.__dict__)

    # Testing the save and get_fleet_manager methods of the FleetManager class
    def test_save_and_get_fleet_manager(self):
        expected_fm = self.actual_fm
        expected_fm.save()
        email = expected_fm.get_email()
        actual_fm = FleetManager.get_fleet_manager(email)
        self.assertEqual(actual_fm.__dict__, expected_fm.__dict__)
        expected_fm.delete()

    # Testing the getters and setters of the FleetManager class
    def test_getters_and_setters(self):
        actual_fm = FleetManager(_id=None, first_name="placeholder", last_name="placeholder", email="placeholder", password="placeholder", fleet_id=None)

        actual_fm.set_first_name("Jane")
        actual_fm.set_last_name("Doe")
        actual_fm.set_email("janedoe@example.com")
        actual_fm.set_password("newpassword")
        actual_fm.set_fleet_id("newfleet")
        self.assertEqual(actual_fm.get_id(), actual_fm._id)
        self.assertEqual(actual_fm.get_first_name(), "Jane")
        self.assertEqual(actual_fm.get_last_name(), "Doe")
        self.assertEqual(actual_fm.get_email(), "janedoe@example.com")
        self.assertNotEqual(actual_fm.get_password(), "newpassword")
        self.assertTrue(actual_fm.check_password("newpassword"))
        self.assertEqual(actual_fm.get_fleet_id(), "newfleet")


if __name__ == '__main__':
    unittest.main()

