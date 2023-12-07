from constants import RANKINGS_OF_CARDS


class Hand:
    def __init__(self, cards, hand_type, bid):
        self.cards = cards
        self.hand_type = hand_type
        self.bid = bid

    def __repr__(self):
        return f"Hand(cards={self.cards}, hand_type={self.hand_type}, bid={self.bid})"

    def compare_types(self, other_hand):
        if self.hand_type == other_hand.hand_type:
            return 0
        if self.hand_type < other_hand.hand_type:
            return 1

        return 2

    def compare_labels(self, other_hand):
        other_hand_cards = other_hand.cards
        for i in range(len(self.cards)):
            if self.cards[i] == other_hand_cards[i]:
                continue
            if RANKINGS_OF_CARDS.index(self.cards[i]) < RANKINGS_OF_CARDS.index(other_hand_cards[i]):
                return 1
            return 2

        return 0

    @property
    def get_bid(self):
        return int(self.bid)
