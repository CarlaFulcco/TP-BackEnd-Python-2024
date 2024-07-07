from flask import jsonify, request
from app.database_hoteles import insert_hoteles, get_completed_hoteles as fetch_completed_hoteles, get_archived_hoteles as fetch_archived_hoteles, get_db


def index():
    return "Welcome to the Hotel API!"

def get_hotel(id_hotel):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM Hoteles WHERE id_hotel = %s", (id_hotel,))
    hotel = cur.fetchone()
    cur.close()
    if hotel:
        return jsonify(hotel)
    else:
        return jsonify({"error": "Hotel not found"}), 404

def create_hotel():
    data = request.get_json()
    insert_hoteles(data['nombre'], data['estrellas'], data['descripcion'], data['mail'], data['telefono'], data['activo'])
    return jsonify({"message": "Hotel created successfully"}), 201

def get_completed_hoteles():
    hotels = fetch_completed_hoteles()
    return jsonify(hotels)

def get_archived_hoteles():
    hotels = fetch_archived_hoteles()
    return jsonify(hotels)

def update_hotel(id_hotel):
    # Function to update hotel
    pass

def archive_hotel(id_hotel):
    # Function to archive hotel
    pass

"""from flask import Flask, jsonify, request
from app.models_hoteles import *
from datetime import date
import psycopg2"""


"""def index():
    return jsonify(
        {
            'mensaje': 'Bienvenid@ a Hoteles'
        }
    )

def get_completed_hoteles():
    hoteles = Hoteles.get_all_completed()
    return jsonify([hotel.serialize() for hotel in hoteles])

def get_archived_hoteles():
    hoteles = Hoteles.get_all_archived()
    return jsonify([hotel.serialize() for hotel in hoteles])

def get_hotel(id_hotel):
    hotel = Hoteles.get_by_id(id_hotel)
    if not hotel:
        return jsonify({'message': 'Hotel not found'}), 404
    return jsonify(hotel.serialize())

def create_hotel():
    data = request.json
    new_hotel = Hoteles(
        nombre=data['nombre'],
        estrellas=data['estrellas'],
        descripcion=data['descripcion'],
        mail=data['mail'],
        telefono=data['telefono'],
        fecha_creacion=date.today().strftime('%Y-%m-%d'),
        activa=True
    )
    new_hotel.save()
    return jsonify({'message': 'Hotel created successfully'}), 201

def update_hotel(id_hotel):
    hotel = Hoteles.get_by_id(id_hotel)
    if not hotel:
        return jsonify({'message': 'Hotel not found'}), 404

    data = request.json
    hotel.nombre = data['nombre']
    hotel.estrellas=data['estrellas']
    hotel.mail=data['mail']
    hotel.telefono=data['telefono']
    hotel.descripcion = data['descripcion']
    hotel.save()
    return jsonify({'message': 'Hotel updated successfully'})

def archive_hotel(id_hotel):
    hotel = Hoteles.get_by_id(id_hotel)
    if not hotel:
        return jsonify({'message': 'Hotel not found'}), 404

    hotel.delete()
    return jsonify({'message': 'Hotel deleted successfully'})"""
