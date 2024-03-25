#!/usr/bin/python3

""" This module defines the BaseTable class which inherits from the Base class. """

from db_storage import DBStorage
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, DateTime, String
from datetime import datetime

Base = declarative_base()

class BaseTable():
        """ This class defines the BaseTable class which
            inherits from the Base class.

            Attributes:
                created_at: A datetime object representing the time
                the record was created.
                updated_at: A datetime object representing
                the time the record was updated.
            Methods:
                __repr__ : A method that returns a string representation
                of the object.
            """
        def __init__(self):
               DBStorage().reload()

        __abstract__ = True

        # created_at attribute using datetime.utcnow() function
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)

        def __repr__(self):
                return f"{type(self).__name__:{self.__dict__}}"
