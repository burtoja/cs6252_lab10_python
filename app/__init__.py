from flask import Flask
from app.model.database import Database

db = Database()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secretkeyforlab10'
    
    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)
    
    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)
    
    from .catalog import catalog as catalog_blueprint
    app.register_blueprint(catalog_blueprint)
    
    from .cart import cart as cart_blueprint
    app.register_blueprint(cart_blueprint)

    return app