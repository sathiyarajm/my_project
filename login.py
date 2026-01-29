from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    result = ""
    if request.method == "POST":
        user = request.form["username"]
        pwd = request.form["password"]

        if user == "admin" and pwd == "1234":
            result = "Login Successful"
        else:
            result = "Login Failed"

    return render_template("login.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
