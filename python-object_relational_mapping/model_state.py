#!/usr/bin/python3
"""Defines a State class mapped to the 'states' table using SQLAlchemy ORM."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Base instance to be used for class definitions
Base = declarative_base()

class State(Base):
    """State class that links to the 'states' MySQL table."""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
