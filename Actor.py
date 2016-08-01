from util import *

class Actor:
    def __init__(self, cash, name):
        self.cash = cash
        self.properties = []
        self.name = name

    def add_property(self, property):
        self.properties.append(property)

    def remove_property(self, property):
        self.properties.remove(property)

    def pay_cash(self, receiver, amount):
        if (self.cash < amount):
            raise ValueError('Do not have cash to pay', self.name, receiver.name)
        self.cash -= amount
        receiver.cash += amount
        printmessage(str(self.name) + " pays $" + str(amount) + " to " +str(receiver.name))

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

