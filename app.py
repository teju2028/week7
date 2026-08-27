from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register():

    name = request.form["name"]
    studentid = request.form["studentid"]
    email = request.form["email"]
    year = request.form["year"]

    return render_template(
        "success.html",
        name=name,
        studentid=studentid,
        email=email,
        year=year
    )

app.run(host="0.0.0.0", port=5050, debug=True)