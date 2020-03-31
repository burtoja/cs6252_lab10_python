'''
Created on Mar 16, 2020

@author: CS6252
'''
from flask import Blueprint, render_template, request, flash
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


@catalog.route('/product')
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


