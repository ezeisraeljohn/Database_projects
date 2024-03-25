#!/usr/bin/python3 

""" This module defines the Category class which inherits"""

from sqlalchemy import Column, DateTime, String
from sqlalchemy.orm import Relationship
from base import BaseTable, Base
from products import Product
from customers import Customer

class Category(BaseTable, Base):
        """ This class defines the Category class which inherits
        Attribures:
                id: A string representing the category id.
                category_name: A string representing the category name.
                category_type: A string representing the category type.
                products: A relationship between the category and products.
        """
        __tablename__ = 'categories'

        id = Column(String(128), primary_key=True, nullable=False)
        category_name = Column(String(60), nullable=False)
        category_type = Column(String(60), nullable=False)
        products = Relationship('Product', back_populates='categories')
        customers = Relationship('Customer', back_populates='categories')
