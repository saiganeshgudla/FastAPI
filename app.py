import os
from dotenv import load_dotenv
load_dotenv()  # Load variables from .env file

from flask import Flask, render_template, request, redirect, flash
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "change-me-in-production")

# Google Sheets setup
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    "credentials.json", scope
)

client = gspread.authorize(creds)
sheet = client.open("FlaskUsers").sheet1


@app.route("/")
def home():
    return redirect("/signup")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        users = sheet.get_all_records()

        for user in users:
            if user["username"] == username:
                flash("User already exists!", "error")
                return redirect("/signup")

        hashed_password = generate_password_hash(
            password,
            method="pbkdf2:sha256"
        )

        sheet.append_row([username, hashed_password])

        flash("Signup successful! Please login.", "success")
        return redirect("/login")

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        users = sheet.get_all_records()

        for user in users:
            if user["username"] == username:
                if check_password_hash(user["password"], password):
                    return "Login successful!"
                else:
                    flash("Wrong password", "error")
                    return redirect("/login")

        flash("User not found", "error")
        return redirect("/login")

    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
