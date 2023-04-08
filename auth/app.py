from flask import Flask

app: Flask = Flask(__name__)

# For dev
app.config.from_object('auth.default_config.Config')
# For deployment
app.config.from_pyfile('config.py')
