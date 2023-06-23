# C: Said Kadrioski <said@kadrioski.de>

class Game:
    def __init__(self,history=[],board=[[0 for _ in range(3)] for _ in range(3)]):
        self.history: list[int]     = history
        self.board: list[list[int]] = board

    def player(self):
        if self.history == []:
            return 1
        return (self.history[-1]//abs(self.history[-1]) * -1)

    def choose(self, index: int):
        p = self.player()
        index = index - 1
        if index > -1 and index < 9:
            f = self.board[index//3][index%3]
            if f == 0:
                self.board[index//3][index%3] = p
                self.history.append(p * (index+1))
                return True
        return False

    def showfree(self) -> list[int]:
        l = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    l.append(i*3+j+1)
        return l

    def finished(self):
        return abs(self.whowon()) == 1 or len(self.showfree()) == 0

    def symmshowfree(self):
        w = self.board
        s = set(self.showfree())
        b = True
        if w[0] == w[2]:
            s -= {7,8,9}
            if len(s) < 2:
                return list(s)
        for i in range(3):
            b = b and w[i][0] == w[i][2]
        if b:
            s -= {3,6,9}
            if len(s) < 2:
                return list(s)
        if w[0][1] == w[1][0] and w[1][2] == w[2][1] and w[0][2] == w[2][0]:
            s -= {4,7,8}
            if len(s) < 2:
                return list(s)
        if w[0][1] == w[1][2] and w[1][0] == w[2][1] and w[0][0] == w[2][2]:
            if len(s - {1,2,4}) == 0:
                return list(s)
            s -= {1,2,4}
        return list(s)

    def whowon(self):
        b = self.board
        for i in b:
            s = sum(i)
            if abs(s) == 3:
                return s//3
        for i in range(3):
            s = 0
            for j in b:
                s += j[i]
            if abs(s) == 3:
                return s//3
        a = b[1][1]
        if b[0][0] + b[2][2] == 2*a or b[0][2] + b[2][0] == 2*a:
            return a
        return 0

    def __str__(self):
        s = ""
        for i in self.board:
            m = list(map(ftos, i))
            for j in m:
                s+= j
            s+='\n'
        return s

    def end_msg(self):
        print("Game finished winner is player {}".format(self.whowon()))
        print(self)


def ftos(field):
    match field:
        case 1:
            return "X"
        case -1:
            return "O"
    return "."

def reproduce(history):
    g = Game()
    for i in history:
        g.choose(i)
    return g
