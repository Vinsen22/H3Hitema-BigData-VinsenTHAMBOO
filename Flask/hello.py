#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask
import json
from os import path as os_path
app = Flask(__name__)

@app.route('/hello')
def index():
    return "Hello !"

@app.route('/books/<book>')
def load (book):
    
    PATH = os_path.abspath(os_path.split(__file__)[0])
    with open(PATH + '\\books.json') as json_data:
        data_dict = json.load(json_data)
    #res = data_dict[0]
    for x in data_dict:
        if(x['title'] == book):
            print("Titre : "+x['title'])
            print("je suis dans le if : " + str(x))
            resultat = x
    return resultat

    
if __name__ == '__main__':
    app.run(debug=True) 
    