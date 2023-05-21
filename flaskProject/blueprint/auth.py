from flask import Blueprint, render_template, jsonify, redirect, url_for, session
from exts import mail, db
from flask_mail import Message
from flask import request
import string
import random
from models import EmailCaptchaModel, UserModel
from . import forms
from .forms import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash


# user management
bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email=email).first()
            if not user:
                print("email not exist as a user!")
                return redirect(url_for("auth.login"))
            if check_password_hash(user.password, password):
                session['user_id'] = user.id
                return redirect("/")
            else:
                print("password error")
                return redirect(url_for("auth.login"))
        else:
            print(form.errors)
            return redirect(url_for(("auth.login")))


@bp.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user = UserModel(email=email, username=username, password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.login"))
        else:
            print(form.email.data, form.username.data)
            return redirect(url_for("auth.register"))


@bp.route("/logout")
def logout():
    session.clear()
    return redirect("/")




@bp.route("/captcha/email")
def get_email_captcha():
    email = request.args.get("email")
    source = string.digits*4
    captcha = random.sample(source, 4)
    captcha = "".join(captcha)
    message = Message(subject="verify code", recipients=[email], body=f"hello! your verify code is {captcha}")
    mail.send(message)
    email_captcha = EmailCaptchaModel(email=email, captcha=captcha)
    db.session.add(email_captcha)
    db.session.commit()
    return jsonify({"code": 200, "message": "", "data": None})




