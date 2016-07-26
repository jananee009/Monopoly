import math
import collections
from Actor import Actor



class Bank(Actor):
    def __init__(self, cash):
        Actor.__init__(self, cash, "Bank")
        self.realestate_houses = 32
        self.realestate_hotels = 12
