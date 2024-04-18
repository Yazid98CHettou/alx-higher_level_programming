#!/usr/bin/python3
"""City"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from model_state import Base, State


class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True,
                unique=True, nullable=False,
                autoincrement=True)
    state_id = Column(Integer, ForeignKey('states.id'),
                      nullable=False)
    name = Column(String(128), nullable=False)
