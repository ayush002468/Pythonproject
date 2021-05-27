from datetime import date

import mongoengine as mongoengine
from flask import Flask, make_response
from flask import jsonify
from flask import request
from flask_mongoengine import MongoEngine
from flask_pymongo import PyMongo
from pyhtonconstants import password

app = Flask(__name__)

database_name = "Api"
DB_URI = "mongodb+srv://DBUSER:{}@cluster0.fagnp.mongodb.net/{}?retryWrites=true&w=majority".format(password,
                                                                                                    database_name)
app.config["MONGODB_HOST"] = DB_URI
db = MongoEngine()
db.init_app(app)


# psushing to collection
class Appointment(db.Document):
    title = db.StringField()
    start_date = db.IntField()
    end_date = db.IntField()

    # converts to json

    def to_json(self):
        return {
            "title": self.title,
            "start_date": self.start_date,
            "end_date": self.end_date,
        }


@app.route('/Api/db_populate', methods=['POST'])
def db_populate():
    appointment1 = Appointment(title="kumar", start_date=22 / 5 / 2020, end_date=23 / 5 / 2021)
    appointment2 = Appointment(title="singh", start_date=23 / 6 / 2020, end_date=26 / 7 / 2021)
    appointment1.save()
    appointment2.save()
    return make_response("", 200)


@app.route('/Api/Appointment', methods=['GET', 'POST'])
def api_appointment():
    if request.method == "GET":
        pass
    elif request.method == "POST":
        pass


@app.route('/Api/Appointment/<title>', methods=['GET', 'POST', 'PUT'])
def Api_Appointment():
    if request.method == "GET":
        Appointment = []
        for appointment in Appointment.objects:
            Appointment.append(appointment)
            return make_response(jsonify(appointment), 200)
        pass




    elif request.method == "POST":
        content = request.json
        appointment = Appointment(title=content['title'], start_date=content['start_date'],
                                  end_date=content['end_date'])
        appointment.save();
        return ("", 200)
        pass


if __name__ == '__main__':
    app.run(debug=True)
