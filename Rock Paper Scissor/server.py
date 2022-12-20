# Flask Server - Rock Paper Scissor

# Imports
from flask import Flask, request, jsonify
import game

# Initialize Flask
app = Flask(__name__)

# Route 1
@app.route("/")
def route1():
    return jsonify(message="This is the Rock Paper Scissor game", status_code=200), 200

# Route 2
@app.route("/play")
def route2():
    choice = request.args.get("choice")

    items = ["paper", "rock", "scissor"]

    if (choice not in items ):
        return jsonify(message="Invalid Choice", status_code=400), 400
    else:
        response = game.play(choice)
        final = dict(response)["Final"]
        computerChoice = dict(response)["Computer"]

        return jsonify(user=choice, result=final, computer=computerChoice, status_code=200), 200

# Run Server
app.run(port=7878)
