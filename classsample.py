class Hoge:
    def __init__(self):
        self.a = 10
        self.b = 20

    def printab(self):
        print("test {0} {1}".format(self.a,self.b))


class Fuga: pass


a = Hoge()
a.printab()
