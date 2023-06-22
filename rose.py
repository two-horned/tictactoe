# C: Said Kadrioski <said@kadrioski.de>

class Rose:
    def __init__(self,data, father:'Rose|None' = None):
        self.father               = father
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

    def mkchild(self,child: 'Rose'):
        child.father = self
        self.children.append(child)

    def mkfather(self,father: 'Rose'):
        father.mkchild(self)

    def __str__(self):
        s = str(self.data)
        for i in self.children:
            s += '\n' + '⎣⎯⎯⎯⎯⎯⎯ ' + '\t'.join(str(i).splitlines(True))
        return s
