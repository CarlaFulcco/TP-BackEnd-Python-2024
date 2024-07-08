from flask import Flask, jsonify, request
from flask_cors import CORS
from app.views_hoteles import index, get_hotel, create_hotel, get_completed_hoteles, get_archived_hoteles,update_hotel, archive_hotel
from app.database_hoteles import init_app, create_table_Hoteles

app = Flask(__name__)
init_app(app)
CORS(app)

# Rutas

app.route('/', methods=['GET'])(index)
app.route('/api/hoteles/fetch/<int:id_hotel>', methods=['GET'])(get_hotel)
app.route('/api/hoteles/create/', methods=['POST'])(create_hotel)
app.route('/api/hoteles/completed/', methods=['GET'])(get_completed_hoteles)
app.route('/api/hoteles/archived/', methods=['GET'])(get_archived_hoteles)
app.route('/api/hoteles/update/<int:id_hotel>', methods=['PUT'])(update_hotel)
app.route('/api/hoteles/archive/<int:id_hotel>', methods=['DELETE'])(archive_hotel)


if __name__ == '__main__':
    create_table_Hoteles()
    app.run(debug=True)

"""@app.route('/', methods=['GET'])
def index_route():
    return index()

@app.route('/api/hoteles/fetch/<int:id_hotel>', methods=['GET'])
def get_hotel_route(id_hotel):
    return get_hotel(id_hotel)

@app.route('/api/hoteles/create/', methods=['POST'])
def create_hotel_route():
    return create_hotel()

@app.route('/api/hoteles/completed/', methods=['GET'])
def get_completed_hoteles_route():
    return get_completed_hoteles()

@app.route('/api/hoteles/archived/', methods=['GET'])
def get_archived_hoteles_route():
    return get_archived_hoteles()

@app.route('/api/hoteles/update/<int:id_hotel>', methods=['PUT'])
def update_hotel_route(id_hotel):
    return update_hotel(id_hotel)

@app.route('/api/hoteles/archive/<int:id_hotel>', methods=['DELETE'])
def archive_hotel_route(id_hotel):
    return archive_hotel(id_hotel)"""

