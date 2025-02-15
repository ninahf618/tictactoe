from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

game_board = [['' for _ in range(3)] for _ in range(3)]
current_player = 'O'

def check_winner():
    for i in range(3):
        if game_board[i][0] == game_board[i][1] == game_board[i][2] and game_board[i][0] != '':
            return game_board[i][0]
        if game_board[0][i] == game_board[1][i] == game_board[2][i] and game_board[0][i] != '':
            return game_board[0][i]

    if game_board[0][0] == game_board[1][1] == game_board[2][2] and game_board[0][0] != '':
        return game_board[0][0]
    if game_board[0][2] == game_board[1][1] == game_board[2][0] and game_board[0][2] != '':
        return game_board[0][2]

    if all(cell != '' for row in game_board for cell in row):
        return "Tie"

    return None

@app.route("/", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def index():
    global current_player

    if request.method == "POST":
        if "position" in request.form:  
            row_col = request.form["position"]  
            if "-" in row_col: 
                row, col = map(int, row_col.split('-'))  

                if game_board[row][col] == '':  
                    game_board[row][col] = current_player
                    winner = check_winner()

                    if winner:
                        return render_template("index.html", board=game_board, winner=winner, current_player=current_player)

                    current_player = 'X' if current_player == 'O' else 'O'

    return render_template("index.html", board=game_board, winner=None, current_player=current_player)

@app.route("/reset")
def reset():
    global game_board, current_player
    game_board = [['' for _ in range(3)] for _ in range(3)]
    current_player = 'O'
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
