from flask import jsonify

def hoteleria():
    response = { "title": "Four Seasons Hotel Madrid⭐⭐⭐⭐⭐"}
    return jsonify(response)