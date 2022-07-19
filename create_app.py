from flask import Flask
import mysql.connector
from mysql.connector import errorcode
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    
    flask_app = Flask(__name__)
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:adminadmin@ipw.cuvxj8ktqbkz.ap-southeast-2.rds.amazonaws.com/sys'
    flask_app.config['SECRET_KEY'] = os.environ["FLASK_SECRET"]
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_app.config["SESSION_PERMANENT"] = False
    flask_app.config['SESSION_TYPE'] = 'filesystem'

    return flask_app

def connect_database():

    try:

        database_connection = mysql.connector.connect(
            user=os.environ["USER"],
            password=os.environ["PASSWORD"],
            host=os.environ["HOST"],
            database=os.environ["DATABASE"]
        )

    except mysql.connector.Error as error:

        if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Invalid Authorisation: Error with username or password.")
        elif error.errno == errorcode.ER_BAD_DB_ERROR:
            print("Invalid Database: database does not exist.")
        else:
            print(error)

    cursor = database_connection.cursor()

    return cursor