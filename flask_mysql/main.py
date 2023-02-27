import re

import MySQLdb.cursors
from flask import Flask, redirect, render_template, request, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key = "your secret key"
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "password"
app.config["MYSQL_DB"] = "geekprofile"
mysql = MySQL(app)


@app.route("/login", methods=["GET", "POST"])
def login():
    msg = ""
    if request.method == "POST" and "username" in request.form and "password" in request.form:
        username = request.form["username"]
        password = request.form["password"]
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(
        "SELECT * FROM accounts WHERE username = % s AND password = % s",
        (
            username,
            password,
        ),
    )
    account = cursor.fetchone()
    if account:
        msg = "Logged in successfully !"
        return render_template("index.html", msg=msg)
    else:
        msg = "Incorrect username / password !"
        return render_template("login.html", msg=msg)


@app.route("/register", methods=["GET", "POST"])
def register():
    msg = ""
    if (
        request.method == "POST"
        and "username" in request.form
        and "password" in request.form
        and "email" in request.form
        and "address" in request.form
        and "city" in request.form
        and "country" in request.form
        and "postalcode" in request.form
        and "organisation" in request.form
    ):
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        organisation = request.form["organisation"]
        address = request.form["address"]
        city = request.form["city"]
        state = request.form["state"]
        country = request.form["country"]
        postalcode = request.form["postalcode"]
        if account:
            msg = "Account already exists !"
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            msg = "Invalid email address !"
        elif not re.match(r"[A-Za-z0-9]+", username):
            msg = "name must contain only characters and numbers !"
        else:
            cursor.execute(
                "INSERT INTO accounts VALUES (NULL, % s, % s, % s, % s, % s, % s, % s, % s, % s)",
                (
                    username,
                    password,
                    email,
                    organisation,
                    address,
                    city,
                    state,
                    country,
                    postalcode,
                ),
            )
            mysql.connection.commit()
            msg = "You have successfully registered !"
    elif request.method == "POST":
        msg = "Please fill out the form !"
        return render_template("register.html", msg=msg)
