#!/usr/bin/python3

""" This module defines the Payment class"""

from sqlalchemy import Column, DateTime, String, ForeignKey
from base import BaseTable, Base
from sqlalchemy.orm import Relationship
from datetime import datetime


class Payment(BaseTable, Base):

        __tablename__ = 'payment'

        id = Column(String(50), primary_key=True)
        category_id = Column(String(128), ForeignKey('categories.id'))
        date = Column(DateTime, default=datetime.utcnow(), nullable=False)
        customer = Relationship('Customer', back_populates='payment')
