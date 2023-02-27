from flask import Flask, make_response, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("cookies.html")


@app.route("/setcookie", methods=["POST", "GET"])
def setcookie():
    if request.method == "POST":
        user = request.form["nm"]
        resp = make_response(render_template("readcookies.html"))
        resp.set_cookie("userID", user)
        return resp


@app.route("/getcookie")
def getcookie():
    name = request.cookies.get("userID")
    print(name)
    if name is None:
        return "<h1>Cookied `userID` does not exist</h1>"
    return f"<h1>welcome {name}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
