from flask import Flask
from python_flask.views import hoteleria

python_flask = Flask(__name__)

python_flask.route("/fourseasons", methods=["GET"])(hoteleria)

if __name__=="__main__":
    app.run(debug=True)