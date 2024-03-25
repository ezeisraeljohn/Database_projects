#!/usr/bin/python3 

""" This module defines the Customer class which inherits
from the BaseTable and Base classes. 
"""

from sqlalchemy import Column, DateTime, String
from sqlalchemy.orm import Relationship
from base import BaseTable, Base
from categories import Category
from products import Product

class Customer(BaseTable, Base):
        
		__tablename__ = 'customers'

		id = Column(String(128), primary_key=True, nullable=False)
		name = Column(String(60), nullable=False)
		phone_number = Column(String(60), nullable=False)
		address = Column(String(60), nullable=False)
		categories = Relationship('Category',
			    back_populates='customers')
		products = Relationship('Product', back_populates='customers')
		order = Relationship('Order', back_populates='customers')
		deliveries = Relationship('Delivery',
			    back_populates='customers')