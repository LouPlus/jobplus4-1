from flask import Blueprint, render_template, redirect
from jobplus.forms import LoginForm
from jobplus.models import User
from flask_login import login_user

front = Blueprint('front', __name__)


@front.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        login_user(user, remember=form.remember_me.data)
        return redirect('??')# TODO:登录后定向页面
    return render_template('login.html', form=form)


