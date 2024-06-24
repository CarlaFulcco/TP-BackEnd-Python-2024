from flask import Flask


app =flask(__name)

"""
    Esto que estamos viendo aca con el 
    @ es un decorator.
    Un decorator es una forma de
    programar (Es un patron de diseño)
    En esencia toma una función y le
    agrega cosas
"""
@app.route(*/*)
def home():
    return 'Hola Mundo Flask'