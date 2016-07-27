from Squares import *
from collections import deque
import random
from Card import Card



class MonopolyBoard:
    def __init__(self,  players, bank):
        # create all the squares of the game board.
        self.squares = {}
        self.community_chest_cards = {}
        #self.bank = bank
        self.players = players
        self.chance_squares = [7, 22, 36]
        self.community_chest_squares = [2, 17, 33]

        self.community_chest_card_deck = deque(random.sample(range(1, 17), 16))  # shuffle the community chest card deck at the start of the game.
        self.chance_card_deck = deque(random.sample(range(1, 17), 16))  # shuffle the chance card deck at the start of the game.
      
        self.populate_squares()
        self.createCommunityChestCards()
        self.createChanceCards()


    def populate_squares(self):

        #bank =  Bank.Instance()

        # Go
        go = Go(0, "Go")
        self.squares[0] = go

        # purple color group
        title_deed_info_land = ("Purple", 2, 10, 30, 90, 160, 250, 30, 50, (50, 4))
        mediterranean_ave = Land(1, "Mediterranean Avenue",  60,  title_deed_info_land)
        self.squares[1] = mediterranean_ave

        title_deed_info_land = ("Purple", 4, 20, 60, 180, 320, 450, 30, 50, (50, 4))
        baltic_ave = Land(3, "Baltic Avenue", 60,  title_deed_info_land)
        self.squares[3] = baltic_ave

        # light blue color group
        title_deed_info_land = ("Light Blue", 6, 30, 90, 270, 400, 550, 50, 50, (50, 4))
        oriental_ave = Land(6,  "Oriental Avenue", 100, title_deed_info_land)
        self.squares[6] = oriental_ave

        title_deed_info_land = ("Light Blue",6, 30, 90, 270, 400, 550, 50, 50, (50, 4))
        vermont_ave = Land(8,  "Vermont Avenue", 100,  title_deed_info_land)
        self.squares[8] = vermont_ave

        title_deed_info_land = ("Light Blue", 8, 40, 100, 300, 450, 600, 60, 50, (50, 4))
        connecticut_ave = Land(9, "Connecticut Avenue", 120,  title_deed_info_land)
        self.squares[9] = connecticut_ave

        # pink color group
        title_deed_info_land = ("Pink", 10, 50, 150, 450, 625, 750, 70, 100, (100, 4))
        st_charles_pl = Land(11, "St. Charles Place",  140,  title_deed_info_land)
        self.squares[11] = st_charles_pl

        title_deed_info_land = ("Pink", 10, 50, 150, 450, 625, 750, 70, 100, (100, 4))
        states_ave = Land(13,  "States Avenue", 140, title_deed_info_land)
        self.squares[13] = states_ave

        title_deed_info_land = ("Pink", 12, 60, 180, 500, 700, 900, 80, 100, (100, 4))
        virginia_ave = Land(14,  "Virginia Avenue",  160,  title_deed_info_land)
        self.squares[14] = virginia_ave


        # Orange Color Group
        title_deed_info_land = ("Orange",14, 70, 200, 550, 750, 950, 90, 100, (100, 4))
        st_james_pl = Land(16,  "St. James Place",  180,  title_deed_info_land)
        self.squares[16] = st_james_pl

        title_deed_info_land = ("Orange", 14, 70, 200, 550, 750, 950, 90, 100, (100, 4))
        tennessee_ave = Land(18,  "Tennessee Avenue",  180,  title_deed_info_land)
        self.squares[18] = tennessee_ave

        title_deed_info_land = ("Orange", 16, 80, 220, 600, 800, 1000, 100, 100, (100, 4))
        new_york_ave = Land(19,  "New York Avenue",   200, title_deed_info_land)
        self.squares[19] = new_york_ave

        # Red color group
        title_deed_info_land = ("Red", 18, 90, 250, 700, 875, 1050, 110, 150, (150, 4))
        kentucky_ave = Land(21,  "Kentucky Avenue",  220,  title_deed_info_land)
        self.squares[21] = kentucky_ave

        title_deed_info_land = ("Red", 18, 90, 250, 700, 875, 1050, 110, 150, (150, 4))
        indiana_ave = Land(23, "Indiana Avenue",  220,  title_deed_info_land)
        self.squares[23] = indiana_ave

        title_deed_info_land = ("Red", 20, 100, 300, 750, 925, 1100, 120, 150, (150, 4))
        illinois_ave = Land(24,  "Illinois Avenue",  240,  title_deed_info_land)
        self.squares[24] = illinois_ave

        # Yellow Group
        title_deed_info_land = ("Yellow", 22, 110, 330, 800, 975, 1150, 130, 150, (150, 4))
        atlantic_ave = Land(26, "Atlantic Avenue",  260,  title_deed_info_land)
        self.squares[26] = atlantic_ave

        title_deed_info_land = ("Yellow", 22, 110, 330, 800, 975, 1150, 130, 150, (150, 4))
        ventnor_ave = Land(27, "Ventnor Avenue",   260,  title_deed_info_land)
        self.squares[27] = ventnor_ave

        title_deed_info_land = ("Yellow", 24, 120, 360, 850, 1025, 1200, 140, 150, (150, 4))
        marvin_gardens = Land(29,  "Marvin Gardens",  280,  title_deed_info_land)
        self.squares[29] = marvin_gardens

        # Green Color Group
        title_deed_info_land = ("Green", 26, 130, 390, 900, 1100, 1275, 150, 200, (200, 4))
        pacific_ave = Land(31, "Pacific Avenue", 300,  title_deed_info_land)
        self.squares[31] = pacific_ave

        title_deed_info_land = ("Green", 26, 130, 390, 900, 1100, 1275, 150, 200, (200, 4))
        no_carolina_ave = Land(32, "North Carolina Avenue",  300,  title_deed_info_land)
        self.squares[32] = no_carolina_ave

        title_deed_info_land = ("Green", 28, 150, 450, 1000, 1200, 1400, 160, 200, (200, 4))
        pennsylvania_ave = Land(34,  "Pennsylvania Avenue",  320,  title_deed_info_land)
        self.squares[34] = pennsylvania_ave


        # Dark blue group
        title_deed_info_land = ("Dark Blue", 35, 175, 500, 1100, 1300, 1500, 175, 200, (200, 4))
        parks_pl = Land(37,  "Parks Place", 350,  title_deed_info_land)
        self.squares[37] = parks_pl

        title_deed_info_land = ("Dark Blue", 50, 200, 600, 1400, 1700, 2000, 200, 200, (200, 4))
        boardwalk = Land(39,  "BoardWalk",  400,  title_deed_info_land)
        self.squares[39] = boardwalk

        # Railroad Companies
        title_deed_info_rr = (25, 50, 100, 200, 100)
        reading_rr = RailRoad(5,  "Reading RailRoad",  200,  title_deed_info_rr)
        self.squares[5] = reading_rr

        title_deed_info_rr = (25, 50, 100, 200, 100)
        penn_rr = RailRoad(15, "Pennsylvania RailRoad",  200,  title_deed_info_rr)
        self.squares[15] = penn_rr

        title_deed_info_rr = (25, 50, 100, 200, 100)
        b_and_o_rr = RailRoad(25,  "B. & O. RailRoad",  200, title_deed_info_rr)
        self.squares[25] = b_and_o_rr

        title_deed_info_rr = (25, 50, 100, 200, 100)
        b_and_o_rr = RailRoad(35,  "Short Line RailRoad",  200, title_deed_info_rr)
        self.squares[35] = b_and_o_rr

        # Utility Companies
        title_deed_info_u = (4,10)
        electric_company = Utility(12, "Electric Company", 150,  title_deed_info_u)
        self.squares[12] = electric_company

        title_deed_info_u = (4, 10)
        water_works = Utility(28,  "Water Works",  150,  title_deed_info_u)
        self.squares[28] = water_works

        # Income Tax
        income_tax = Tax(4, "Income Tax", 200)
        self.squares[4] = income_tax

        # Luxury Tax
        luxury_tax = Tax(38, "Luxury Tax", 75)
        self.squares[38] = luxury_tax

        # Jail
        jail = Jail(10, "Jail", 50)
        self.squares[10] = jail


        # Free Parking
        free_parking = Square(20, "Free Parking")
        self.squares[20] = free_parking

        # Go To Jail
        go_to_jail = GoToJail(30, "Go To Jail", jail)
        self.squares[30] = go_to_jail


        # Community Chest
        for i in  self.community_chest_squares:
            community_chest = CommunityChest(i, "Community Chest")
            self.squares[i] = community_chest

        # Chance
        for j in self.chance_squares:
            chance = Chance(j, "Chance")
            self.squares[j] = chance


    def createCommunityChestCards(self):
        doctor_fee = Card(1,"Doctor's Fee")
        self.community_chest_cards[1] = doctor_fee

        hospital_bill = Card(2, "Pay Hospital Bill")
        self.community_chest_cards[2] = hospital_bill

        school_tax = Card(3, "Pay School Tax")
        self.community_chest_cards[3] = school_tax

        street_repairs = Card(4, "Assessed For Street Repairs")
        self.community_chest_cards[4] = street_repairs

        life_insurance = Card(5, "Life Insurance Matures")
        self.community_chest_cards[5] = life_insurance

        stock_sale = Card(6, "Sale Of Stock")
        self.community_chest_cards[6] = stock_sale

        beauty_contest = Card(7, "2nd Price In Beauty Contest")
        self.community_chest_cards[7] = beauty_contest

        inheritance = Card(8, "You Inherit")
        self.community_chest_cards[8] = inheritance

        receive_services = Card(9, "Receive For Services")
        self.community_chest_cards[9] = receive_services

        tax_refund = Card(10, "Income Tax Refund")
        self.community_chest_cards[10] = tax_refund

        xmas_fund = Card(11, "Xmas Fund Matures")
        self.community_chest_cards[11] = xmas_fund

        bank_error = Card(12, "Bank Error In Your Favor")
        self.community_chest_cards[12] = bank_error

        grand_opera = Card(13, "Grand Opera Opening")
        self.community_chest_cards[13] = grand_opera

        advance_to_go = Card(14, "Advance To Go")
        self.community_chest_cards[7] = advance_to_go

        get_out_of_jail = Card(15, "Get Out Of Jail Free")
        self.community_chest_cards[15] = get_out_of_jail

        go_to_jail = Card(16, "Go To Jail")
        self.community_chest_cards[16] = go_to_jail

    def createChanceCards(self):

        advance_to_go = Card(1, "Advance To Go")
        self.community_chest_cards[1] = advance_to_go

        get_out_of_jail = Card(2, "Get Out Of Jail Free")
        self.community_chest_cards[2] = get_out_of_jail

        go_to_jail = Card(3, "Go To Jail")
        self.community_chest_cards[3] = go_to_jail

        go_to_utility = Card(4, "Advance To Nearest Utility")
        self.community_chest_cards[4] = go_to_utility

        go_to_illinois = Card(5, "Advance To Illinois")
        self.community_chest_cards[3] = go_to_illinois

        go_to_boardwalk = Card(6, "Advance To BoardWalk")
        self.community_chest_cards[6] = go_to_boardwalk

        go_to_railroad_1 = Card(7, "Advance To Nearest RailRoad")
        self.community_chest_cards[7] = go_to_railroad_1

        go_back = Card(8, "Go Back 3 spaces")
        self.community_chest_cards[8] = go_back

        go_to_charles_place = Card(9, "Advance To  St. Charles Place")
        self.community_chest_cards[9] = go_to_charles_place

        go_to_reading = Card(10, "Take A Ride On Reading")
        self.community_chest_cards[10] = go_to_reading

        go_to_railroad_2 = Card(11, "Advance To Nearest RailRoad")
        self.community_chest_cards[11] = go_to_railroad_2

        bank_dividend = Card(12, "Bank Pays You A Dividend")
        self.community_chest_cards[12] = bank_dividend

        building_loan_matures = Card(13, "Building And Loan Matures")
        self.community_chest_cards[13] = building_loan_matures

        poor_tax = Card(14, "Pay Poor Tax")
        self.community_chest_cards[14] = poor_tax

        board_chairman = Card(15, "You Are Elected Board Chairman")
        self.community_chest_cards[15] = board_chairman

        general_repairs = Card(16, "Make General Repairs On All Your Property")
        self.community_chest_cards[16] = general_repairs



    def get_square(self, location):
        return self.squares[location]

    def printJustTheBoard(self):
        print("")
        print("printing just the board................")
        for i in range(40):
            print(i, ":",self.squares[i].title )
        print("")
        return


    def print(self):
        for player in self.players:
            print(player.name, ": ")
            print("Location :", player.location_on_board)
            print("Cash :", player.cash)
            print("Property :", player.properties)
            print ("**********************************")





        #   community_chest_card_dict = {1: advance_to_go, 2: go_to_jail}

