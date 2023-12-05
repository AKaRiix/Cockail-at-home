from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

# Ajoute cette ligne pour permettre la création de la base de données
db.create_all()

@app.route("/")
def home():
    return render_template("home.html")

# Ajoute cette route pour la page de connexion
@app.route("/login")
def login():
    return render_template("home.html")


from flask import render_template

# ... (autres imports)

@app.route("/recettes")
def recettes():
    return render_template("recettes.html")


from flask import render_template

# ... (autres imports)

@app.route("/contact")
def contact():
    return render_template("contact.html")
