from flask import Flask, g
from flask_login import LoginManager

import models

app = Flask(__name__)
app.secret_key = 'aiaskasndasndklasndlkanslk'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id ==userid)
    except models.DoseNotExist:
        return None