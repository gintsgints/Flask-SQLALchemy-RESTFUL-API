from flask import Flask, Response

class MyResponse(Response):
     default_mimetype = 'application/xml'
     
    

# http://flask.pocoo.org/docs/0.10/patterns/appfactories/
def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    app.response_class = MyResponse

    from app.models import db
    db.init_app(app)

    # Blueprints   
    from app.users.views import users
    app.register_blueprint(users, url_prefix='/api/v1/users')
    
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
        return response

    return app
    