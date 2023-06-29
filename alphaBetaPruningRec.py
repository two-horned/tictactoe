# C: Said Kadrioski <said@kadrioski.de>

from time import time
from game import Game
from copy import deepcopy

class Evaluater:
    def __init__(self) -> None:
        self.forbidden: dict[str, Game] = dict()

    def minmax(self, player: int, game_list: list[Game]) -> Game:
        n = self.eval(game_list[0])
        if n.whowon() == player:
            return n
        if player > 0:
            for i in game_list[1:]:
                i = self.eval(i)
                if i.whowon() == 1:
                    return i
                if i.whowon() > n.whowon():
                    n = i
        else:
            for i in game_list[1:]:
                i = self.eval(i)
                if i.whowon() == -1:
                    return i
                if i.whowon() < n.whowon():
                    n = i
        return n

    def eval(self, game: Game):
        s: list[int] = game.symmshowfree()
        h = mkstr(game.history)
        if h in self.forbidden:
            n = self.forbidden[h]
            game.board = n.board
            game.history += n.history[len(game.history):]
            return game
        if s != []:
            l: list[Game] = []
            for i in s:
                g = deepcopy(game)
                g.choose(i)
                if g.whowon() != 0:
                    return g
                l.append(g)
            game = self.minmax(game.player(), l)
        self.forbidden.update({h : game })
        return game

def mkstr(history: list[int]):
    return str(sorted(history))



def benchmark():
    g = Game()
    e = Evaluater();
    start = time()
    g = e.eval(g)
    end = time()
    return (g,end - start)

def test():
    print("World's fastest recursive tic tac toe solver")
    print("Look how much time it needed to solve the whole game tree:")
    b = benchmark()
    print("time needed: {}".format(b[1]))
    print("best path: {}".format(b[0].history))

if __name__ == "__main__":
    test()
