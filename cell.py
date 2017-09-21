class Cell:
    def __init__(self):
        self.card = None
        self.picked_up_card = None

    # pickup the card on the cell
    # return None if there is no card
    def pick_up(self):
        if self.card:
            self.picked_up_card = self.card
            self.card = None
            return self.picked_up_card
        else:
            return None

    # place a card on the cell and return True
    # return False if the cell is occupied
    def place_on(self, card):
        if not self.card:
            self.card = card
            return True
        return False

    # if fail to move the card which has be picked up, place it back
    def place_back(self):
        self.card = self.picked_up_card
        self.picked_up_card = None

    # if the card which has be picked up moved successfully, set picked_up_card to None
    def put_down(self):
        self.picked_up_card = None

    def __str__(self):
        if self.card:
            return '[' + '%3s' % self.card + ']'
        else:
            return '[   ]'
