class BaseConfig(object):
<<<<<<< HEAD
	SECRET_KEY = 'louplus 4-1'
=======
	pass
>>>>>>> a90bdf8aa8ed754b02c8f083e1caae3bd19d3b8f

class DevelopmentConfig(BaseConfig):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root@localhost:3306/simpledu?charset=utf8'

<<<<<<< HEAD
class ProductionConfig(DevelopmentConfig):
	DEBUG = False
=======
class ProductionConfig(BaseConfig):
	pass
>>>>>>> a90bdf8aa8ed754b02c8f083e1caae3bd19d3b8f

class TestingConfig(BaseConfig):
	pass

configs = {
	'development': DevelopmentConfig,
	'production': ProductionConfig,
	'testing': TestingConfig
}
