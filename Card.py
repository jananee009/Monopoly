from Bank import Bank

class Card:
     bank = Bank.Instance()
     def __init__(self, n, card_title):
         self.card_number = n
         self.title = card_title



     def take_action(self, card_type, card_title, player):

          if card_title =="Advance To Go":
              player.location_on_board = 0
              player.cash += 200
              Card.bank.cash -= 200
              return

          if card_title == "Go To Jail":
              player.location_on_board = 10
              # implement logic to not collect $200 while passing go.
              return

          if card_title == "Get Out Of Jail Free":
              player.get_out_of_jail_free_card = True
              return

          if card_type == "Community Chest":
              if card_title == "Doctor's Fee":
                  player.cash -= 50
                  Card.bank.cash += 50
                  return

              if card_title == "Pay Hospital Bill":
                  player.cash -= 100
                  Card.bank.cash += 100
                  return

              if card_title == "Pay School Tax":
                  player.cash -= 150
                  Card.bank.cash += 150
                  return

              if card_title == "Assessed For Street Repairs":
                  street_repairs_cost = ((40*player.total_number_of_houses_owned) + (115*player.total_number_of_hotels_owned))
                  player.cash -= street_repairs_cost
                  Card.bank.cash += street_repairs_cost
                  return

              if card_title == "Life Insurance Matures":
                  player.cash += 100
                  Card.bank.cash -= 100
                  return

              if card_title == "Sale Of Stock":
                  player.cash += 45
                  Card.bank.cash -= 45
                  return

              if card_title == "2nd Price In Beauty Contest":
                  player.cash += 10
                  Card.bank.cash -= 10
                  return

              if card_title == "You Inherit":
                  player.cash += 100
                  Card.bank.cash -= 100
                  return

              if card_title == "Receive For Services":
                  player.cash += 25
                  Card.bank.cash -= 25
                  return

              if card_title == "Income Tax Refund":
                  player.cash += 20
                  Card.bank.cash -= 20
                  return

              if card_title == "Xmas Fund Matures":
                  player.cash += 100
                  Card.bank.cash -= 100
                  return

              if card_title == "Bank Error In Your Favor":
                  player.cash += 200
                  Card.bank.cash -= 200
                  return

              if card_title == "Grand Opera Opening":
                  # TODO : implement logic for collecting $50 from each player.
                  return


          if card_type == "Chance": # chance cards

              if card_title == "Go Back 3 spaces":
                  player.location_on_board -= 3
                  # TODO: implement the following
                  # going back 3 spaces on the board can land the player in one of the following squares:
                  # a) Income Tax
                  # b) New York Avenue
                  # c) Community Chest
                  return

              if card_title == "Advance To Illinois":
                  if player.location_on_board == 36: # check the player's current location
                   # the player has to pass through Go to advance to illinois ave. Hence he collects $200.
                      player.cash += 200
                      Card.bank.cash -= 200

                  # if the player is located on other Chance Squares, he will not pass "Go" to advance to Illinois Ave.
                  player.location_on_board = 24
                  # TODO implement logic to buy / pay rent for Illinois Ave.
                  return

              if card_title ==   "Advance To BoardWalk":
                  player.location_on_board = 39
                  # TODO implement logic to buy / pay rent for BoardWalk
                  return

              if  card_title ==   "Advance To  St. Charles Place":
                  if player.location_on_board in [36, 22]:
                      # the player has to pass through Go to advance to St. Charles Place Hence he collects $200.
                      player.cash += 200
                      Card.bank.cash -= 200

                  player.location_on_board = 11
                  # TODO implement logic to buy / pay rent for St. Charles Place
                  return


              if  card_title ==   "Building And Loan Matures":
                  player.cash += 200
                  Card.bank.cash -= 200
                  return

              if  card_title ==   "Bank Pays You A Dividend":
                  player.cash += 50
                  Card.bank.cash -= 50
                  return

              if card_title == "Pay Poor Tax":
                  player.cash -= 15
                  Card.bank.cash += 15
                  return

              if card_title == "Make General Repairs On All Your Property":
                  general_repairs_cost = ((25 * player.total_number_of_houses_owned) + (100 * player.total_number_of_hotels_owned))
                  player.cash -= general_repairs_cost
                  Card.bank.cash += general_repairs_cost
                  return

              if  card_title == "You Are Elected Board Chairman":
                  # TODO : implement logic for paying $50 to each player.
                  return

              if card_title ==  "Advance To Nearest Utility":
                  if player.location_on_board in [7,36]:
                      player.location_on_board = 12

                  else:
                      player.location_on_board = 28

                  # TODO: implement logic for either buying it or paying 10*amt shown on dice as rent.
                  return

              if card_title == "Advance To Nearest RailRoad":
                  if player.location_on_board == 7:
                      player.location_on_board = 15

                  elif player.location_on_board == 22:
                      player.location_on_board = 25

                  elif player.location_on_board == 36:
                      player.location_on_board = 5

                  # TODO   implement logic for either buying it or paying 2*rent entitled to owner.
                  return

              if card_title == "Take A Ride On Reading":
                  player.location_on_board = 5
                  player.cash += 200
                  Card.bank.cash -= 200
                  # TODO: If Reading is already owned, should player pay rent or buy it? Nothing is mentioned on the card.
                  return












