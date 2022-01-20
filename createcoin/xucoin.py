from flask import Flask, render_template

app = Flask(__name__)

BALANCES = {
    "xu": 1000000
}

# how to get params 
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/balance", methods=["POST", "GET"])
def balance():
    pass
    # return render_template('login.html')

@app.route("/<usr>")
def user(usr): 
    pass
    # return f"<h1>{usr}</h1>"

@app.route("/")
def transfer_from_to(): 
    pass

if __name__ == "__main__": 
    app.run(debug=True)

# TODO:able to finish three operations of client.py