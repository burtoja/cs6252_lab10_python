'''
Created on Mar 16, 2020

@author: AnjaRemshagen
'''
class CartItem():
    """ tracks an item in a cart """

    def __init__(self, product_id, product_name, quantity, unit_price, total_price):
        '''
        Constructor
        '''
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity
        self.unit_price = unit_price
        self.total_price = total_price