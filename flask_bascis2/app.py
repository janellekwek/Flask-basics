from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/chickens")
def chickens():
    return "<h1>Info on chickens</h1><p>The chicken is a large and round short-winged bird, domesticated from the red junglefowl of Southeast Asia around 8,000 years ago. Most chickens are raised for food, providing meat and eggs; others are kept as pets or for cockfighting.</p>"

@app.route("/pandas")
def panda():
    return "<h1>Pandas are black and white</h1>"





if __name__ == "__main__":
    app.run(debug=True, port=1234)
