#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import models
import shlex

class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    """id = Column(String(60), nullable=False, primary_key=True)"""
    cities = relationship("City", cascade="all, delete, delete-orphan",
                          backref="state")

    @property
    def cities(self):
        var = models.storage.all()
        lista = []
        res = []
        for key in var:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                lista.append(var[key])
        for elem in lista:
            if (elem.state_id == self.id):
                res.append(elem)
        return(res)
