class Base(object):
    def __init__(self):
        self.i = 10 
        self.j = 20

    def fun(self):
        print("Base Fun")

    def gun(self):
        print("Base gun")

class Dervied(Base):
    def __init__(self):
        self.i = 11 
        self.j = 21

    def fun(self):
        print("Dervied Fun")

    def sun(self):
        print("Dervied sun")

def main ():
    Bobj = Base()
    Dobj = Dervied()


if __name__=="__main__":
    main()