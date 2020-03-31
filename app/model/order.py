'''
Created on Mar 16, 2020

@author: CS6252
'''
import json

class OrderItem():
    """ tracks the items of an order """

    def __init__(self, product_id, quantity):
        '''
        Constructor
        '''
        self.product_id = product_id
        self.quantity = quantity


class Order():
    """ maintains a list of Order objects """
    def __init__(self):
        self.load()

      
    def load(self):
        self.order = []
        order = []
        try:
            with open("app/data/order.json", "rt") as order_file:
                order_json_string = order_file.read()
                order_wrapped = json.loads(order_json_string)
                order = order_wrapped["order"]
        except:
            print("reading from order.json failed")
        
        for item in order:
            item_obj = OrderItem(item["product_id"], item["quantity"])
            self.order.append(item_obj)
    
    
    def get_items(self):
        return self.order
    
    
    def get_item(self, product_id):
        for item in self.order:
            if item.product_id == product_id:
                return item
        return None
    
    
    def add_item(self, product_id, quantity):
        item = self.get_item(product_id)
        if item:
            item.quantity = item.quantity + quantity
        else:
            item = OrderItem(product_id, quantity)
            self.order.append(item)
        self.save()
    
    
    def update_item(self, product_id, quantity):
        item =  self.get_item(product_id)
        if not item:
            return False
        
        if quantity == 0:
            self.order.remove(item)
        else:
            item.quantity = quantity
        
        self.save()
        return True
    
    
    def save(self):
        order = []
        for item in self.order:
            item_dict = {"product_id": item.product_id, "quantity": item.quantity }
            order.append(item_dict)
            
        try:
            with open("app/data/order.json", "wt") as order_file:
                order_file.write(json.dumps({"order": order}))
        except:
            print("writing to file order.json failed")
            return False
        
        return True
