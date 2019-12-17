#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    """id = Column(String(60), nullable=False, primary_key=True)"""
    cities = relationship("City", cascade="delete", backref="state")

    @property
    def cities(self):
        return(self.cities)
