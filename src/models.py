from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<People %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }



class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planet_name = db.Column(db.String(120))
    diameter = db.Column(db.Integer)
    rotation_period = db.Column(db.Integer)
    gravity = db.Column(db.Integer)
    population = db.Column(db.Integer)
    climate = db.Column(db.String(80))
    terrian = db.Column(db.String(80))
    surface_water = db.Column(db.Integer)
   

    def __repr__(self):
        return '<Planets %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.planet_name,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrian": self.terrian,
            "surface_water": self.surface_water
            # do not serialize the password, its a security breach
        }

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Characters_name = db.Column(db.String(120))
    gender = db.Column(db.String(80))
    movies = db.Column(db.String(80))
    eye_color = db.Column(db.String(80))
    height = db.Column(db.Integer)
    hair_color = db.Column(db.String(80))
    birth_year = db.Column(db.Integer)
    mass = db.Column(db.Integer)
    homeworld = db.Column(db.String(80))

    def __repr__(self):
        return '<Characters %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "gender": self.gender,
            "movies": self.movies,
            "eye_color": self.eye_color,
            "height": self.height,
            "hair_color": self.hair_color,
            "birth_year": self.birth_year,
            "mass": self.mass,
            "homeworld": self.homeworld
            # do not serialize the password, its a security breach
        }
class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    characters = db.Column(db.String(120))
    planets = db.Column(db.String(80))


    def __repr__(self):
        return '<Favorite %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "characters": self.characters,
            "planets": self.planets
            
            # do not serialize the password, its a security breach
        }
