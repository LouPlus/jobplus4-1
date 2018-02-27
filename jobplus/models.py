from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Base(db.Model):
	__abstract__ = True
	create_at = db.Column(db.DateTime, default=datetime.utcnow)
	update_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class User(Base):
	__tablename__ = 'user'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(24), unique=True, index=True, nullable=False)
	_password = db.Column('password',db.String(256), nullable=False)

	def __repr__(self):
		return '<User:{}'.format(self.username)

	@property
	def password(self):
		return self._password

	@password.setter
	def password(self, orig_password):
		self._password = generate_password_hash(orig_password)

	def check_pwd(self, password):
		return check_password_hash(self._password, password)



	