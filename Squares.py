from  collections import deque
import random
from Bank import Bank
from util import *

class Square:
    bank = Bank.Instance()
    def __init__(self, _pos, _title):
        self.location_of_square_on_board = _pos
        self.title = _title





class Property(Square):

    def __init__(self, _position,  _title, _price):
        Square.__init__(self, _position, _title)
        self.price = _price # assign the price to the property
        self.owner = None
        self.change_owner(Square.bank) # assign bank as the initial owner of the property


    def buy_property(self, player):
        if self.owner == Square.bank:
            if(player.cash >= self.price):
                printmessage("Buys " + self.title)
                player.cash -= self.price
                Square.bank.cash += self.price
                self.change_owner(player)


    def change_owner(self, _owner):
        if self.owner != None:
            self.owner.remove_property(self)
        self.owner = _owner
        _owner.add_property(self)

    def __str__(self):
        #return self.title + ", " + str(self.owner)
        return self.title

    def __repr__(self):
        #return self.title + ", " + str(self.owner)
        return  self.title

def move_cash(giver, receiver, cash):
    giver.cash -= cash
    receiver.cash += cash

class Land(Property):
    def __init__(self, _position,  _title, _price, _title_deed_info):
        Property.__init__(self,_position,  _title, _price)
        self.colorGroup, self.rent_of_unimproved_lot, self.rent_1_house, self.rent_2_houses, self.rent_3_houses, self.rent_4_houses, \
        self.hotel_rent, self.mortgage_value, self.cost_1_house, self.cost_1_hotel = _title_deed_info

    def take_action(self, player):
        if self.owner == Square.bank:
            Property.buy_property(self, player)
        elif self.owner != player:
            move_cash(player, self.owner, self.rent_of_unimproved_lot)

class RailRoad(Property):
    def __init__(self, _position,  _title, _price,  _title_deed_info):
        Property.__init__(self, _position,  _title, _price)
        self.rent_1_rr, self.rent_2_rr, self.rent_3_rr, self.rent_4_rr, self.mortgage_value = _title_deed_info


    def take_action(self, player):
        if self.owner == Square.bank:
            Property.buy_property(self, player)
        elif self.owner != player:
            move_cash(player, self.owner, self.rent_1_rr)

class Utility(Property):
    def __init__(self, _position,  _title, _price,  _title_deed_info):
        Property.__init__(self, _position, _title, _price)
        self.rent_1_uc, self.rent_2_uc = _title_deed_info


    def take_action(self, player):
        if self.owner == Square.bank:
            Property.buy_property(self, player)
        elif self.owner != player:
            move_cash(player, self.owner, self.rent_1_uc)


class Go(Square):
    def __init__(self, _position, _title):
        Square.__init__(self, _position, _title)

    def take_action(self, player):
        player.cash += 200
        Square.bank.cash -= 200


class Tax(Square):
    def __init__(self, _position, _title, tax):
        Square.__init__(self, _position, _title)
        self.tax = tax
        #self.bank = _bank

    def take_action(self, player):
        player.cash -= self.tax
        Square.bank.cash += self.tax

class Jail(Square):
    def __init__(self, _position, _title, fine):
        Square.__init__(self, _position, _title)
        self.fine  = fine
        #self.bank = _bank

    # to do
    def take_action(self, player):
        if player.just_visiting_jail:
            pass
        else:
            # player is sent to jail. He will pay fine to get out.
            player.cash -= self.fine
            Square.bank.cash += self.fine
            player.just_visiting_jail = True
    # find out if player is "Just Visiting" or "sent to jail".
    # if   "sent to jail" do something

class GoToJailSquare(Square):
    def __init__(self, _position, _title, jail):
        Square.__init__(self, _position, _title)
        self.jail = jail

    def take_action(self, player):
        player.just_visiting_jail = False
        player.location_on_board = self.jail.location_of_square_on_board
        self.jail.take_action(player)

    # to do
    # implement "sending the player to jail" method

class CommunityChest(Square):
    def __init__(self, _position, _title, community_chest_card_deck):
        Square.__init__(self, _position, _title)
        self.community_chest_card_deck = community_chest_card_deck

    def take_action(self, player):
        card_drawn = self.community_chest_card_deck.popleft()  # player draws a card from the top of the deck
        printmessage("Community Chest Card drawn is: " + card_drawn.__class__.__name__)
        card_drawn.take_action(player)
        self.community_chest_card_deck.append(card_drawn)

class Chance(Square):
    def __init__(self, _position, _title, chance_card_deck):
        Square.__init__(self, _position, _title)
        self.chance_card_deck = chance_card_deck

    def take_action(self, player):
        card_drawn = self.chance_card_deck.popleft()
        printmessage("Chance Card drawn is: " + card_drawn.__class__.__name__)
        card_drawn.take_action(player)
        self.chance_card_deck.append(card_drawn)


class FreeParking(Square):
    def __init__(self, _position, _title):
        Square.__init__(self, _position, _title)

    def take_action(self, player):
       pass
       # Player does nothing if he lands at Free Parking Square