# Supply Back-End

### Description:

- This repository includes includes the methods for handling vehicles, fleets, and fleet managers storing their information. Additionally it also handles Fleet Manager Authentication.

---

### WeGo Supply Backend Structure:


```
.
└── wego_supply_repos
    ├── supply_be
    │   ├── __init__.py
    │   ├── auth.py
    |   ├── views.py
    │   ├── dispatch.py
    │   ├── fleet_manager.py
    │   ├── fleet.py
    │   ├── vehicle.py
    │   └── tests
    │       ├── test_dispatch.py
    │       ├── test_fleet_manager.py
    │       ├── test_fleet.py
    │       └── test_vehicle.py
    ├── supply_fe
    │   ├── dashboard.html
    │   ├── fleetDV.html
    │   ├── base.html
    │   ├── fleetsanalytics.html
    │   └── fmMap.html
    ├── common_services_fe
    │   ├── login.html
    │   ├── sign_up.html
    │   └── static
    │       └── map_animation.js
    ├── map_service_handler
    │   ├── mapbox.py
    │   └── tests
    │       └── test_mapbox.py
    ├── vehicle_simulator
    │   ├── map_handler.py
    │   ├── geocode_traversal.py
    │   └── tests
    │       └── test_geocode_traversal.py
    ├── supply_order_handler_api
    │   ├──order_rest_api.py
    │   └── tests
    │       └── test_order_rest_api.py
    ├── requirements.txt 
    ├── config.py
    └── main.py
```

---

### Installation

* Create a directory in your machine where all the supply cloud repositories along with main.py, requirements.txt, and config.py will all live (as shown in the project structure above).
* Preferably call it `wego_supply_repos`
* Proceed to clone this repository in that directory:
    * `git clone https://your_user_name@bitbucket.org/swe-spring-23-team-11/supply_be.git`
* Libraries used:
    * flask -> `pip install flask`
    * pymysql -> `pip install pymongo`
    * cryptography -> `pip install cryptography`
    * requests -> `pip install requests`

---

### Testing

- Running test cases in supply_be:
  - Make sure that your current directory is set to supply_be in the command prompt.
  - Proceed to run the following command:
    `python -m unittest discover -s tests -v`
  - The result should be as follow:

```
test_request_vehicle_for_invalid_dropoff_location_order (test_dispatch.TestDispatch) ... ok
test_request_vehicle_for_invalid_pickup_location_order (test_dispatch.TestDispatch) ... ok
test_request_vehicle_for_valid_order (test_dispatch.TestDispatch) ... ok
test_and_save_get_fleet (test_fleet.TestFleet) ... ok
test_fleet_creation (test_fleet.TestFleet) ... ok
test_from_dict (test_fleet.TestFleet) ... ok
test_getters_and_setters (test_fleet.TestFleet) ... ok
test_to_dict (test_fleet.TestFleet) ... ok
test_fleet_manager_creation (test_fleet_manager.TestFleetManager) ... ok
test_from_dict (test_fleet_manager.TestFleetManager) ... ok
test_getters_and_setters (test_fleet_manager.TestFleetManager) ... ok
test_save_and_get_fleet_manager (test_fleet_manager.TestFleetManager) ... ok
test_to_dict (test_fleet_manager.TestFleetManager) ... ok
test_from_dict (test_vehicle.TestVehicle) ... ok
test_getters_and_setters (test_vehicle.TestVehicle) ... ok
test_save_and_get_vehicle (test_vehicle.TestVehicle) ... ok
test_to_dict (test_vehicle.TestVehicle) ... ok
test_vehicle_creation (test_vehicle.TestVehicle) ... ok
Ran 18 tests in 0.009s
OK
```

- To run unit tests with coverage:

```
python -m coverage run  --source='/Users/emiliocardenas/sweCourse/wego_supply_repos/supply_be' --omit="*/test_*.py" -m unittest discover -s tests/ -v
```

- A `.coverage` file should be generated, to be able to see the contents of it, run the following command:

```
python -m coverage report
```

- It should display the following table:

```
Name               Stmts    Miss   Cover
dispatch.py         12       0      100%
fleet_manager.py    62       4      94%
fleet.py            46       6      87%
vehicle.py          73       0      100%
TOTAL               193      10     94%
```

---

### Manual Deployment (not using CI/CD)

- If you do not have a supply cloud user, please contact DevOps for deployment
- The following steps take place in the supply cloud
- First navigate to the repos folder with the following command:`$ cd /home/team11/repos`

  - Now navigate to the supply_be directory

    - `$ cd supply_be`

  - To get the changes into production environment run the following commands:

    - `$ git checkout main`

    - `$ git fetch`

    - `$ git pull`

    - You should now be able to see the version of the main branch that from bitbucket reflected in the production environment.

---

### Who do I talk to?

- WeGo Team 11 2023:

- Team Members:

```
  1.  Deautaun Ross
  2.  Emilio Cardenas - Request Handling Developer
  3.  Trent Tucker
  4.  Brandon Capdevielle - Class and Tests Developer
  5.  Alexandra Burke
  6.  Johan Olvera
  7.  Nicolas Campbell
  8.  Isael Ramirez
  9.  Chris Townsend
```
