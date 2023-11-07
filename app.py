from flask import Flask, render_template, request, url_for, flash, redirect

#import pyodbc
app=Flask(__name__)#montre le nom (app) de notre application a flask
app.config['SECRET_KEY']='clés_flash'


@app.route('/')
def connexion():
    return render_template("connexion.html")


@app.route("/accueil/")
def accueil():
    return render_template("acceuil.html")




if __name__== "__main__":
    app.run(debug=True)