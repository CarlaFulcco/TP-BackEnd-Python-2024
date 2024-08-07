import os
from app.database_hoteles import get_db
import psycopg2
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy


class Hoteles:
    def __init__(self, id_hotel=None, nombre=None, estrellas=None, descripcion=None, mail=None, telefono=None, activa=None):
        self.id_hotel = id_hotel
        self.nombre = nombre
        self.estrellas = estrellas
        self.descripcion = descripcion
        self.mail = mail
        self.telefono = telefono
        self.activa = activa

    @staticmethod
    def __get_hoteles_by_query(query):
        db = get_db()
        cursor = db.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
    
        hoteles = []
        for row in rows:
            hoteles.append(
                Hoteles(
                    id_hotel=row[0],
                    nombre=row[1],
                    estrellas=row[2],
                    descripcion=row[3],
                    mail=row[4],
                    telefono=row[5],
                    activa=row[6]
                )
            )
        cursor.close()
        return hoteles

    @staticmethod
    def get_all_completed():
        return Hoteles.__get_hoteles_by_query(
            """ SELECT * FROM Hoteles WHERE activo = true ORDER BY id_hotel""")

    @staticmethod
    def get_all_archived():
        return Hoteles.__get_hoteles_by_query(
            """ SELECT * FROM Hoteles WHERE activo = false ORDER BY id_hotel""")
        
    @staticmethod
    def get_all_hoteles():
        return Hoteles.__get_hoteles_by_query(
            """ SELECT * FROM Hoteles ORDER BY id_hotel""")    
    
    @staticmethod
    def get_by_id(id_hotel):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Hoteles WHERE id = %s", (id_hotel,))
        row = cursor.fetchone()
        cursor.close()

        if row:
            return Hoteles(
                id_hotel=row[0],
                nombre=row[1],
                estrellas=row[2],
                descripcion=row[3],
                mail=row[4],
                telefono=row[5],
                activa=row[6]
            )
        return None

    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id_hotel:
            cursor.execute(
                """
                    UPDATE Hoteles
                    SET nombre = %s, estrellas = %s, descripcion = %s, mail = %s, telefono = %s, activa = %s
                    WHERE id_hotel = %s
                """,
                (self.nombre, self.estrellas, self.descripcion, self.mail, self.telefono, self.activa, self.id_hotel)
            )
        else:
            cursor.execute(
                """
                    INSERT INTO Hoteles
                    (nombre, estrellas, descripcion, mail, telefono, activa)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (self.nombre, self.estrellas, self.descripcion, self.mail, self.telefono, self.activa)
            )
            self.id_hotel = cursor.fetchone()[0]
        db.commit()
        cursor.close()

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("UPDATE Hoteles SET activa = false WHERE id_hotel = %s", (self.id_hotel,))
        db.commit()
        cursor.close()

    def serialize(self):
        return {
            'id_hotel': self.id_hotel,
            'nombre': self.nombre,
            'estrellas': self.estrellas,
            'descripcion': self.descripcion,
            'mail': self.mail,
            'telefono': self.telefono,
            'activa': self.activa
        }