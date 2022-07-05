import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class People(Base):
    __tablename__ = "people"
    name = Column(String(256))
    height = Column(Float)
    mass = Column(String(256))
    hair_color = Column(String(256))
    skin_color = Column(String(256))
    eye_color = Column(String(256))
    birth_year = Column(String(256))
    gender = Column(String(256))
    homeworld = Column(String(256))
    id = Column(Integer, primary_key=True)


class Planets(Base):
    __tablename__ = "planets"
    name = Column(String(256))
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    diameter = Column(Integer)
    climate = Column(String(256))
    gravity = Column(Integer)
    terrain = Column(String(256))
    surface_water = Column(Integer)
    population = Column(Integer)
    id = Column(Integer, primary_key=True)


class Starships(Base):
    __tablename__ = "starships"
    name = Column(String(256))
    model = Column(String(256))
    manufacturer = Column(String(256))
    cost_in_credits = Column(Integer)
    length = Column(Integer)
    max_atmosphering_speed = Column(Integer)
    passengers = Column(Integer)
    cargo_capacity = Column(Integer)
    id = Column(Integer, primary_key=True)


class User(Base):
    __tablename__ = "user"
    username = Column(String(256))
    firstname = Column(String(256))
    lastname = Column(String(256))
    email = Column(String(256))
    favorites = relationship("favorites")
    id = Column(Integer, primary_key=True)


class Favorites(Base):
    __tablename__ = "favorites"
    planet = Column(String(256))
    people = Column(String(256))
    user_id = Column(Integer, ForeignKey("user.id"))
    id = Column(Integer, primary_key=True)

    def to_dict(self):
        return {}


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
