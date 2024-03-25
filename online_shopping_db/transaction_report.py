#!/usr/bin/python3

""" This module defines the TransactionReport class"""

from sqlalchemy import Column, DateTime, String, ForeignKey
from base import BaseTable, Base
from sqlalchemy.orm import Relationship
from customers import Customer
from products import Product    

class TransactionReport(BaseTable, Base):
        
        __tablename__ = 'transaction_reports'

        id = Column(String(128), primary_key=True, nullable=False)
        customer_id = Column(String(128), ForeignKey('customers.id'),
                             nullable=False)
        order_id = Column(String(128), ForeignKey('orders.id'), nullable=False)
        product_id = Column(String(128), ForeignKey('products.id'), nullable=False)
        payment_id = Column(String(128), ForeignKey('payments.id'), nullable=False)
        orders = Relationship('Order', back_populates='transaction_reports')
        products = Relationship('Product', back_populates='transaction_reports')
