from flask import Flask, render_template
import random
app = Flask(__name__)

my_college = "ASRJC"
rival_college = "ACJC"
secret_text = "This is my secret"
secret_nums = [1111, 7722, 2, 23323]
secret_info = {"name": "Janelle", "description" : "something", "gender" : "female", "type" : "human"}


@app.route("/")
def home():
    return "<h1>Hello World!</h1><p>This is my page.</p>"

@app.route("/h2comp")
@app.route("/best_subject")
@app.route("/computing")
def computing():
    return "<h1>What is computing?</h1>"

@app.route("/information")
def information():
    return "<h2><em>This is a webapp</em></h2>"

@app.route("/greeting")
def greet():
    return "<h1>HELLOOOOOO</h1>"

@app.route("/about")
def about():
    return render_template("about.html", my_college=my_college, rival_college=rival_college)

@app.route("/secret")
def secret():
    lucky_num = random.choice(secret_nums)
    return render_template("secret.html", secret_text=secret_text, lucky_num=lucky_num, secret_info=secret_info)

if __name__ == "__main__":
    app.run(debug=True)
