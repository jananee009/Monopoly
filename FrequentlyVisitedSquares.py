import time
from MonopolyBoard import MonopolyBoard
from Bank import Bank
from Player import Player
from util import *
from  collections import Counter








def play_monopoly(n, board, bank, player_list):

    try:

        printmessage("****************** Simulation Begins ******************")

        simulation_number = 0

        while ( simulation_number <  n): # while all players have cash
            printmessage("**** SIMULATION NO: " + str(simulation_number)+" *****")
            for player in player_list:

                while(True):
                    player.play()
                    if not player.playAnotherTurn:
                        break

            simulation_number += 1

        printmessage("****************** Simulation Ends ******************")
        printmessage("Number of rounds played: " + str(simulation_number))
        printmessage("Player's cash: "+str(player.cash))
        printmessage("Locations visited by player: " + str( player.locations_visited_by_player))
        most_visited_squares_counts = Counter(player.locations_visited_by_player).most_common(40)
        printmessage("Most visited Squares" + str(most_visited_squares_counts))
        return

    except ValueError as err:
        print(err.args)


def createPlayers(n, bank):
    cash_for_each_player = 1500
    p = [Player("player_"+str(i), cash_for_each_player) for i in range(n)]
    bank.cash -= (n * cash_for_each_player)
    return p


def main():
    start_time = time.time()
    # creating a new log file
    create_file()
    the_bank = Bank.Instance()
    number_of_players = 1
    the_players = createPlayers(number_of_players, the_bank)
    game_board = MonopolyBoard( the_players, the_bank)
    for player in the_players:
        player.game_board = game_board
    number_of_simulations = 4
    play_monopoly(number_of_simulations, game_board, the_bank, the_players)

    printmessage("Problem solved in %s seconds " +str( (time.time() - start_time)))


if __name__ == "__main__":
    main()