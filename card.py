from enum import Enum


# enum for card face
class CardFace(Enum):
    X = 10  # Ten
    J = 11  # Jack
    Q = 12  # Queen
    K = 13  # King


# enum for card suit
class CardSuit(Enum):
    S = 0  # spade
    H = 1  # heart
    C = 2  # club
    D = 3  # diamond


class Card:
    def __init__(self, card_face, card_suit):
        self.face = card_face
        self.suit = card_suit

    def __str__(self):
        if self.face < 10:
            s = str(self.face)
        else:
            s = str(CardFace(self.face).name)
        s += ':' + str(self.suit.name)
        return s
