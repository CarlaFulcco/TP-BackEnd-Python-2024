from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from app import views_hoteles
from app.database_hoteles import init_app, create_table_Hoteles

init_app(app)

create_table_Hoteles()