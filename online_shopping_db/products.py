#!/usr/bin/python3 

""" This module defines the Product class which inherits"""

from sqlalchemy import Column, DateTime, String, ForeignKey
from base import BaseTable, Base
from sqlalchemy.orm import Relationship
from categories import Category
from customers import Customer


class Product(BaseTable, Base):
        """ This class defines the Product class which inherits 
        Attributes:
                id: A string representing the product id.
                category_id: A string representing the category id.
                product_name: A string representing the product name.
                categories: A relationship between the product and categories.
        """
        __tablename__ = 'products'

        id = Column(String(128), nullable=False, primary_key=True)
        category_id = Column(String(128), ForeignKey('categories.id'),
                             nullable=False)
        product_name = Column(String(60), nullable=False)
        categories = Relationship('Category', back_populates='products',
                                  cascade='all, delete')
        customers = Relationship('Customer', back_populates='products')
        transaction_reports = Relationship('TransactionReport',
                                           back_populates='products')
        sellers = Relationship('Seller', secondary='product_seller_pivot',
                               back_populates='products')
