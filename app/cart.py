'''
Created on April 2, 2020

@author: A. Burton
'''
from flask import Blueprint, render_template, request, redirect, url_for
from . import db
from app.model.cartitem import CartItem

cart = Blueprint('cart', __name__, url_prefix="/cart", template_folder='templates/cart')


@cart.route('/', methods=['GET'])
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


@cart.route('/', methods=['POST'])
def update_cart():
    product_id = request.form.get('product_id')
    product_id = int(product_id)
    quantity = request.form.get('quantity')
    quantity = int(quantity)
    print('PRODUCTID={} QTY={}'.format(product_id, quantity))
    db.order.update_item(product_id, quantity)

    return redirect(url_for('cart.home'))












