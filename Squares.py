from  collections import deque
import random

class Square:
    def __init__(self, _pos, _title):
        self.location_of_square_on_board = _pos
        self.title = _title



class Property(Square):
    def __init__(self, _position,  _title, _price, _bank):
        Square.__init__(self, _position, _title)
        self.price = _price
        self.owner = None
        self.change_owner(_bank)
        self.bank = _bank

    def take_action(self, player):
        if self.owner == self.bank:
            player.cash -= self.price
            self.bank.cash += self.price
            self.change_owner(player)

    def change_owner(self, owner):
        if self.owner != None:
            self.owner.remove_property(self)
        self.owner = owner
        owner.add_property(self)

    def __str__(self):
        return self.title + ", " + str(self.owner)

    def __repr__(self):
        return self.title + ", " + str(self.owner)



class Land(Property):
    def __init__(self, _position,  _title, _price, _bank, _title_deed_info):
        Property.__init__(self,_position,  _title, _price, _bank)
        self.colorGroup, self.rent_of_unimproved_lot, self.rent_1_house, self.rent_2_houses, self.rent_3_houses, self.rent_4_houses, \
        self.hotel_rent, self.mortgage_value, self.cost_1_house, self.cost_1_hotel = _title_deed_info


class RailRoad(Property):
    def __init__(self, _position,  _title, _price, _bank, _title_deed_info):
        Property.__init__(self, _position,  _title, _price, _bank)
        self.rent_1_rr, self.rent_2_rr, self.rent_3_rr, self.rent_4_rr, self.mortgage_value = _title_deed_info


class Utility(Property):
    def __init__(self, _position,  _title, _price, _bank, _title_deed_info):
        Property.__init__(self, _position, _title, _price, _bank)
        self.rent_1_uc, self.rent_2_uc = _title_deed_info






class Go(Square):
    def __init__(self, _position, _title):
        Square.__init__(self, _position, _title)

    def take_action(self, player):
        player.cash += 200
        self.bank.cash -= 200

        # to do
        # implement a method to give each player $200 as they pass Go



class Tax(Square):
    def __init__(self, _position, _title, tax):
        Square.__init__(self, _position, _title)
        self.tax = tax

    def take_action(self, player):
        player.cash -= self.tax
        self.bank.cash += self.tax

class Jail(Square):
    def __init__(self, _position, _title, fine):
        Square.__init__(self, _position, _title)
        self.fine  = fine

    # to do
    def take_action(self, player):
        player.cash -= self.fine
        self.bank.cash += self.fine
    # find out if player is "Just Visiting" or "sent to jail".
    # if   "sent to jail" do something

class GoToJail(Square):
    def __init__(self, _position, _title, jail):
        Square.__init__(self, _position, _title)
        self.jail = jail

    def take_action(self, player):
        player.location_on_board = self.jail.location_of_square_on_board
        self.jail.take_action(player)

    # to do
    # implement "sending the player to jail" method

class CommunityChest(Square):
    def __init__(self, _position, _title):
        Square.__init__(self, _position, _title)

    def take_action(self, player):
        cc_card_drawn = self.community_chest_card_deck.popleft()
        self.community_chest_card_deck.append(cc_card_drawn)


class Chance(Square):
    def __init__(self, _position, _title):
        Square.__init__(self, _position, _title)

    def take_action(self, player):
        cc_card_drawn = self.chance_card_deck.popleft()
        self.chance_card_deck.append(cc_card_drawn)


