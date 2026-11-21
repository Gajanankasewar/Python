from flask import Flask
app=Flask(__name__)

@app.route("/")
def contact():
    return "<h1>Contact</h1>"

@app.route("/services")
def services():
    return "Our Services"

@app.route("/profile")
def profile():
    return "My Profile"

@app.route("/login")
def login():
    return "<h2>Login</h2>"

@app.route("/register")
def register():
    return "Register"

if __name__ == "__main__":
    app.run(debug=True)