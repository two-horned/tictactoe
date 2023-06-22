# C: Said Kadrioski <said@kadrioski.de>

from time import time
from game import Game
from rose import Rose
from copy import deepcopy

def decidefirst() -> int:
    rose = Rose(Game())
    eval(Rose(Game()))
    print("This is the best path I see: {}".format(rose.data.history))
    g = rose.data
    if len(g.history) < 1:
        quit("there was nothing to do")
    return abs(g.history[0])

def decide(rose: Rose) -> int:
    eval(rose)
    print("This is the best path I see: {}".format(rose.data.history))
    g = rose.data
    if len(g.history) < 2:
        quit("there was nothing to do")
    return abs(g.history[1])

def allfinished(rose: Rose):
    b = True
    for i in rose.children:
        b = b and i.data.finished()
    return b

def minmax(rose: Rose):
    n = rose.children[0]
    if rose.data.player() > 0:
        for i in rose.children:
            if n.data.whowon() < i.data.whowon():
                n = i
    else:
        for i in rose.children:
            if i.data.whowon() < n.data.whowon():
                n = i
    return n

def prune(rose: Rose):
    q = [rose]
    f: dict[str, Rose] = {}
    while q != []:
        r = q.pop()
        h = str(sorted(r.data.history))
        f.update({h : r})
        r.data = minmax(r).data
        r.children = []
        if r.father != None and allfinished(r.father):
            q.append(r.father)
    return f

def eval(rose: Rose):
    q = [rose]
    f: dict[str, Rose] = {}
    while q != []:
        r = q.pop()
        h = r.data.history
        if str(sorted(h)) not in f:
            s = r.data.symmshowfree()
            for i in s:
                g: Game = deepcopy(r.data)
                g.choose(i)
                if g.finished():
                    r.data     = g
                    r.children = []
                    break
                else:
                    n = Rose(g)
                    n.father = r
                    r.children.append(n)
            q += r.children
        else:
            n = f.get(str(sorted(h)))
            if n != None:
                r.data.board = n.data.board
                r.data.history += n.data.history[len(h):]

        if r.data.finished() and r.father != None and allfinished(r.father):
            f.update(prune(r.father))

def benchmark():
    start = time()
    r = Rose(Game())
    eval(r)
    end = time()
    return (r,end - start)

def test():
    print("World's fastest iterative tic tac toe solver")
    print("Look how much time it needed to solve the whole game tree:")
    b = benchmark()
    print("time needed: {}".format(b[1]))
    print("best path: {}".format(b[0].data.history))
test()
