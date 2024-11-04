from flask import Flask
from shared.utils.db_utils import db
from shared.utils.db_utils import migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@Nish@009@localhost/social_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)

from shared.models import user_model
from shared.models import post_model
