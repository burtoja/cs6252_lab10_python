'''
Created on Mar 16, 2020

@author: CS6252
'''
from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db

catalog = Blueprint('catalog', __name__, url_prefix="/catalog", template_folder='templates/catalog')


@catalog.route('/')
def home():
    category_id_string = request.args.get('category_id')
    category_id = 1
    if category_id_string:
        category_id = int(category_id_string)
        
    categories = db.categories.get_categories()
    products = db.products.get_products(category_id)
    category_name = db.categories.get_category(category_id).category_name
    return render_template('catalog.html', category_name=category_name, categories=categories, products=products)


@catalog.route('/product', methods=['GET'])
def product():
    categories = db.categories.get_categories()
    product_id = request.args.get('product_id')
    product = None
    
    if not product_id:
        flash("No product found")
    else:   
        product_id = int(product_id)
        product = db.products.get_product(product_id)
    
    return render_template('product.html', categories=categories, product=product)

@catalog.route('/product', methods=['POST'])
def add_product_to_cart():
    product_id = request.form.get('product_id')
    product_id = int(product_id)
    quantity = request.form.get('quantity')
    quantity = int(quantity)
    
    if not product_id or not quantity:
        flash('Missing product data. Check all fields and try again.')
        return redirect(url_for('catalog.product'))
    
    db.order.add_item(product_id, quantity)
    return redirect(url_for('cart.home'))

