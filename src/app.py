from flask import Flask

from src.common.database import Database

__author__ = "abhishekmadhu"

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = "abhishek"

@app.before_first_request
def initialize_database():
    Database.initialize()


from src.models.users.views import user_blueprint
app.register_blueprint(user_blueprint, url_prefix="/users")