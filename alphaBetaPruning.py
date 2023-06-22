# C: Said Kadrioski <said@kadrioski.de>

from time import time
from game import Game
from rose import Rose
from copy import deepcopy

OPTIMIZED = True

def decide(rose: Rose) -> Game:
    eval(rose)
    print(rose.data.history)
    return rose.leaves()[0].data

def allfinished(rose: Rose):
    b = True
    for i in rose.children:
        b = b and i.data.finished()
    return b

def minmax(rose: Rose):
    n = rose.children[0]
    if rose.data.player() == 1:
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
        if not OPTIMIZED or str(sorted(h)) not in f:
            s = r.data.showfree()
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
                h += n.data.history[len(h):]
                r.data = deepcopy(n.data)
                r.data.history = h

        if r.data.finished() and r.father != None and allfinished(r.father):
            f.update(prune(r.father))

# Functions used for validating, no significance
def dddd(r):
   return r.data.history

def wwww(r):
   return r.data.whowon()

def ffff(r):
    return r.data.finished()

def fdfd(r):
    if r.data.finished():
        return ""
    else:
        return len(r.children)

def benchmark():
    start = time()
    r = Rose(Game())
    eval(r)
    end = time()
    print(end - start)

benchmark()
