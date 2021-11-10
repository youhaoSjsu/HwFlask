from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_mapping(

    SECRET_KEY = 'it doesnt matter',
    SQLAlCHEMY_DATABASE_URI = 'sqlite:///site.db'
)


# app.config["SECRET_KEY"] = "13c4cba1f4044c"
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
# db = SQLAlchemy(app)

from city import routes