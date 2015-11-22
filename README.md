# Flask-SQLALchemy-RESTFUL-API
RESTFUL JSON API with Flask and SQLALchemy
Tutorial and explanation at http://techarena51.com/index.php/buidling-a-database-driven-restful-json-api-in-python-3-with-flask-flask-restful-and-sqlalchemy/

# Steps to Install

     git clone 
     pip install -r requirements.txt
     gedit config.py
     #Add  and save your database details
     python migrate.py db init
     python migrate.py db migrate
     python migrate.py db upgrade
     python run.py
     
     
HTTP Method	URL	Results
GET	http://localhost:5000/api/v1/users.json	Returns a list of all users
POST	http://localhost:5000/api/v1/users.json	Creates a user and returns with user id
GET	http://localhost:5000/api/v1/users/<user_id>.json	Returns user details for the given user id if the it exists
PATCH	http://localhost:5000/api/v1/users/<user_id>.json	Updates the user details if the user exists and returns with the updated results
DELETE	http://localhost:5000/api/v1/users/<user_id>.json	Deletes the user and returns a 204 on success as per the JSON API spec
