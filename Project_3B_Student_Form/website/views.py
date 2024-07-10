from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from .models import db, StudentData, User

views_bp = Blueprint('views', __name__)

@views_bp.route('/')
def home():
    return render_template('home.html')

@views_bp.route('/form', methods=['GET', 'POST'])
def form():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    user_id = session['user_id']
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        standard = request.form.get('standard')
        school = request.form.get('school')
        contact_no = request.form.get('contact_no')
        hindi = int(request.form.get('hindi'))
        math = int(request.form.get('math'))
        science = int(request.form.get('science'))
        history = int(request.form.get('history'))
        english = int(request.form.get('english'))
        full_marks = 500

        if not (0 <= hindi <= 100 and 0 <= math <= 150 and 0 <= science <= 100 and 0 <= history <= 100 and 0 <= english <= 100):
            flash('Marks should be within the valid range')
            return redirect(url_for('views.form'))

        new_data = StudentData(user_id=user_id, first_name=first_name, last_name=last_name, standard=standard, school=school, contact_no=contact_no,
                              hindi=hindi, math=math, science=science, history=history, english=english)
        db.session.add(new_data)
        db.session.commit()
        return redirect(url_for('views.display'))
    return render_template('form.html', user_id=user_id)

@views_bp.route('/display')
def display():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    user_id = session['user_id']
    data = StudentData.query.filter_by(user_id=user_id).first()
    total_marks = data.hindi + data.math + data.science + data.history + data.english
    percentage = (total_marks / 550) * 100
    return render_template('display.html', data=data, total_marks=total_marks, percentage=percentage)
