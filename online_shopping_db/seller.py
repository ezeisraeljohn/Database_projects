#!/usr/bin/python3

""" This module defines the Seller class"""

from sqlalchemy import Column, DateTime, String, ForeignKey
from base import BaseTable, Base
from sqlalchemy.orm import Relationship
from datetime import datetime

class Seller(BaseTable, Base):
        
        __tablename__ = 'sellers'

        id = Column(String(128), primary_key=True, nullable=False)
        product_id = Column(String(128), ForeignKey('products.id'),
                            nullable=False)
        name = Column(String(60), nullable=False)
        products = Relationship('Product', secondaryjoin='product_seller_pivot'
                                ,back_populates='sellers')