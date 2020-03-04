# class Card:
#     def __init__(self, color, symbol):
#         self.color = color
#         self.symbol = symbol
#

import os
from random import shuffle


class Deck:
    def __init__(self):
        self.list = []
        self.SUITE = 'H D S C'.split()
        # self.RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
        self.RANKS = [[2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], ['J', 11], ['Q', 12],
                      ['K', 13], ['A', 14]]
        self.hand1 = []
        self.hand2 = []

    def add_cards(self):
        for i in range(len(self.SUITE)):
            for j in range(len(self.RANKS)):
                # self.append(Card(SUITE[i]),RANKS[j])
                self.list.append([self.SUITE[i], self.RANKS[j]])

    def get_cards(self):
        return self.list

    def mix_cards(self):
        shuffle(self.list)

    def split_deck(self):
        for _ in range(len(self.list)):
            if _ % 2 == 0:
                self.hand1.append(self.list[_])
            else:
                self.hand2.append(self.list[_])


class Hand:

    def __init__(self, list):
        self.list = list

    def give_card(self):
        return self.list.pop()

    def get_cards(self):
        return self.list

    def add_card(self, card):
        self.list.reverse()
        self.list.append(card)
        self.list.reverse()

    def add_cards(self, cards):
        self.list.reverse()
        self.list.extend(cards)
        self.list.reverse()

    def empty_hand(self):
        if self.get_cards():
            return False
        else:
            return True

    def count(self):
        return len(self.list)

    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    pass


class Player:

    def __init__(self, hand):
        self.hand = hand

    def set_name(self, name):
        self.name = name

    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    pass


def clear():
    os.system('cls')


###### GAME PLAY #######
print("Welcome to War, let's begin...")
game_on = True
deck = Deck()
deck.add_cards()
deck.mix_cards()
deck.split_deck()
player1 = Player(Hand(deck.hand1))
player2 = Player(Hand(deck.hand2))
s = 0

player1.set_name(input("Enter first player name: "))
player2.set_name(input("Enter second player name: "))
player1.hand.get_cards()
while game_on:
    # input("Press Enter to continue")
    cards = []
    card1 = player1.hand.give_card()
    card2 = player2.hand.give_card()
    cards.append(card1)
    cards.append(card2)
    #    print("{} throws {}{}.".format(player1.name, card1[0], card1[1][0]))
    #    print("{} throws {}{}.".format(player2.name, card2[0], card2[1][0]))
    if card1[1][1] == card2[1][1]:
        #        print("WAR!!!".format())
        cards.append(player1.hand.give_card())
        cards.append(player2.hand.give_card())
        card13 = player1.hand.give_card()
        card23 = player2.hand.give_card()
        cards.append(card13)
        cards.append(card23)
        #       print("{} throws {}{}.".format(player1.name, card13[0], card13[1][0]))
        #       print("{} throws {}{}.".format(player2.name, card23[0], card23[1][0]))
        if card13[1][1] > card23[1][1]:
            #            print("{} wins this round and takes cards.".format(player1.name))
            shuffle(cards)
            player1.hand.add_cards(cards)

        elif card13[1][1] < card23[1][1]:
            #            print("{} wins this round and takes cards.".format(player2.name))
            shuffle(cards)
            player2.hand.add_cards(cards)
        else:
            print("WAR of WAR!!!")
            input("Press Enter to continue")
            cards.append(player1.hand.give_card())
            cards.append(player2.hand.give_card())
            # brak obslugi braku kart w rece
            card15 = player1.hand.give_card()
            card25 = player2.hand.give_card()
            cards.append(card15)
            cards.append(card25)
            print("{} throws {}{}.".format(player1.name, card15[0], card15[1][0]))
            print("{} throws {}{}.".format(player2.name, card25[0], card25[1][0]))
            if card15[1][1] > card25[1][1]:
                print("{} wins this round and takes cards.".format(player1.name))
                shuffle(cards)
                player1.hand.add_cards(cards)

            elif card15[1][1] < card25[1][1]:
                print("{} wins this round and takes cards.".format(player2.name))
                shuffle(cards)
                player2.hand.add_cards(cards)
            else:
                print("WAR of WAR of WAR!!!")
                input("Press Enter to end - its over")
                print("{} iteration!".format(s))
                game_on = False

    elif card1[1][1] > card2[1][1]:
        #        print("{} wins this round and takes cards.".format(player1.name))
        shuffle(cards)
        player1.hand.add_cards(cards)

    elif card1[1][1] < card2[1][1]:
        #        print("{} wins this round and takes cards.".format(player2.name))
        shuffle(cards)
        player2.hand.add_cards(cards)
    else:
        print("There is no way you can see this")

    if player1.hand.empty_hand():
        print("{} won the game! Gratz. Its taked only {} iterations!".format(player2.name, s))
        print(player1.hand.count())
        print(player2.hand.count())
        game_on = False

    elif player2.hand.empty_hand():
        print("{} won the game! Gratz. Its taked only {} iterations!".format(player2.name, s))
        print(player1.hand.count())
        print(player2.hand.count())
        game_on = False

    #    print("---------------------------------------------------")
    #    print("{} got {} cards.".format(player1.name, player1.hand.count()))
    #    print("{} got {} cards.".format(player2.name, player2.hand.count()))
    s += 1
    if s % 100000 == 0:
        print(s)