class BaseConfig(object):
	SECRET_KEY = 'louplus 4-1'

class DevelopmentConfig(BaseConfig):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root@localhost:3306/simpledu?charset=utf8'

class ProductionConfig(DevelopmentConfig):
	DEBUG = False

class TestingConfig(BaseConfig):
	pass

configs = {
	'development': DevelopmentConfig,
	'production': ProductionConfig,
	'testing': TestingConfig
}
