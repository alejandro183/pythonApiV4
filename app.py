import configparser as configparser
from flask import Flask, Response, json
from flask_jwt_extended import JWTManager
from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes

config = configparser.ConfigParser()
config.read('config.properties')

app = Flask(__name__)

api = Api(app)

app.config['MONGODB_SETTINGS'] = {
    'host': config.get(section='database_config', option='host') + config.get(section='database_config', option='database')
}

@app.route('/')
def base():
    return Response(response=json.dumps({"Status": "UP!!! HOOla holalkhdsa j ", 'db_host': config.get(section='database_config', option='host')}),
                    status=200,
                    mimetype='application/json')

initialize_db(app)
initialize_routes(api)

if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')
