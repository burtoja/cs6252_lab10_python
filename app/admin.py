'''
Created on Mar 16, 2020

@author: CS6252
'''
from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db

admin = Blueprint('admin', __name__, url_prefix='/admin', template_folder='templates/admin')


@admin.route('/')
def home():
    category_id_string = request.args.get('category_id')
    category_id = 1
    if category_id_string:
        category_id = int(category_id_string)
        
    categories = db.categories.get_categories()
    products = db.products.get_products(category_id)
    category_name = db.categories.get_category(category_id).category_name
    return render_template('admin.html', category_name=category_name, categories=categories, products=products)


@admin.route('/add')
def add_product_form():
    categories = db.categories.get_categories()
    return render_template('add_product.html', categories=categories)


@admin.route('/add', methods=['POST'])
def add_product():
    category_id = request.form.get('category_id')
    code = request.form.get('code')
    name = request.form.get('name')
    price = request.form.get('price')
    
    if not category_id or not code or not name or not price :
        flash('Missing product data. Check all fields and try again.')
        return redirect(url_for('admin.add_product_form'))
        
    try:
        price = float(price)
    except:
        flash('Invalid price. Try again.')
        return redirect(url_for('admin.add_product_form'))
    
    category_id = int(category_id)
    db.products.add_product(category_id, code, name, price)
    return redirect(url_for('admin.home', category_id=category_id))


@admin.route('/delete', methods=['POST'])
def delete_product():
    product_id = request.form.get('product_id')
    category_id = request.form.get('category_id')
    
    if not category_id:
        category_id = 1
    else:
        category_id = int(category_id)
    
    if not product_id or not category_id:
        flash('Missing or incorrect product id.')
    else: 
        product_id = int(product_id)
        db.products.delete_product(product_id)

    return redirect(url_for('admin.home', category_id=category_id))
