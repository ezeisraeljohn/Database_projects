#!/usr/bin/python3

""" The module that defines the the delivery table"""

from sqlalchemy import create_engine
import base
from sqlalchemy.orm import sessionmaker, scoped_session
import categories
from customers import Customer
from deliveries import Delivery
from payment import Payment
from products import Product
from seller import Seller
from shopping_order import Order


class DBStorage():
        __engine = None
        __session = None
        """ This is used to store information on the db"""

        __engine = create_engine('mysql+mysqldb://israel:#israelEze12@localhost/shopping_db', pool_pre_ping=True)

        def save(self, obj):
                """ Method that saves an object"""
                self.__session.add(obj)

        def all(self, cls=None):
                """ Method that returns all objects"""
                storage_dict = {}
                if cls:
                        for obj in self.__session.query(cls):
                                key = f"{type(obj).__name__}.{obj.id}"
                                storage_dict[key] = obj
                else:
                        for obj in self.__session.query(categories.Category):
                                key = f"{type(obj).__name__}.{obj.id}"
                                storage_dict[key] = obj

        def new(self, obj):
                """ Method that creates a new object"""
                self.save(obj)

        def delete(self, obj):
                """ Method that deletes an object"""
                self.__session.delete(obj)

        def reload(self):
                """ Method that reloads the session"""
                base.Base.metadata.create_all(self.__engine)
                Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
                self.__session = scoped_session(Session)

        def commit(self):
                """ Method that commits the session"""
                self.__session.commit()

        def rollback(self):
                """ Method that rolls back the session"""
                self.__session.rollback()

        def close(self):
                """ Method that closes the session"""
                self.__session.close()