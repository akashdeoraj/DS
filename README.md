# Weather Forecast API

Please pip install the dependencies listed in the requirements.txt file

To run the weather application, change directory to weatherApp folder from terminal or cmd. Run the command - python3 manage.py runserver. Django will start running at localhost: http://127.0.0.1:8000/

Currently, there is only a single GET api. The best way to access this API would be through Postman dev tool. 

Parameters required are: latitude, logitude and day.

The API only accept geographic US latitude/longitude values as input. i.e 38.2527° N, 85.7585° W
Only the above format of latitude/longitude is accepted.

The "day" parameter accepts all the following inputs: today, tonight, monday, monday_night, tuesday, tuesday_night, thursday, thursday_night, friday, friday_night, saturday, saturday_night, sunday, sunday_night


example request: http://127.0.0.1:8000/weatherDetails/get-forecast?latitude=38.2527° N&longitude=85.7585° W&day=today