# C: Said Kadrioski <said@kadrioski.de>

class Rose:
    def __init__(self,data):
        self.father: None|Rose    = None
        self.data                 = data
        self.children: list[Rose] = []

    def leaves(self):
        l: list[Rose] = []
        q: list[Rose] = [self]
        while q != []:
            i = q.pop()
            if i.children == []:
                l.append(i)
            for j in i.children:
                q.append(j)
        return l

    def __str__(self):
        s = str(self.data)
        s += '\n' + '----|' + '\t'
        for i in self.children:
            s += str(i) + '\t' + '--|--'
        return s
