# C: Said Kadrioski <said@kadrioski.de>

from game import Game
from rose import Rose
from copy import deepcopy
from alphaBetaPruningRec import Evaluater
from alphaBetaPruning import eval as evi

evaluater = Evaluater();

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

def alg():
    e = 0
    while e != -1 and e != 1:
        e = int(input("Choose Algorithm (Iterative: 1 or Recursive: 2): ")) * -2 + 3
        if e == 3:
            q()
    return e == 1

def player_play(g: Game):
    e = 0
    while not g.choose(e):
        e = int(input("Enter input (1-9): "))
        if e == 0:
            q()
    return e

def bot_play(game: Game, algorithm: bool):
    l = len(game.history)
    g = deepcopy(game)
    if algorithm:
        r = Rose(g)
        print("using iterative algorithm...")
        evi(r)
        g = r.data
    else:
        print("using recursive algorithm...")
        g = evaluater.eval(game)
    e = abs(g.history[l:][0])
    game.choose(e)
    return e

def main():
    print("Enter 0 to quit")
    p = player()
    b = not botting()
    a = False
    if not b:
        a = alg()
    g = Game()

    while len(g.showfree()) > 0:
        print("Turn of player {}".format(g.player()))
        e = 0
        if g.player() == p or b:
            e = player_play(g)
        else:
            e = bot_play(g, a)
        print("Choice {}".format(e))
        if (g.whowon() != 0):
            break
        print(g)
    g.end_msg()
main()
