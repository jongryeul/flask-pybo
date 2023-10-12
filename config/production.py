from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'B\xb8\xa5\x8a\xaa~\xd3\xee\x89@k\x1c\xd2&|\xc3'
