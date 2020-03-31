'''
Created on Mar 16, 2020

@author: CS6252
'''
import json

class Product():
    """ tracks a product """

    def __init__(self, product_id, category_id, product_code, product_name, price):
        '''
        Constructor
        '''
        self.product_id = product_id
        self.category_id = category_id
        self.product_code = product_code
        self.product_name = product_name
        self.price = price
        

class Products():
    """ maintains a list of Product objects """
    def __init__(self):
        self.max_id = 0
        self.products = []
        self.load()

      
    def load(self):
        products = []
        try:
            with open("app/data/products.json", "rt") as products_file:
                products_json_string = products_file.read()
                products_wrapped = json.loads(products_json_string)
                products = products_wrapped["products"]
        except:
            print("reading from products.json failed")
        
        for product in products:
            product_obj = Product(product["product_id"], product["category_id"], product["product_code"], product["product_name"], product["price"])
            if product["product_id"] > self.max_id:
                self.max_id = product["product_id"]
            self.products.append(product_obj)
    
    
    def get_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
          
        return None


    def get_products(self, category_id=None):
        if not category_id:
            return self.products
           
        products = []
        for product in self.products:
            if product.category_id == category_id:
                products.append(product)
          
        return products
    
    
    def add_product(self, category_id, product_code, product_name, price):
        self.max_id = self.max_id + 1
        product = Product(self.max_id, category_id, product_code, product_name, price)
        self.products.append(product)
        self.save()
    
    
    def delete_product(self, product_id):
        print("Delete product with id {}".format(product_id))
        product_to_delete = None
        for product in self.products:
            if product.product_id == product_id:
                product_to_delete = product
        
        if product_to_delete:
            self.products.remove(product_to_delete)
            self.save()
        
        
    def save(self):
        products = []
        for product in self.products:
            product_dict = {"product_id": product.product_id, "category_id": product.category_id, "product_code": product.product_code, "product_name": product.product_name, "price": product.price }
            products.append(product_dict)
            
        try:
            with open("app/data/products.json", "wt") as products_file:
                products_file.write(json.dumps({"products": products}))
        except:
            print("writing to file products.json failed")
            return False
        
        return True
