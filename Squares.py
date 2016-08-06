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
                player.pay_cash(Square.bank, self.price)
                self.change_owner(player)


    def change_owner(self, _owner):
        if self.owner != None:
            self.owner.remove_property(self)
        self.owner = _owner
        _owner.add_property(self)

    def __str__(self):
        return self.title

    def __repr__(self):
        return  self.title


class Land(Property):
    def __init__(self, _position,  _title, _price, _title_deed_info):
        Property.__init__(self,_position,  _title, _price)
        self.colorGroup, self.rent_of_unimproved_lot, self.rent_1_house, self.rent_2_houses, self.rent_3_houses, self.rent_4_houses, \
        self.hotel_rent, self.mortgage_value, self.cost_1_house, self.cost_1_hotel = _title_deed_info

    def take_action(self, player):
        if self.owner == Square.bank:
            Property.buy_property(self, player)
        elif self.owner != player:

            # To determine rent, check if owner owns other properties in the same color group.
            number_of_lots_owner_has_in_same_color_grp = 0
            for p in self.owner.properties:
                # A player may own Land, Railroad or utility companies.
                # Color groups exist only for Land type of properties.
                if type(p) is Land:
                    if p.colorGroup == self.colorGroup:
                        number_of_lots_owner_has_in_same_color_grp += 1

            if (number_of_lots_owner_has_in_same_color_grp == 2 and p.colorGroup in ["Purple", "Dark Blue"]) or \
                    number_of_lots_owner_has_in_same_color_grp == 3:
                rent = self.rent_of_unimproved_lot * 2
            else:
                rent = self.rent_of_unimproved_lot

            printmessage("Pays rent to owner.")
            player.pay_cash(self.owner, rent)

class RailRoad(Property):
    def __init__(self, _position,  _title, _price,  _title_deed_info):
        Property.__init__(self, _position,  _title, _price)
        self.rr_base_rent,  self.mortgage_value = _title_deed_info


    def take_action(self, player):
        if self.owner == Square.bank:
            Property.buy_property(self, player)
        elif self.owner != player:
            # To determine rent, check how many rail road companies owner owns.
            number_of_rr_owner_has = 0
            for p in self.owner.properties:
                if type(p) is RailRoad:
                    number_of_rr_owner_has += 1
            rent = number_of_rr_owner_has * self.rr_base_rent
            printmessage("Pays rent to owner.")
            player.pay_cash( self.owner, rent)

class Utility(Property):
    def __init__(self, _position,  _title, _price,  _title_deed_info):
        Property.__init__(self, _position, _title, _price)
        self.rent_1_uc_factor, self.rent_2_uc_factor, self.mortgage_value = _title_deed_info


    def take_action(self, player):
        if self.owner == Square.bank:
            Property.buy_property(self, player)
        elif self.owner != player:
            # pay rent to owner
            # To determine rent, check how many utility companies owner owns.
            number_of_uc_owner_has = 0
            for p in self.owner.properties:
                if type(p) is Utility:
                    number_of_uc_owner_has += 1

            if  number_of_uc_owner_has == 1:
                rent = self.rent_1_uc_factor * player.sum_of_numbers_rolled_on_dice

            elif number_of_uc_owner_has == 2:
                rent = self.rent_2_uc_factor *  player.sum_of_numbers_rolled_on_dice

            printmessage("Pays rent to owner.")
            player.pay_cash(self.owner, rent)



class Go(Square):
    def __init__(self, _position, _title):
        Square.__init__(self, _position, _title)

    def take_action(self, player):
        pass


class Tax(Square):
    def __init__(self, _position, _title, tax):
        Square.__init__(self, _position, _title)
        self.tax = tax


    def take_action(self, player):
        player.pay_cash(Square.bank, self.tax)

class Jail(Square):
    def __init__(self, _position, _title, fine):
        Square.__init__(self, _position, _title)
        self.fine  = fine


    # to do
    def take_action(self, player):
        if player.just_visiting_jail:
            pass
        else:
            # player is sent to jail. He will pay fine to get out.
            printmessage("Player has to pay fine. " )
            player.pay_cash(Square.bank, self.fine)
            player.just_visiting_jail = True # player has paid fine. Hence he can get out of jail.


class GoToJailSquare(Square):
    def __init__(self, _position, _title, jail):
        Square.__init__(self, _position, _title)
        self.jail = jail

    def take_action(self, player):
        player.just_visiting_jail = False
        player.sum_of_numbers_rolled_on_dice = 20
        player.move_and_take_action()



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