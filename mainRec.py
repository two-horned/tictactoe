# C: Said Kadrioski <said@kadrioski.de>

from game import Game
from alphaBetaPruningRec import decide,decidefirst

def q():
    quit("Exiting...")

def player():
    e = 0
    while e != -1 and e != 1:
        e = int(input("Choose player (1 or 2): ")) * -2 + 3
        if e == 3:
            q()
    return e

def botting():
    b=""
    while b != "y" and b != "n":
        b = str(input("Play with bot? [y,n]: "))
        if b == 0:
            q()
    match b:
        case "y":
            b = True
        case "n":
            b = False
    return b

def player_play(g: Game):
    e = 0
    while not g.choose(e):
        e = int(input("Enter input (1-9): "))
        if e == 0:
            q()
    return e

def bot_play(game: Game):
    h = []
    if game.history != []:
        h = [game.history[-1]]
    g = Game(h,game.board)
    d = decide(g)
    game.choose(d)
    return d

def main():
    print("Enter 0 to quit")
    p = player()
    b = not botting()
    g = Game()

    while len(g.showfree()) > 0:
        print("Turn of player {}".format(g.player()))
        e = 0
        if g.player() == p or b:
            e = player_play(g)
        else:
            if g.history == []:
                e = decidefirst()
            else:
                e = bot_play(g)
        print("Choice {}".format(e))
        if (g.whowon() != 0):
            break
        print(g)
    g.end_msg()

main()