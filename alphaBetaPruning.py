# C: Said Kadrioski <said@kadrioski.de>

from game import Game
from rose import Rose
from copy import deepcopy

def decide(rose: Rose) -> Game:
    eval(rose)
    print(rose.data.history)
    return rose.leaves()[0].data

def prune(q: list[Rose]):
    while q != []:
        r = q.pop()
        if r.data.history == [1,-9]:
            print(list(map(dddd,r.children)))
        if r.children != []:
            n = r.children[0]
            if r.data.player() == 1:
                for i in r.children:
                    if n.data.whowon() < i.data.whowon():
                        n = i
            else:
                for i in r.children:
                    if i.data.whowon() < n.data.whowon():
                        n = i
            for i in r.children:
                i.father.remove(r)
            r.data = n.data
            r.children = []
        for p in r.father:
            b = True
            for i in p.children:
                b = b and i.data.finished()
            if b:
                q.append(p)

def eval(rose: Rose):
    q: list[Rose] = [rose]
    f: dict[str, Rose] = {}
    c: list[Rose] = []
    while q != []:
        t: list[Rose] = []
        r = q.pop()
        h = deepcopy(r.data.history)
        h.sort()
        if True or str(h) not in f:
            f.update({str(h): r})
            s = r.data.showfree()
            for i in s:
                g = deepcopy(r.data)
                g.choose(i)
                if g.finished():
                    r.data     = g
                    r.children = []
                    t = []
                    break
                else:
                    n = Rose(g)
                    t.append(n)
            for n in t:
                n.father.append(r)
                r.children.append(n)
            q+=t
        else:
            n = f.get(str(h))
            if n != None:
                for p in r.father:
                    p.children.remove(r)
                    p.children.append(n)
                    if p not in n.father:
                        n.father.append(p)
                r = n
        if r.data.finished():
            for p in r.father:
                b = True
                for i in p.children:
                    b = b and i.data.finished()
                if b:
                    c.append(p)
        prune(c)

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

#r = Rose(Game([-4], [[1,1,0], [-1,-1,0], [0,0,0]]))
r = Rose(Game())
#print(r.data)
eval(r)
l = r.leaves()
print(list(map(dddd,l)))
print(list(map(wwww,l)))
#print(list(map(ffff,l)))
#print(list(map(fdfd,l)))
#print(r.data)
