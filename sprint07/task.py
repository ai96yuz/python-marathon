#       TASK 1
#       TASK 2
#       TASK 3
#       TASK 4


class Washing:
    def wash(self):
        print("Washing...")


class Rinsing:
    def rinse(self):
        print("Rinsing...")


class Spinning:
    def spin(self):
        print("Spinning...")


class WashingMachine:
    def __init__(self):
        self.washing = Washing()
        self.rinsing = Rinsing()
        self.spinning = Spinning()

    def startWashing(self):
        self.washing.wash()
        self.rinsing.rinse()
        self.spinning.spin()


""" main method """
if __name__ == "__main__":
    washingMachine = WashingMachine()
    washingMachine.startWashing()


#       TASK 5


class LeafElement:
    def __init__(self, *args):
        self.position = args[0]

    def showDetails(self):
        print("\t", end="")
        print(self.position)


class CompositeElement:
    def __init__(self, *args):
        self.position = args[0]
        self.children = []

    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)

    def showDetails(self):
        print(self.position)
        for child in self.children:
            print("\t", end="")
            child.showDetails()
