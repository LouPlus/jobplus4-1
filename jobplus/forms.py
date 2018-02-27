from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, ValidationError,BooleanField
from wtforms.validators import length, required
from .models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[required(), length(3, 24)])
    password = PasswordField('Password', validators=[required(), length(6, 24)])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('submit')

    def validate_username(self, field):
        if not User.query.filter_by(username=field.data).first():
            raise ValidationError('Username has not exist!')

    def validate_password(self, field):
        user = User.query.filter_by(username=self.username.data).first()
        if user and not user.check_pwd(field.data):
            raise ValidationError('Incorrect Username or Password!')

