#!/usr/python3

""" This module defines the Delivery class"""

from sqlalchemy import Column, String, ForeignKey
from base import Base, BaseTable
from sqlalchemy.orm import Relationship

class Delivery(BaseTable, Base):
        """ The Delivery Class"""

        __tablename__ = 'deliveries'

        id = Column(String(128), primary_key=True, nullable=False)
        customer_id = Column(String(60), ForeignKey('customers.id'), nullable=False)
        customer = Relationship('Customer', back_populates='deliveries')