class Cascade:
    def __init__(self):
        self.cards = []
        # the card you have picked up
        self.picked_up_card = None

    # pickup the last card
    def pick_up(self):
        self.picked_up_card = self.get_last()
        return self.cards.pop()

    # place a card onto the cascade and return True
    # return False if fail to place it
    def place_on(self, card):
        last_card = self.get_last()
        if self.cards.__len__() == 0:
            self.cards.append(card)
            return True
        if card.face + 1 == last_card.face and (card.suit.value + last_card.suit.value) % 2 == 1:
            self.cards.append(card)
            return True
        return False

    # get card by index
    # return None if index is wrong
    def get_card(self, index):
        try:
            return self.cards[index]
        except IndexError:
            return None

    # get the last card
    # return None if there is no card
    def get_last(self):
        try:
            return self.cards[self.cards.__len__() - 1]
        except IndexError:
            return None

    # if fail to move the card which has be picked up, place it back
    def place_back(self):
        if self.picked_up_card:
            self.cards.append(self.picked_up_card)
            self.picked_up_card = None

    # if the card which has be picked up moved successfully, set picked_up_card to None
    def put_down(self):
        self.picked_up_card = None
