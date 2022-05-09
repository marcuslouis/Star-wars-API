"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, People, Planets, Characters
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/people', methods=['GET'])
def handle_people():

    people = People.query.all()
    people_list = list(map(lambda x: x.serialize(),people))
    return jsonify(people_list), 200


@app.route('/people/<int:people_id>', methods=['GET'])
def handle_onePerson():
    people = People.query.get(people_id)
    return jsonify(people.serialize)

@app.route('/people', methods=['POST'])
def create_people():
    request_body = request.get_json()
    new_people = People(email=request_body['email'], password=request_body['password'], is_active=request_body['is_active'])
    db.session.add(new_people)
    db.session.commit()
    return f"The new people {request_body['email']} was created successfully", 200


@app.route('/people', methods=['DELETE'])
def delete_people():
    people = People.query.get(people_id)
    if people is None:
        raise APIException('User not found', status_code=404)
    db.session.delete(people)
    db.session.commit()
    return jsonify(people)


@app.route('/planets', methods=['GET'])
def handle_planets():

    planets = Planets.query.all()
    planets_list = list(map(lambda x: x.serialize(), planets))
    return jsonify(planets_list), 200


@app.route('/planets/<int:planets_id>', methods=['GET'])
def handle_onePlanets():
    planets = Planets.query.get(planets_id)
    return jsonify(planets.serialize)


@app.route('/planets', methods=['POST'])
def create_planets():
    request_body = request.get_json()
    new_planets = Planets(planet_name=request_body['planet_name'], diameter=request_body['diameter'], rotation_period=request_body['rotation_period'],gravity=request_body['gravity'], population=request_body['population'], climate=request_body['climate'],terrian=request_body['terrian'], surface_water=request_body['surface_water'])
    db.session.add(new_planets)
    db.session.commit()
    return f"The new planet {request_body['planet_name']} was created successfully", 200


@app.route('/planets', methods=['DELETE'])
def create_planets():
     planets = Planets.query.get(planets_id)
    if planets is None:
        raise APIException('User not found', status_code=404)
    db.session.delete(planets)
    db.session.commit()
    return jsonify(planets)

@app.route('/characters', methods=['GET'])
def handle_characters():

    characters  = Characters.query.all()
    character_list = list(map(lambda x: x.serialize(),characters))
    return jsonify(character_list), 200


@app.route('/characters/<int:character_id>', methods=['GET'])
def handle_onecharacter():
    character = Characters.query.get(character_id)
    return jsonify(character.serialize)


@app.route('/characters', methods=['POST'])
def create_characters():
    request_body = request.get_json()
    new_character = Characters(Characters_name=request_body['Characters_name'], gender=request_body['gender'], movies=request_body['movies'],eye_color=request_body['eye_color'], height=request_body['height'], hair_color=request_body['hair_color'], birth_year=request_body['birth_year'], mass=request_body['mass'], homeworld=request_body['homeworld'])
    db.session.add(new_characters)
    db.session.commit()
    return f"The new character {request_body['Characters_name']} was created successfully", 200

@app.route('/characters', methods=['DELETE'])
def create_characters():
    character = Characters.query.get(characters_id)
    if character is None:
        raise APIException('User not found', status_code=404)
    db.session.delete(character)
    db.session.commit()
    return jsonify(character)


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
