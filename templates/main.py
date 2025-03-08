from flask import Flask, render_template, session, redirect

import os

from question import questions

from resultat import resultats

app = Flask("Mon_questionnaire")

app.secret_key = os.urandom(24)

@app.route("/")
def Page_acceuil():
    session["numero_question"] = 0
    session["score"] = {"Pikachu" : 0, "Mew" : 0, "Salamèche":0, "Carapuce":0}
    return render_template("Page_accueil.html")


app.run(host = "0.0.0.0",port = 80)