from flask import Flask
from .models import db
from .auth import auth_bp
from .views import views_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SECRET_KEY'] = 'your_secret_key'

    db.init_app(app)

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(views_bp, url_prefix='/')

    with app.app_context():
        db.create_all()

    return app
