class Actor:
    def __init__(self, cash, name):
        self.cash = cash
        self.properties = []
        self.name = name

    def add_property(self, property):
        self.properties.append(property)

    def remove_property(self, property):
        self.properties.remove(property)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

