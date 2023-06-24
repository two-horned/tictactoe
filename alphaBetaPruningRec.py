# C: Said Kadrioski <said@kadrioski.de>

from time import time
from game import Game,reproduce

def decidefirst():
    g = Game()
    eval(g)
    return g.history[0]

def decide(game: Game):
    g = reproduce(game.history)
    eval(g)
    return abs(g.history[1])

def eval(game: Game):
    s: list[int] = game.symmshowfree()
    if s == []:
        return None
    l: list[Game] = []
    for i in s:
        g = reproduce(game.history)
        g.choose(i)
        if g.whowon() != 0:
            game.history = g.history
            game.board = g.board
            return None
        l.append(g)
    n = l[0]
    if game.player() > 0:
        for i in l:
            eval(i)
            if n.whowon() < i.whowon():
                n = i
    else:
        for i in l:
            eval(i)
            if i.whowon() < n.whowon():
                n = i
    game.history = n.history
    game.board = n.board

def benchmark():
    start = time()
    g = Game()
    eval(g)
    end = time()
    return (g,end - start)

def test():
    print("World's fastest recursive tic tac toe solver")
    print("Look how much time it needed to solve the whole game tree:")
    b = benchmark()
    print("time needed: {}".format(b[1]))
    print("best path: {}".format(b[0].history))
test()
