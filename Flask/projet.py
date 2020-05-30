

from flask import Flask, render_template, url_for, request
import json
import pandas as pd 
from os import path as os_path
from sklearn import datasets
from sklearn.linear_model import LogisticRegression 
from datetime import date
import matplotlib.pyplot as plt
app = Flask(__name__)

    
@app.route('/')
def index():
    return render_template('test.html')

@app.route('/test',methods=['POST'])
def load ():
    if request.method =="POST":
        largeur = float(request.form['width'])
        longueur = float(request.form['length'])
        df = datasets.load_iris()
        X = df.data[:,:2] #On récupère uniquement Sepal_width & Sepal_length comme features
        y = (df.target != 0) * 1 
        #On remplace l'ensemble des fleurs ayant un label différent de 0 avec la valeur "1"
        #Pour avoir un problème de classification binaire

        model = LogisticRegression(C=1e20) # construction d'un objet de Régression logistique
        model.fit(X,y)
        Iries_To_Predict = [
            [longueur,largeur ]
        ]
        res = model.predict(Iries_To_Predict)
        return str("D'apres les dimensions saisies de votre fleur, elle est de catégorie : " + str(res[0]))


    
if __name__ == '__main__':
    app.run(debug=True) 
    
    