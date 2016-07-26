import math
import collections

class Singleton:
     def __init__(self, decorated):
         self._decorated = decorated


     def  Instance(self):
         try:
              return self._instance
         except AttributeError:
             self._instance = self._decorated()
             return self._instance

     def __call__(self):
         raise TypeError('Singletons must be accessed through Instance().')


     def __instancecheck__(self, inst):
         return isinstance(inst, self._decorated)





@Singleton
class Bank:
    def __init__(self):
        self.cash = 16550
        self.properties = []
        self.realestate_houses = 32
        self.realestate_hotels = 12
        self.title = "The Bank"

    def add_property(self, property):
        self.properties.append(property)

    def remove_property(self, property):
        self.properties.remove(property)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title