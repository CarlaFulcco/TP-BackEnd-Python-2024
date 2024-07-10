from flask import jsonify, request
from app.database_hoteles import *
import psycopg2
from app.models_hoteles import Hoteles


def index():
    return jsonify({'mensaje': 'Bienvenid@ a Hoteles'})


def get_completed_hoteles():
    hoteles = Hoteles.get_all_completed()
    return jsonify([hotel.serialize() for hotel in hoteles])


def get_archived_hoteles():
    hoteles = Hoteles.get_all_archived()
    return jsonify([hotel.serialize() for hotel in hoteles])


def get_all_hoteles():
    hoteles = Hoteles.get_all_hoteles()
    return jsonify([hotel.serialize() for hotel in hoteles])


def get_hotel(id_hotel):
    hotel = Hoteles.get_by_id(id_hotel)
    if not hotel:
        return jsonify({'message': 'Hotel not found'}), 404
    return jsonify(hotel.serialize())


def create_hotel():
    data = request.json()
    hotel = Hoteles(
        nombre=data['nombre'],
        estrellas=data['estrellas'],
        descripcion=data['descripcion'],
        mail=data['mail'],
        telefono=data['telefono'],
        activa=True
    )
    hotel.save()
    return jsonify({'message': 'Hotel created successfully'}), 201


def update_hotel(id_hotel):
    hotel = Hoteles.get_by_id(id_hotel)
    if not hotel:
        return jsonify({'message': 'Hotel not found'}), 404

    data = request.json
    hotel.nombre = data['nombre']
    hotel.estrellas = data['estrellas']
    hotel.mail = data['mail']
    hotel.telefono = data['telefono']
    hotel.descripcion = data['descripcion']
    hotel.save()
    return jsonify({'message': 'Hotel updated successfully'})


def archive_hotel(id_hotel):
    hotel = Hoteles.get_by_id(id_hotel)
    if not hotel:
        return jsonify({'message': 'Hotel not found'}), 404

    hotel.delete()
    return jsonify({'message': 'Hotel archived successfully'})
