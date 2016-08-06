from Bank import Bank
from util import *

class Card:
     bank = Bank.Instance()

class DoctorFee(Card):
     def take_action(self, player ):
         doctorFee = 50
         player.pay_cash(Card.bank, doctorFee)


class PayHospitalBill(Card):
    def take_action(self, player ):
        hospitalBill = 100
        player.pay_cash(Card.bank, hospitalBill )


class PaySchoolTax(Card):
    def take_action(self, player ):
        schoolTax = 150
        player.pay_cash(Card.bank,schoolTax )


class StockSale(Card):
    def take_action(self, player ):
        stockSale  =45
        Card.bank.pay_cash(player,stockSale )


class StreetRepairs(Card):
    def take_action(self, player ):
        street_repairs_cost = ((40*player.total_number_of_houses_owned) + (115*player.total_number_of_hotels_owned))
        player.pay_cash(Card.bank, street_repairs_cost)

class LifeInsuranceMaturity(Card):
    def take_action(self, player ):
        LifeInsuranceAmt = 100
        Card.bank.pay_cash(player, LifeInsuranceAmt)

class BeautyContest(Card):
    def take_action(self, player ):
        beautyContestPrize = 10
        Card.bank.pay_cash(player, beautyContestPrize)


class YouInherit(Card):
    def take_action(self, player ):
        inheritance = 100
        Card.bank.pay_cash(player, inheritance)


class ReceiveForServices(Card):
    def take_action(self, player ):
        salary = 25
        Card.bank.pay_cash(player, salary)


class IncomeTaxRefund(Card):
    def take_action(self, player ):
        taxRefund = 20
        Card.bank.pay_cash(player, taxRefund)


class XmasFund(Card):
    def take_action(self, player ):
        xmasFund = 100
        Card.bank.pay_cash(player, xmasFund)


class BankError(Card):
    def take_action(self, player ):
        bankError = 200
        Card.bank.pay_cash(player, bankError)


class GrandOperaOpening(Card):
    def __init__(self, players):
        self.players = players
    def take_action(self, player ):
        opera_ticket_cost = 50
        for p in self.players:
            if(p != player):
                p.pay_cash(player,opera_ticket_cost )


class GoBack3Spaces(Card): # This is a chance card.
    def take_action(self, player ):
        player.sum_of_numbers_rolled_on_dice = -3
        player.move_and_take_action()

class AdvanceToIllinois(Card): # This is a chance card.
    def take_action(self, player ):
        if player.location_on_board == 36: # check the player's current location
            #salary = 200 # the player has to pass through Go to advance to illinois ave. Hence he collects $200.
            #Card.bank.pay_cash(player,salary)
            player.sum_of_numbers_rolled_on_dice = 28
            player.move_and_take_action()

        elif player.location_on_board == 7: # check the player's current location
            player.sum_of_numbers_rolled_on_dice = 17
            player.move_and_take_action()

        elif player.location_on_board == 22: # check the player's current location
            player.sum_of_numbers_rolled_on_dice = 2
            player.move_and_take_action()

        else:
            printmessage("Cannot come here")

class AdvanceToBoardWalk(Card): # This is a chance card.
    def take_action(self, player):
        if player.location_on_board == 36:  # check the player's current location
            player.sum_of_numbers_rolled_on_dice =3
            player.move_and_take_action()

        elif player.location_on_board == 7:  # check the player's current location
            player.sum_of_numbers_rolled_on_dice = 32
            player.move_and_take_action()

        elif player.location_on_board == 22:  # check the player's current location
            player.sum_of_numbers_rolled_on_dice = 17
            player.move_and_take_action()
        else:
            printmessage("Cannot come here")

class AdvanceToStCharlesPlace(Card):
    def take_action(self, player):
        if player.location_on_board == 36:  # check the player's current location
            #salary = 200  # the player has to pass through Go to advance to St. Charles Place Hence he collects $200.
            #Card.bank.pay_cash(player, salary)
            player.sum_of_numbers_rolled_on_dice = 15
            player.move_and_take_action()

        elif player.location_on_board == 7:  # check the player's current location
            player.sum_of_numbers_rolled_on_dice = 4
            player.move_and_take_action()

        elif player.location_on_board == 22:  # check the player's current location
            # the player has to pass through Go to advance to St. Charles Place Hence he collects $200.
            salary = 200
            Card.bank.pay_cash(player, salary)
            player.sum_of_numbers_rolled_on_dice = 29
            player.move_and_take_action()
        else:
            printmessage("Cannot come here")

class BuildingAndLoanMatures(Card):
    def take_action(self, player):
        buildingLoanMaturityAmt = 200
        Card.bank.pay_cash(player, buildingLoanMaturityAmt)

class BankPaysYouADividend(Card):
    def take_action(self, player):
        bankDividend = 50
        Card.bank.pay_cash(player, bankDividend)


class PayPoorTax(Card):
    def take_action(self, player):
        poorTax = 15
        player.pay_cash(Card.bank, poorTax)



class GeneralRepairs(Card):
    def take_action(self, player):
        general_repairs_cost = ((25 * player.total_number_of_houses_owned) + (100 * player.total_number_of_hotels_owned))
        player.pay_cash(Card.bank, general_repairs_cost)

class YouAreElectedBoardChairman(Card):
    def __init__(self, players):
        self.players = players

    def take_action(self, player): # pay each player $50
        treat = 50
        for p in self.players:
            if (p != player):
                player.pay_cash(p, treat)
        return


class AdvanceToNearestUtility(Card): # This is a chance card.
    def take_action(self, player):
        # TODO If utility is already owned by some other player, pay rent = 10*(amount thrown on dice) to owner.
        if player.location_on_board == 36:  # check the player's current location.
            #salary = 200 # the player has to pass through Go to advance to St. Charles Place Hence he collects $200.
            #Card.bank.pay_cash(player, salary)
            player.sum_of_numbers_rolled_on_dice = 16
            player.move_and_take_action()

        elif player.location_on_board == 7:  # check the player's current location
            player.sum_of_numbers_rolled_on_dice = 5
            player.move_and_take_action()

        elif player.location_on_board == 22:  # check the player's current location
            player.sum_of_numbers_rolled_on_dice = 6
            player.move_and_take_action()
        else:
            printmessage("Cannot come here")

class AdvanceToNearestRailRoad(Card):
    def take_action(self, player):

        # TODO if railraod already owned, player pays twice the rent the owner is entitled to.
        if player.location_on_board == 36:  # check the player's current location
            #salary = 200 # the player has to pass through Go to advance to St. Charles Place Hence he collects $200.
            #Card.bank.pay_cash(player, salary)
            player.sum_of_numbers_rolled_on_dice = 9
            player.move_and_take_action()

        elif player.location_on_board == 7:  # check the player's current location
            player.sum_of_numbers_rolled_on_dice = 8
            player.move_and_take_action()

        elif player.location_on_board == 22:  # check the player's current location
            player.sum_of_numbers_rolled_on_dice = 3
            player.move_and_take_action()
        else:
            printmessage("Cannot come here")

        return

class TakeARideOnReading(Card): # This is a chance card.
    def take_action(self, player):
        if player.location_on_board == 36:  # check the player's current location
            player.sum_of_numbers_rolled_on_dice = 9

        elif player.location_on_board == 7:  # check the player's current location
            player.sum_of_numbers_rolled_on_dice = 38

        elif player.location_on_board == 22:  # check the player's current location
            player.sum_of_numbers_rolled_on_dice = 23

        else:
            printmessage("Cannot come here")

        # the player has to pass through Go to advance to Reading Railraod. Hence he collects $200
        #salary = 200
        #Card.bank.pay_cash(player, salary)

        player.move_and_take_action()

        return

class AdvanceToGo(Card): # This card belongs to both Chance and Community Chest.
    def take_action(self, player):
          if player.location_on_board == 36:  #  Location# 36 is a Chance Square.
              player.sum_of_numbers_rolled_on_dice = 4
              player.move_and_take_action()

          elif player.location_on_board == 7:  #  Location# 7 is a Chance Square.
              player.sum_of_numbers_rolled_on_dice = 33
              player.move_and_take_action()

          elif player.location_on_board == 22:  # Location# 22 is a Chance Square.
              player.sum_of_numbers_rolled_on_dice = 18
              player.move_and_take_action()

          elif player.location_on_board == 2:  #  Location# 2 is a Community Chest Square.
              player.sum_of_numbers_rolled_on_dice = 38
              #player.collectSalary = False
              #player.just_visiting_jail = False
              player.move_and_take_action()

          elif player.location_on_board == 17:  #  Location# 17 is a Community Chest Square.
              player.sum_of_numbers_rolled_on_dice = 23
              player.move_and_take_action()

          elif player.location_on_board == 33:  #  Location# 33 is a Community Chest Square.
              player.sum_of_numbers_rolled_on_dice = 7
              player.move_and_take_action()

          else:
              printmessage("Cannot come here")

class GetOutOfJailFree(Card): # This card belongs to both Chance and Community Chest.
    def take_action(self, player):
        player.get_out_of_jail_free_card = True
        return

class GoToJail(Card): # This card belongs to both Chance and Community Chest.

    def take_action(self, player):
        if player.location_on_board == 36:  # check the player's current location. Location# 36 is a Chance Square.

            player.sum_of_numbers_rolled_on_dice = 14
            player.collectSalary = False
            player.just_visiting_jail = False
            player.move_and_take_action()

        elif player.location_on_board == 7:  # check the player's current location. Location# 7 is a Chance Square.
            player.sum_of_numbers_rolled_on_dice = 3
            player.just_visiting_jail = False
            player.move_and_take_action()

        elif player.location_on_board == 22:  # check the player's current location. Location# 22 is a Chance Square.
            player.sum_of_numbers_rolled_on_dice = 28
            player.collectSalary = False
            player.just_visiting_jail = False
            player.move_and_take_action()

        elif player.location_on_board == 2:  # Player is on Community Chest Square. Location# 2 is a Community Chest Square.
            player.sum_of_numbers_rolled_on_dice = 8
            player.collectSalary = False
            player.just_visiting_jail = False
            player.move_and_take_action()

        elif player.location_on_board == 17:  # Player is on Community Chest Square. Location# 17 is a Community Chest Square.
            player.sum_of_numbers_rolled_on_dice = 33
            player.collectSalary = False
            player.just_visiting_jail = False
            player.move_and_take_action()

        elif player.location_on_board == 33:  # Player is on Community Chest Square. Location# 33 is a Community Chest Square.
            player.sum_of_numbers_rolled_on_dice = 17
            player.collectSalary = False
            player.just_visiting_jail = False
            player.move_and_take_action()

        else:
            printmessage("Cannot come here")












