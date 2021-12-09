from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from sqlalchemy.exc import NoResultFound
from werkzeug.security import check_password_hash, generate_password_hash

from Project import db, app
from Project.Classes import User, Message


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('Guest.html')


@app.route('/add_message', methods=['POST'])
@login_required
def add_message():
    text = request.form['text']

    db.session.add(Message(text))
    db.session.commit()

    return redirect(url_for('main_page'))


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    login = request.form.get('login')
    password = request.form.get('password')

    if login and password:
        user = User.query.filter_by(login=login).first()

        if user and check_password_hash(user.password, password):
            login_user(user)

            next_page = request.args.get('next')

            if next_page is None:
                return redirect(url_for('main_page'))
            else:
                return redirect(next_page)
        else:
            flash('Логин или пароль не верны')
    else:
        flash('Пожалуйста введи логин и пароль')

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    login = request.form.get('login')
    password = request.form.get('password')
    password2 = request.form.get('password2')

    if request.method == 'POST':
        if not (login and password and password2):
            flash('Пожалуйста заполните все поля!')
        elif password != password2:
            flash('Пароли не совпадают!')
        else:
            try:
                hash_pwd = generate_password_hash(password)
                new_user = User(login=login, password=hash_pwd)
                db.session.add(new_user)
                db.session.commit()

                return redirect(url_for('main_page'))
            except:
                flash('Такое имя уже занято!')

    return render_template('register.html')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()

    return redirect(url_for('hello_world'))


@app.after_request
def redirect_to_signing(response):
    if response.status_code == 401:
        return redirect(url_for('login_page') + '?next=' + request.url)

    return response


@app.route('/Messenger', methods=['GET', 'POST'])
@login_required
def main_page():
    return render_template('Auth.html', messages=Message.query.all())
