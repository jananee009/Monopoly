
import random
from Actor import Actor


class Player(Actor):
    def __init__(self, name, cash):
        Actor.__init__(self, cash, name)
        self.location_on_board = 0
        self.sum_of_numbers_rolled_on_dice = 0
        self.consecutive_doubles_counter = 0
        self.list_of_numbers_rolled = []
        self.locations_visited_by_player = []
        self.just_visiting_jail = True
        self.get_out_of_jail_free_card = False # player does not have the "get out of jail free" card.
        self.total_number_of_houses_owned = 0 # Initially player owns 0 houses
        self.total_number_of_hotels_owned = 0 # Initially player owns 0 hotels
        self.game_board = None

    def roll_dice(self):
        dice1 = random.randint(1, 6)  # roll 2 six-sided dice.
        dice2 = random.randint(1, 6)

        self.sum_of_numbers_rolled_on_dice = dice1 + dice2  # sum of the numbers rolled on both dice.
        self.list_of_numbers_rolled.append(self.sum_of_numbers_rolled_on_dice)


        if dice1 == dice2:
            self.consecutive_doubles_counter += 1


        elif ( (dice1 != dice2)    or   self.consecutive_doubles_counter < 3):
            self.consecutive_doubles_counter = 0 #reset the number of times player rolled a double.


    def play(self):

        self.roll_dice()

        self.move_and_take_action()

    def move_and_take_action(self):

        self.move()

        self.take_action()

    def move (self):


        if self.consecutive_doubles_counter == 3:  # check if player rolled doubles 3 times in a row
            self.location_on_board = 10  # player goes to jail.
            self.consecutive_doubles_counter = 0  # reset the number of times player rolled a double.
            self.just_visiting_jail = False



        else:
            self.location_on_board += self.sum_of_numbers_rolled_on_dice
            if self.location_on_board > 39:
                self.location_on_board = self.location_on_board - 40



        self.locations_visited_by_player.append(self.location_on_board)



    def take_action(self):
        take_another_turn = False

        square = self.game_board.get_square(self.location_on_board)

        square.take_action(self)
        # if 0 < number_of_doubles < 3:
        #     take_another_turn = True
        #
        # if location in game_board.chance_squares:
        #     # do something
        #     return
        #
        # if location in game_board.community_chest_squares:
        #     game_board.drawACommunityChestCard()
        #
        #     return
        #
        # if location == 10 and not self.just_visiting_jail: # player is currently in jail and he is not "just visiting".
        #     # get out of jail by rolling consecutive doubles.
        #     # get out of jail by using "get out of jail free" card.
        #     # pay a fine of $50 before you roll
        #
        # if 0 < number_of_doubles < 3 :
        #     take_another_turn = True


        return  ( take_another_turn, )
