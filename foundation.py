from card import CardSuit


class Foundation:
    def __init__(self, suit):
        self.cards = []
        self.suit = CardSuit(suit)
        self.picked_up_card = None

    # if there is no card on the foundation, place the card which is Ace
    # else place the card when its face equals the last card's face plus 1
    def place_on(self, card):
        last_card = self.get_last()
        if not last_card:
            if card.face == 1 and card.suit == self.suit:
                self.cards.append(card)
                return True
        if card.suit == self.suit:
            if card.face == self.current_card.face + 1:
                self.cards.append(card)
                return True
        return False

    # pickup the last card
    # return None if there is no card
    def pick_up(self):
        try:
            return self.cards.pop()
        except IndexError:
            return None

    # if fail to move the card which has be picked up, place it back
    def place_back(self):
        self.cards.append(self.picked_up_card)
        self.picked_up_card = None

    # if the card which has be picked up moved successfully, set picked_up_card to None
    def put_down(self):
        self.picked_up_card = None

    # get the last card
    # return None if there is no card
    def get_last(self):
        try:
            return self.cards[self.cards.__len__() - 1]
        except IndexError:
            return None

    def __str__(self):
        if self.get_last():
            return '[' + '%3s' % self.get_last() + ']'
        else:
            return '[ ' + self.suit.name + ' ]'
