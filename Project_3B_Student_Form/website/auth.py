from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from .models import db, User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                session['user_id'] = user.id
                return redirect(url_for('views.form'))
            else:
                flash('Wrong password')
        else:
            flash('Email not registered, kindly sign up')
    return render_template('login.html')

@auth_bp.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        if password != confirm_password:
            flash('Passwords do not match')
            return redirect(url_for('auth.sign_up'))

        if len(password) < 5:
            flash('Password must be at least 5 characters long')
            return redirect(url_for('auth.sign_up'))

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already in use')
            return redirect(url_for('auth.sign_up'))

        new_user = User(email=email, password=generate_password_hash(password, method='pbkdf2:sha256'))
        db.session.add(new_user)
        db.session.commit()
        flash('Account successfully created')
        return redirect(url_for('auth.login'))
    return render_template('sign-up.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('auth.login'))
