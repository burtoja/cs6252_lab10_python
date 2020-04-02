'''
Created on April 2, 2020

@author: A. Burton
'''
from flask import Blueprint, render_template
from . import db
from app.model.cartitem import CartItem

cart = Blueprint('cart', __name__, url_prefix="/cart", template_folder='templates/cart')


@cart.route('/', methods=['GET', 'POST'])
def home():
    cart_items = db.order.get_items()
    cart = []
    for item in cart_items:
        product_id = item.product_id
        product_name = db.products.get_product(product_id).product_name
        quantity = item.quantity
        unit_price = db.products.get_product(product_id).price
        total_price = unit_price * quantity      
        cart_item = CartItem(product_id, product_name, quantity, unit_price, total_price)
        cart.append(cart_item)

    return render_template('cart.html', cart=cart)

