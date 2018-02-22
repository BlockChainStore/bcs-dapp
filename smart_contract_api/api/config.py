# Flask settings
FLASK_SERVER_NAME = 'localhost:8888'
FLASK_DEBUG = True  # Do not use debug mode in production

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False

# SQLAlchemy settings

_file = open('db_pass','r')
_db_user = 'postgres'
_db_pass = str(_file.read().replace('\n',''))
_db_server = 'localhost'
_db_name = 'bcs_db'

SQLALCHEMY_DATABASE_URI = 'postgresql://' + _db_user +':'+ _db_pass +'@'+_db_server +'/'+ _db_name
SQLALCHEMY_TRACK_MODIFICATIONS = False

#L LOG FILE

DEBUG_LOGFILE = 'debug.log'
