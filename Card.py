from Bank import Bank

class Card:
     bank = Bank.Instance()

class DoctorFee(Card):
     def take_action(self, player ):
         player.cash -= 50
         Card.bank.cash += 50

class PayHospitalBill(Card):
    def take_action(self, player ):
        player.cash -= 100
        Card.bank.cash += 100


class PaySchoolTax(Card):
    def take_action(self, player ):
        player.cash -= 150
        Card.bank.cash += 150


class StockSale(Card):
    def take_action(self, player ):
        player.cash += 45
        Card.bank.cash -= 45

class StreetRepairs(Card):
    def take_action(self, player ):
        street_repairs_cost = ((40*player.total_number_of_houses_owned) + (115*player.total_number_of_hotels_owned))
        player.cash -= street_repairs_cost
        Card.bank.cash += street_repairs_cost

class LifeInsuranceMaturity(Card):
    def take_action(self, player ):
        player.cash += 100
        Card.bank.cash -= 100

class BeautyContest(Card):
    def take_action(self, player ):
        player.cash += 10
        Card.bank.cash -= 10

class YouInherit(Card):
    def take_action(self, player ):
        player.cash += 100
        Card.bank.cash -= 100

class ReceiveForServices(Card):
    def take_action(self, player ):
        player.cash += 25
        Card.bank.cash -= 25

class IncomeTaxRefund(Card):
    def take_action(self, player ):
        player.cash += 20
        Card.bank.cash -= 20

class XmasFund(Card):
    def take_action(self, player ):
        player.cash += 100
        Card.bank.cash -= 100

class BankError(Card):
    def take_action(self, player ):
        player.cash += 200
        Card.bank.cash -= 200

class GrandOperaOpening(Card):
    def __init__(self, players):
        self.players = players
    def take_action(self, player ):
        for p in self.players:
            if(p != player):
                p.cash -= 50
                player.cash += 50

class GoBack3Spaces(Card):
    def take_action(self, player ):
        player.sum_of_numbers_rolled_on_dice = -3
        player.move_and_take_action()

class AdvanceToIllinois(Card):
    def take_action(self, player ):
        if player.location_on_board == 36: # check the player's current location
            # the player has to pass through Go to advance to illinois ave. Hence he collects $200.
            player.cash += 200
            Card.bank.cash -= 200
            player.sum_of_numbers_rolled_on_dice = 28
            player.move_and_take_action()
        elif player.location_on_board == 7: # check the player's current location
            player.sum_of_numbers_rolled_on_dice = 17
            player.move_and_take_action()
        elif player.location_on_board == 22: # check the player's current location
            player.sum_of_numbers_rolled_on_dice = 2
            player.move_and_take_action()
        else:
            print("Cannot come here")

class AdvanceToBoardWalk(Card):
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
            print("Cannot come here")

class AdvanceToStCharlesPlace(Card):
    def take_action(self, player):
        if player.location_on_board == 36:  # check the player's current location
            # the player has to pass through Go to advance to St. Charles Place Hence he collects $200.
            player.cash += 200
            Card.bank.cash -= 200

            player.sum_of_numbers_rolled_on_dice = 15
            player.move_and_take_action()

        elif player.location_on_board == 7:  # check the player's current location
            player.sum_of_numbers_rolled_on_dice = 4
            player.move_and_take_action()

        elif player.location_on_board == 22:  # check the player's current location
            # the player has to pass through Go to advance to St. Charles Place Hence he collects $200.
            player.cash += 200
            Card.bank.cash -= 200

            player.sum_of_numbers_rolled_on_dice = 29
            player.move_and_take_action()
        else:
            print("Cannot come here")

class BuildingAndLoanMatures(Card):
    def take_action(self, player):
        player.cash += 200
        Card.bank.cash -= 200

class BankPaysYouADividend(Card):
    def take_action(self, player):
        player.cash += 50
        Card.bank.cash -= 50


class PayPoorTax(Card):
    def take_action(self, player):
        player.cash -= 15
        Card.bank.cash += 15


class GeneralRepairs(Card):
    def take_action(self, player):
        general_repairs_cost = ((25 * player.total_number_of_houses_owned) + (100 * player.total_number_of_hotels_owned))
        player.cash -= general_repairs_cost
        Card.bank.cash += general_repairs_cost
        return

class YouAreElectedBoardChairman(Card):
    def __init__(self, players):
        self.players = players

    def take_action(self, player): # pay each player $50
        for p in self.players:
            if (p != player):
                p.cash += 50
                player.cash -= 50
        return


class AdvanceToNearestUtility(Card):
    def take_action(self, player):
        # TODO If utility is already owned by some other player, pay rent = 10*(amount thrown on dice) to owner.
        if player.location_on_board == 36:  # check the player's current location
            # the player has to pass through Go to advance to St. Charles Place Hence he collects $200.
            player.cash += 200
            Card.bank.cash -= 200

            player.sum_of_numbers_rolled_on_dice = 16
            player.move_and_take_action()

        elif player.location_on_board == 7:  # check the player's current location
            player.sum_of_numbers_rolled_on_dice = 5
            player.move_and_take_action()

        elif player.location_on_board == 22:  # check the player's current location
            player.sum_of_numbers_rolled_on_dice = 6
            player.move_and_take_action()
        else:
            print("Cannot come here")

class AdvanceToNearestRailRoad(Card):
    def take_action(self, player):

        # TODO if railraod already owned, player pays twice the rent the owner is entitled to.
        if player.location_on_board == 36:  # check the player's current location
            # the player has to pass through Go to advance to St. Charles Place Hence he collects $200.
            player.cash += 200
            Card.bank.cash -= 200

            player.sum_of_numbers_rolled_on_dice = 9
            player.move_and_take_action()

        elif player.location_on_board == 7:  # check the player's current location
            player.sum_of_numbers_rolled_on_dice = 8
            player.move_and_take_action()

        elif player.location_on_board == 22:  # check the player's current location
            player.sum_of_numbers_rolled_on_dice = 3
            player.move_and_take_action()
        else:
            print("Cannot come here")

        return

class TakeARideOnReading(Card):
    def take_action(self, player):
        if player.location_on_board == 36:  # check the player's current location

            player.sum_of_numbers_rolled_on_dice = 9

        elif player.location_on_board == 7:  # check the player's current location
            player.sum_of_numbers_rolled_on_dice = 38

        elif player.location_on_board == 22:  # check the player's current location
            player.sum_of_numbers_rolled_on_dice = 23

        else:
            print("Cannot come here")

        # the player has to pass through Go to advance to Reading Railraod. Hence he collects $200
        player.cash += 200
        Card.bank.cash -= 200

        player.move_and_take_action()

        return

class AdvanceToGo(Card):
    def take_action(self, player):
          player.location_on_board = 0
          player.cash += 200
          Card.bank.cash -= 200
          return

class GetOutOfJailFree(Card):
    def take_action(self, player):
        player.get_out_of_jail_free_card = True
        return

class GoToJail(Card):

    def take_action(self, player):
        if player.location_on_board == 36:  # check the player's current location

            player.sum_of_numbers_rolled_on_dice = 14
            player.move_and_take_action()

        elif player.location_on_board == 7:  # check the player's current location
            player.sum_of_numbers_rolled_on_dice = 3
            player.move_and_take_action()

        elif player.location_on_board == 22:  # check the player's current location
            player.sum_of_numbers_rolled_on_dice = 28
            player.move_and_take_action()
        else:
            print("Cannot come here")












