from flask import Flask, request, jsonify

app = Flask(__name__)

BALANCES = {
    'xu': 1000000
}

@app.route("/")
def hello_world():
    return BALANCES
    
@app.route("/balance",methods=['GET'])
def return_balance():
    username = request.args.get('user')
    if username is None:
        return "haha"
    else:
        return "user {} has {} amount of dollars!".format(
        str(username), 
        BALANCES[str(username)]
    )

@app.route("/user",methods=['POST'])
def add_user():
    request_data = request.get_json(force=True)
    user = request_data['user']
    if user not in BALANCES:
        BALANCES[user] = 0
        print(BALANCES[user])
    return "user created!"


if __name__ == '__main__':
    app.run(debug=True)
