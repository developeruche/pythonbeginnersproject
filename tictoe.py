##This applacation was placed on hold for somw reasons... sorry

board = {
    "top-left": " ",
    "top-middle": " ",
    "top-right": " ",
    "mid-left": " ",
    "mid-mid": " ",
    "mid-right": " ",
    "bottom-left": " ",
    "bottom-middle": " ",
    "bottom-right": " ",
}

def drawBoard(a, b, c, d, e, f, g, h, i):
    print(f" {a} | {b} | {c} ")
    print("-----------")
    print(f" {d} | {e} | {f} ")
    print("-----------")
    print(f" {g} | {h} | {i} ")


def theGame(playerOne):
    computerFigure = None
    if(playerOne == "X"):
        computerFigure = "O"
    else:
      computerFigure = "X"
    drawBoard(board["top-left"], board["top-middle"], board["top-right"], board["mid-left"], board["mid-mid"], board["mid-right"], " ", " ", " ")