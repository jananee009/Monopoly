
import random
from Actor import Actor
from Bank import Bank
from util import *

class Player(Actor):
    def __init__(self, name, cash):
        Actor.__init__(self, cash, name)
        self.location_on_board = 0
        self.sum_of_numbers_rolled_on_dice = 0
        self.consecutive_doubles_counter = 0
        self.list_of_numbers_rolled = []
        self.locations_visited_by_player = []
        self.just_visiting_jail = True
        self.get_out_of_jail_free_card = False # Initially, player does not have the "get out of jail free" card.
        self.total_number_of_houses_owned = 0 # Initially player owns 0 houses
        self.total_number_of_hotels_owned = 0 # Initially player owns 0 hotels
        self.game_board = None
        self.collectSalary = False
        self.bank =  Bank.Instance()
        self.playAnotherTurn = False

    def get_dice_value_interactively(self, mes):
        val = 100
        while(val < 1 or val > 6):
            val = int(input(mes))
        return val

    def roll_dice(self):
        interactive = True
        if(interactive):
            dice1 = self.get_dice_value_interactively('Enter the first dice roll:')
            dice2 = self.get_dice_value_interactively('Enter the second dice roll:')
        else:
            dice1, dice2 = self.set_dice_roll()
        self.sum_of_numbers_rolled_on_dice = dice1 + dice2  # sum of the numbers rolled on both dice.
        self.list_of_numbers_rolled.append(self.sum_of_numbers_rolled_on_dice)


        printmessage("Number rolled on dice1: " + str(dice1))
        printmessage("Number rolled on dice2: " + str(dice2))
        printmessage("Number rolled: " + str(self.sum_of_numbers_rolled_on_dice))


        if dice1 == dice2:
            self.consecutive_doubles_counter += 1
            self.playAnotherTurn = True


        elif ( (dice1 != dice2)    or   self.consecutive_doubles_counter < 3):
            self.consecutive_doubles_counter = 0 #reset the number of times player rolled a double.
            self.playAnotherTurn = False

    def set_dice_roll(self):
        dice1 = random.randint(1, 6)  # roll 2 six-sided dice.
        dice2 = random.randint(1, 6)
        return (dice1, dice2)

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
            self.just_visiting_jail = False # player is not "just visiting".
            self.playAnotherTurn = False # Since player has  landed in  jail, he does not take another turn.
            self.collectSalary = False # he does not collect salary



        else:
            self.location_on_board += self.sum_of_numbers_rolled_on_dice
            if self.location_on_board > 39:
                self.location_on_board = self.location_on_board - 40
                if self.just_visiting_jail:
                    self.collectSalary = True


            printmessage("Player's location on board: " + str(self.location_on_board))


        self.locations_visited_by_player.append(self.location_on_board)



    def take_action(self):

        if (self.collectSalary):
        # player has passed through Go. He collects a salary of $200 from bank.
            printmessage(self.name + " collects salary.")
            salary = 200
            self.bank.pay_cash(self, salary)
            self.collectSalary = False


        square = self.game_board.get_square(self.location_on_board)

        printmessage("player lands on square: " + square.title)

        square.take_action(self)

        printmessage("player's cash: "+ str(self.cash))

        return
