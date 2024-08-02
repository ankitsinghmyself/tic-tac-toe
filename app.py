from pathlib import Path
from flask import Flask, redirect, render_template, session, url_for
from flask_session import Session

from routes import audio_route

app = Flask(__name__)
app.register_blueprint(audio_route.audio_bp)
sessions_dir = Path(__file__).parent / "sessions"
sessions_dir.mkdir(parents=True, exist_ok=True)
app.config["SESSION_FILE_DIR"] = sessions_dir
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def index():
    if "board" not in session:
        session["board"] = [[None, None, None], [None, None, None], [None, None, None]]
        session["turn"] = "X"
        session["winner"] = False
        session["draw"] = False

    winner = winnerFound(session["board"])

    if winner[0] == True:
        session["winner"] = True
        session["turn"] = winner[1]
        print("winner found", session["winner"], session["turn"])

    elif winner[0] == False and winner[1] == "draw":
        session["draw"] = True

    listen = True
    if session["winner"] == True or session["draw"] == True:
        listen = False

    return render_template(
        "index.html",
        game=session["board"],
        turn=session["turn"],
        winnerFound=session["winner"],
        winner=session["turn"],
        draw=session["draw"],
        listen=listen,
    )


@app.route("/play/<int:row>/<int:col>")
def play(row, col):
    session["board"][row][col] = session["turn"]
    if session["turn"] == "X":
        session["turn"] = "O"
    else:
        session["turn"] = "X"

    return redirect(url_for("index"))


@app.route("/reset")
def reset():
    session["board"] = [[None, None, None], [None, None, None], [None, None, None]]
    session["turn"] = "X"
    session["winner"] = False
    session["draw"] = False
    return redirect(url_for("index"))


def winnerFound(board):
    # print("here at winner")
    # check rows
    for i in range(len(board)):
        if board[i][0] == None:
            break
        if board[i][0] == board[i][1] and board[i][0] == board[i][2]:
            return [True, board[i][0]]
    # check cols
    for i in range(len(board)):
        if board[0][i] == None:
            break
        if board[0][i] == board[1][i] and board[0][i] == board[2][i]:
            return [True, board[0][i]]
    # check diagonals
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        if board[0][0] != None:
            return [True, board[0][0]]
    # check diagonals
    if board[2][0] == board[1][1] and board[2][0] == board[0][2]:
        if board[2][0] != None:
            return [True, board[2][0]]
    # check if game is drawn
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == None:
                return [False, board[0][0]]

    # game is drawn since there is no winner
    # and all boxes are filled
    return [False, "draw"]


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9100, debug=True)
