class Animals:

    age = None
    weight = None

    def __init__(self, *args, **kwargs):
        if len(args) != 0:
            self.age = args[0]
            self.weight = args[1]

    def search_food(self):
        print('start search')

    def eat(self, value):
        print('start eat')
        self.fill += value

    def sleep(self):
        print('start sleep')

# -------------------------------------------------


class Duck(Animals):
    pass


duck = Duck(5, 30)
print(duck.__dict__)


class Chicken(Animals):
    pass


class Geese(Animals):
    pass


class Cow(Animals):
    pass


class Goat(Animals):
    pass


class Sheep(Animals):
    pass


class Pig(Animals):
    pass
