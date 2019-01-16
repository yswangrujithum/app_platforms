

from flask import Flask, render_template, request, Markup, redirect, url_for

import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask_sqlalchemy import SQLAlchemy

# # Create connection to SQL
# engine = create_engine("mysql://root:password@localhost/app_db")
# query='''select * from app_store'''


engine = create_engine(os.environ['DATABASE_URL'])


app = Flask(__name__)

db = SQLAlchemy(app)

@app.route("/", methods=['GET', 'POST'])
def home():
    """Return the Home Page."""
    
    return render_template('templates/index.html')


@app.route('/categories', methods=['GET', 'POST'])
def categories():
    
    
    return render_template('categories.html')

@app.route('/price', methods=['GET', 'POST'])
def price():
    
    
    return render_template('price.html')

@app.route('/ratings', methods=['GET', 'POST'])
def ratings():
    
    
    return render_template('ratings.html')

@app.route('/sizeprice', methods=['GET', 'POST'])
def sizeprice():
    
    
    return render_template('sizeprice.html')

@app.route('/language', methods=['GET', 'POST'])
def language():
    
    
    return render_template('language.html')

@app.route('/catprice', methods=['GET', 'POST'])
def catprice():
    
    
    return render_template('catprice.html')

@app.route('/compare', methods=['GET', 'POST'])
def compare():
    
    
    return render_template('compare.html')

@app.route('/playdata', methods=['GET', 'POST'])
def playdata():
    
    
    return render_template('playdata.html')

@app.route('/appdata', methods=['GET', 'POST'])
def appdata():
    
    
    return render_template('appdata.html')


if __name__ == "__main__":
    app.run(debug=True,threaded=True)