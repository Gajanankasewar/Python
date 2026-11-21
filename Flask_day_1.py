
from flask import*

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("homee.html")

@app.route("/about")
def about():
    return "aboutpage"

@app.route("/gallary")
def gallery():
    return "our collection"


if __name__ == "__main__":
    app.run(debug=True)
