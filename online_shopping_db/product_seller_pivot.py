#!/usr/bin/python3

""" This module defines the ProductSellerPivot class"""

from sqlalchemy import Column, DateTime, String, ForeignKey
from base import BaseTable, Base
from sqlalchemy.orm import Relationship
from datetime import datetime

class ProductSellerPivot(Base):
        """ This class defines the ProductSellerPivot class"""

        __tablename__ = 'product_seller_pivot'

        seller_id = Column(String(128), ForeignKey('sellers.id'),
                           primary_key=True)
        product_id = Column(String(128), ForeignKey('products.id'),
                            primary_key=True)