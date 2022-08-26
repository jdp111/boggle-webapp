from boggle import Boggle
from flask import Flask, request, render_template, redirect, session, jsonify
app = Flask(__name__)

boggle_game = Boggle()
app.config['SECRET_KEY'] = "boggleisfun"

@app.route('/')
def game():
    oldboard = session.get("board", False)

    if not oldboard:
        gameBoard = boggle_game.make_board()
        session["board"] = gameBoard

    gameBoard = session["board"]
    
    return render_template("base.html", board = gameBoard)


@app.route('/check-word')
def checkword():
    
    word = request.args.get("word", default = "notavalidword")

    response = {'result' : boggle_game.check_valid_word(session["board"],word)}
    return jsonify(response)
    

