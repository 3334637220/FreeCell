import random
from card import Card, CardSuit
from cascade import Cascade
from foundation import Foundation
from cell import Cell


class Deck:
    def __init__(self, value_start, value_end, number_of_suits):
        self.cascades = [Cascade() for i in range(8)]
        self.foundations = [Foundation(i) for i in range(4)]
        self.cells = [Cell() for i in range(4)]
        self.cards = []
        # init the cards
        for i in range(number_of_suits):
            suit = CardSuit(i)
            for j in range(value_start, value_end + 1):
                self.cards.append(Card(j, suit))
        # shuffle the cards
        self.shuffle()
        # draw card from cards and place them onto eight cascades
        while self.cards.__len__() > 0:
            for cascade in self.cascades:
                card = self.draw_card()
                if card:
                    cascade.cards.append(card)
                else:
                    break

    # A shuffle method randomize the cards
    def shuffle(self):
        random.shuffle(self.cards)

    # A function to add a card to deck
    def add_card(self, card):
        self.cards.append(card)

    # A function draw a card
    # return None if there no card
    def draw_card(self):
        try:
            return self.cards.pop()
        except IndexError:
            return None

    # A function to move card
    def move(self):
        pick_info = self.pick()
        if pick_info:
            if self.place(pick_info[0], pick_info[1]):
                print('Move card ' + str(pick_info[0]) + ' successfully!')
                return True
            else:
                print('Fail to move card ' + str(pick_info[0]))
                return False

    # pick one card and return the position
    def pick(self):
        # position where you want to pick up a card
        pick_pos_index = int(input('\nPick up from ?\n'
                                   '\t1. Cascade\n'
                                   '\t2. Foundation\n'
                                   '\t3. Cell\n'))

        # pick up a card from cascade
        if pick_pos_index == 1:
            # choose one cascade
            cascade_pick_index = int(input('Choose one cascade: (1-8)\n'))
            if cascade_pick_index not in range(1, 9):
                print('<Error>: please input 1-8!')
                return False
            cascade_pick = self.cascades[cascade_pick_index - 1]
            # pick up one card
            card_pick = cascade_pick.pick_up()
            pick_pos = cascade_pick
            # return False if the card does not exist
            if not card_pick:
                print('<Error>: the card does not exist')
                return False
        # pick up a card from foundation
        elif pick_pos_index == 2:
            # choose one foundation
            foundation_pick_index = int(input('Choose one foundation: (1-4)\n'))
            if foundation_pick_index not in range(1, 5):
                print('<Error>: please input 1-4!')
                return False
            foundation_pick = self.foundations[foundation_pick_index - 1]
            card_pick = foundation_pick.pick_up()
            pick_pos = foundation_pick
            if not card_pick:
                print('<Error>: the card does not exist')
                return False
        # pick up a card from cell
        elif pick_pos_index == 3:
            # choose one cell
            cell_pick_index = int(input('Choose one cell: (1-4)\n'))
            if cell_pick_index not in range(1, 5):
                print('<Error>: please input 1-5!')
                return False
            cell_pick = self.cells[cell_pick_index - 1]
            card_pick = cell_pick.pick_up()
            pick_pos = cell_pick
            if not card_pick:
                print('<Error>: the card does not exist')
                return False
        else:
            print('<Error>: please input 1-3!')
            return False

        # print the card which you have picked up
        print('pick up card: ' + str(card_pick))
        return card_pick, pick_pos

    # place the card
    # put down the card when place successfully
    # place back the card when fail to place it
    def place(self, card_pick, pick_pos):
        # position where you want to place the card onto
        place_pos_index = int(input('\nPlace onto ?\n'
                                    '\t1. Cascade\n'
                                    '\t2. Foundation\n'
                                    '\t3. Cell\n'))
        # place onto cascade
        if place_pos_index == 1:
            cascade_place_index = int(input('Choose one cascade: (1-8)\n'))
            if cascade_place_index not in range(1, 9):
                print('<Error>: please input 1-8!')
                # Found an error and place back the card
                pick_pos.place_back()
                return False
            cascade_place = self.cascades[cascade_place_index - 1]

            if cascade_place.place_on(card_pick):
                # success to move the card and put down it
                pick_pos.put_down()
                return True
            else:
                # Found an error and place back the card
                pick_pos.place_back()
        # place onto foundation
        elif place_pos_index == 2:
            foundation_place_index = int(input('Choose one foundation: (1-4)\n'))
            if foundation_place_index not in range(1, 5):
                print('<Error>: please input 1-4!')
                # Found an error and place back the card
                pick_pos.place_back()
                return False
            foundation_target = self.foundations[foundation_place_index - 1]
            if foundation_target.place_on(card_pick):
                # success to move the card and put down it
                pick_pos.put_down()
                return True
            else:
                # Found an error and place back the card
                pick_pos.place_back()
        # place onto cell
        elif place_pos_index == 3:
            cell_place_index = int(input('Choose one cell: (1-4)\n'))
            if cell_place_index not in range(1, 5):
                print('<Error>: please input 1-4!')
                # Found an error and place back the card
                pick_pos.place_back()
                return False
            cell_place = self.cells[cell_place_index - 1]
            if cell_place.place_on(card_pick):
                # success to move the card and put down it
                pick_pos.put_down()
                return True
            else:
                # Found an error and place back the card
                pick_pos.place_back()
        else:
            print('<Error>: please input 1-3!')
            # Found an error and place back the card
            pick_pos.place_back()
            return False

    # return True if victory is achieved
    def victory(self):
        for f in self.foundations:
            if not f.get_last() or f.get_last().face != 13:
                return False
        return True

    # print the deck
    def print(self):
        print('_' * 65)
        print('Cells', end='\t' * 7)
        print('Foundations')
        for c in self.cells:
            print(c, end='\t')
        for f in self.foundations:
            print(f, end='\t')
        print()
        max_len = 0
        for cascade in self.cascades:
            if cascade.cards.__len__() > max_len:
                max_len = cascade.cards.__len__()
        for i in range(max_len):
            for cascade in self.cascades:
                if cascade.get_card(i):
                    print('%4s' % cascade.get_card(i), end='\t')
                else:
                    print('%4s' % '', end='\t')
            print()
        print('_' * 65)
