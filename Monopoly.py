# In a game of Monopoly (the classic edition), with 2 players, we want to find the best strategy to win the game.
# A player's goal is to become rich by buying, renting or trading properties.
# The game continues until one of the players becomes bankrupt. The remaining player is declared the winner.
# The Game:
# i) The game board has 40 spaces including "Go".
# ii) Properties: a) There are 22 color coded property locations, which can be purchased by players when they land on them.
# b) There are 4 rail road companies.
# c) There are 2 utility companies ( water and electric).
# iii) There are 3 spaces each for community chest and chance cards.
# iv) Each player rolls a two 6-sided dice and moves on the board.
# We will assume that both players are playing strategically.
# To solve the problem, we will find:
# a. which are the most frequently visited locations on the board ? This information will be used by both players to buy properties.



# Data Structures needed:
# An iterable  to maintain the "Chance" cards.
# An iterable to store "Community Chest " cards.
# An iterable (of length n for n simulations) to keep track of which square the player landed on, finally, at the end of every simulation.

# Things to do:
# Simulate the roll of 2 6-sided dice.

# Set up the game board.
# Each location of the board means someth


# Set up a bank.
# Maintain the count of notes available under each denomination.
# Track the number of houses, hotels that are available with the bank.

# Players:
# Track each player's:
# a) position on the board
# b) liquid cash
# c) properties purchased
# d) houses bought
# e) hotel bought
# f) Mortgages

# For the Community Chest card:
# a) There are 16 CC cards. Shuffle the cards at the start of the game. This is achieved by randomly sampling without replacement 16 numbers in the range (1,16) both inclusive.
# b) Each time the player lands on the Community Chest square, get the first number (and the corresponding chance card) from the beginning of the random list.
# c) Once the card is read, remove the number from the beginning and append the number  to the end of the random list.

# For the Chance card:
# a) These work exactly the same as Community Chest cards.

# Track the number landed on the 2 dice each time they are rolled. This number can be used to calculate the probability of landing a sum when 2 dice are rolled.
# This in turn can be used to check whether our simulation has been truly close to random. (We can easily calculate the probability of getting a specific sum using basic probability).

# How to store the result of each simulation?
# In each simulation:
# 2 Dice are rolled. We will store the sum of the dice.
# We will store in which square the player finally landed. i.e. We will store the game_board_square_number.

# once we run the simulation for 1000000 times, we can count the total number of times the each square was  visited and compute the required result.


import time
import random
from MonopolyBoard import MonopolyBoard
from Bank import Bank
from Player import Player
from operator import itemgetter





# this method returns the list of player numbers in the order in which they will play the game.
# This is determined by which player rolls the highest sum ( using the two 6-sided dice).
# If there is a tie between two or more players, each player rolls again to determine the order.

def determinePlayOrder(total_number_of_players):
    while (True):
        # construct a list of tuples (a,b) where a = player_number and b = value of dice rolled by that player
        player_scores = [ ( p, random.randint(1, 6) + random.randint(1, 6) ) for p in range(total_number_of_players)]
        scores = [ tuple[1] for tuple in player_scores] # get only the values rolled by players in to a list.

        if len(scores) == len(set(scores)): # check if values rolled by all players are different.
            # there is no  tie.

            # player who rolls the highest value on the dice begins the game.
            player_scores.sort(key=itemgetter(1), reverse=True) # sort the tuples in descending order of  the values rolled by players.
            player_order = [ tuple[0] for tuple in player_scores ] # get the player numbers from the sorted list.

            return player_order
        else:
            # two or more players have rolled the same sum. To resolve the tie, all players will roll their dice again.
            continue



def roll_dice():
    return (random.randint(1,6)+random.randint(1,6))

def play_monopoly(n, board, bank, player_list):

    print("****** At the start of the game: ********")

    board.print()
    print("")
    print("Bank's Properties: ")
    print(len(bank.properties))
    print([property for property in bank.properties])
    print("")

    # determine who will begin the game:
    player_order = determinePlayOrder(len(player_list))

    players = [player_list[player_number] for player_number in  player_order]


    number_of_throws_each = 0

    while ( True ): # while all players have cash

        # for each player, check if cash == 0 and add them to losers.
        losers = [ p for p in players if p.cash <= 0 ]

        if(number_of_throws_each >= 1):
            break
        # remove  losers from players list
        for p in losers:
            players.remove(p)

        # after removing all losers, if there is only one player left, he is the winner.
        if (len(players) == 1):
            return players[0]

        print("Play begins........................")

        for player in players:

            # Player rolls dice to determine new position
            player.play()
            print("player name: ",player.name)
            print ("sum rolled:",player.list_of_numbers_rolled)
            print("square number visited: ",player.locations_visited_by_player)
            print( "square visited: ", board.get_square( player.locations_visited_by_player[-1] ).title )
            print("")
            print("*******************")

            number_of_throws_each += 1
        board.print()
        print("Bank's liquid cash: ",bank.cash)
    return



def createPlayers(n, bank):
    cash_for_each_player = 1500
    p = [Player("player_"+str(i), cash_for_each_player) for i in range(n)]
    bank.cash -= (n * cash_for_each_player)
    return p


def main():
    start_time = time.time()

    the_bank = Bank.Instance()
    number_of_players = 2
    the_players = createPlayers(number_of_players, the_bank)
    game_board = MonopolyBoard( the_players, the_bank)
    for player in the_players:
        player.game_board = game_board
    number_of_simulations = 1
    play_monopoly(number_of_simulations, game_board, the_bank, the_players)

    print ("Problem solved in %s seconds " % (time.time() - start_time))


if __name__ == "__main__":
    main()