from flask import Flask, render_template, request, redirect
import sqlite3 as sql


app = Flask(__name__,template_folder='templates')

@app.route('/list')
def list():
   con = sql.connect("tietokanta.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from Vinkit")
   
   rows = cur.fetchall(); 
   return render_template("list.html",rows = rows)

   

@app.route("/")
def index():
   return render_template("index.html")

@app.route('/new')
def new():
   return render_template("new.html")

@app.route('/create', methods=["POST"])
def create():
   vinkki = request.form["otsikko"]
   komento = "INSERT INTO Vinkit (Otsikko) VALUES (:vinkki)"
   con = sql.connect("tietokanta.db")
   con.row_factory = sql.Row
   con.isolation_level = None
   
   cur = con.cursor()
   cur.execute(komento, {"vinkki":vinkki})

   return redirect("/list")

app.run(debug = True)