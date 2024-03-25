#!/usr/bin/python3 

""" This module defines the Product class which inherits"""

from sqlalchemy import Column, DateTime, String, ForeignKey
from base import BaseTable, Base
from sqlalchemy.orm import Relationship
from categories import Category
from customers import Customer
from datetime import datetime

class Order(BaseTable, Base):
        ___tablename__ = 'orders'

        id = Column(String(128), primary_key=True, nullable=False)
        customer_id = Column(String(128), ForeignKey('customers.id'),
                             nullable=False)
        date = Column(DateTime, nullable=False, default=datetime.utcnow())
        customer = Relationship('Customer', back_populates='orders')
        transaction_reports = Relationship('TransactionReport',
                                           back_populates='orders')
