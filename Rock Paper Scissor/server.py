# Rock Paper Scissor - Flask Server

# Imports
from flask import Flask, request, jsonify, render_template
import game
from flask_cors import CORS

# Initialize Flask
app = Flask(__name__, template_folder="C:/Rock Paper Scissor/templates", static_folder="C:/Rock Paper Scissor/templates/assets")
CORS(app)

# Route 1 - Main
@app.route("/")
def route1():
    return render_template("index.html")

# Route 2 - Play
@app.route("/play")
def route3():
    choice = request.args.get("choice")

    items = ["paper", "rock", "scissor"]

    if (choice not in items ):
        return jsonify(message="Invalid Choice", status_code=400), 400
    else:
        response = game.play(choice)
        result = dict(response)["result"]
        computer = dict(response)["computer"]

        return jsonify(user=choice, computer=computer, result=result, status_code=200), 200

# Run Server
if __name__ == "__main__":
    app.run(debug=True, port=7878)