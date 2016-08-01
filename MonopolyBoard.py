from Squares import *
from collections import deque
import random
from Card import *
from util import *


class MonopolyBoard:
    def __init__(self,  players, bank):
        # create all the squares of the game board.
        self.squares = {}
        self.players = players

        self.chance_squares = [7, 22, 36]
        self.community_chest_squares = [2, 17, 33]


        # create a randomly shuffled deck of community chest cards
        self.community_chest_card_deck = []
        orig_comm_chest = self.createCommunityChestCards()
        random.shuffle(orig_comm_chest)
        self.community_chest_card_deck = deque(orig_comm_chest)

        # create a randomly shuffled deck of chance cards
        self.chance_card_deck = []
        orig_chance = self.createChanceCards()
        random.shuffle(orig_chance)
        self.chance_card_deck = deque(orig_chance)

        self.populate_squares()
        self.bank = bank

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
        title_deed_info_rr = (25, 100)
        rr_price = 200

        reading_rr = RailRoad(5,  "Reading RailRoad",  rr_price,  title_deed_info_rr)
        self.squares[5] = reading_rr


        penn_rr = RailRoad(15, "Pennsylvania RailRoad",  rr_price,  title_deed_info_rr)
        self.squares[15] = penn_rr


        b_and_o_rr = RailRoad(25,  "B. & O. RailRoad",  rr_price, title_deed_info_rr)
        self.squares[25] = b_and_o_rr


        b_and_o_rr = RailRoad(35,  "Short Line RailRoad",  rr_price, title_deed_info_rr)
        self.squares[35] = b_and_o_rr

        # Utility Companies
        title_deed_info_u = (4,10,75)
        uc_price = 150

        electric_company = Utility(12, "Electric Company", uc_price,  title_deed_info_u)
        self.squares[12] = electric_company


        water_works = Utility(28,  "Water Works",  uc_price,  title_deed_info_u)
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
        free_parking = FreeParking(20, "Free Parking")
        self.squares[20] = free_parking

        # Go To Jail
        go_to_jail = GoToJailSquare(30, "Go To Jail", jail)
        self.squares[30] = go_to_jail


        # Community Chest
        for i in  self.community_chest_squares:
            community_chest = CommunityChest(i, "Community Chest", self.community_chest_card_deck)
            self.squares[i] = community_chest

        # Chance
        for j in self.chance_squares:
            chance = Chance(j, "Chance", self.chance_card_deck)
            self.squares[j] = chance



    def createCommunityChestCards(self):
        community_chest_card_deck = []
        community_chest_card_deck.append(DoctorFee())
        community_chest_card_deck.append(PayHospitalBill())
        community_chest_card_deck.append(PaySchoolTax())
        community_chest_card_deck.append(StreetRepairs())
        community_chest_card_deck.append(LifeInsuranceMaturity())
        community_chest_card_deck.append(StockSale())
        community_chest_card_deck.append(BeautyContest())
        community_chest_card_deck.append(YouInherit())
        community_chest_card_deck.append(ReceiveForServices())
        community_chest_card_deck.append(IncomeTaxRefund())
        community_chest_card_deck.append(XmasFund())
        community_chest_card_deck.append(BankError())
        community_chest_card_deck.append(GrandOperaOpening(self.players))
        community_chest_card_deck.append(AdvanceToGo())
        community_chest_card_deck.append(GetOutOfJailFree())
        community_chest_card_deck.append(GoToJail())
        return community_chest_card_deck

    def createChanceCards(self):
        chance_card_deck = []
        chance_card_deck.append(AdvanceToGo())
        chance_card_deck.append(GetOutOfJailFree())
        chance_card_deck.append(GoToJail())
        chance_card_deck.append(AdvanceToNearestUtility())
        chance_card_deck.append(AdvanceToIllinois())
        chance_card_deck.append(AdvanceToBoardWalk())
        chance_card_deck.append(AdvanceToNearestRailRoad())
        chance_card_deck.append(GoBack3Spaces())
        chance_card_deck.append(AdvanceToStCharlesPlace())
        chance_card_deck.append(TakeARideOnReading())
        chance_card_deck.append(AdvanceToNearestRailRoad())
        chance_card_deck.append(BankPaysYouADividend())
        chance_card_deck.append(BuildingAndLoanMatures())
        chance_card_deck.append(PayPoorTax())
        chance_card_deck.append(YouAreElectedBoardChairman(self.players))
        chance_card_deck.append(GeneralRepairs())
        return chance_card_deck



    def get_square(self, location):
        return self.squares[location]

    def printJustTheBoard(self):
        printmessage("")
        printmessage("printing just the board................")
        for i in range(40):
            printmessage(i, ":",self.squares[i].title )
        printmessage("")
        return

    def printChanceCardDeck(self):
        printmessage("Chance Cards:")
        for c in self.chance_card_deck:
            printmessage(c.__class__.__name__)
        return

    def printCommunityChestCardDeck(self):
        printmessage("Community chest cards:")
        for c in self.community_chest_card_deck:
            printmessage(c.__class__.__name__)
        return

    def printmessage(self):
        printmessage("")
        printmessage("********* MONOPOLY BOARD STATUS***************")
        printmessage("Bank's cash: " + str(self.bank.cash))
        printmessage("**********************************")
        for player in self.players:
            printmessage(player.name + ": ")
            printmessage("Current Location : "+ str(player.location_on_board))
            printmessage("Cash Owned:"+ str(player.cash))
            printmessage("Properties Owned:" + str(player.properties))
            printmessage("**********************************")
        printmessage("********* MONOPOLY BOARD STATUS ENDS ***************")





