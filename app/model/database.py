'''
Created on Mar 16, 2020

@author: CS6252
'''
from app.model.category import Categories
from app.model.product import Products
from app.model.order import Order

class Database:
    """ A database simulation """
    
    def __init__(self):
        self.products = Products()
        self.categories = Categories()
        self.order = Order()

        