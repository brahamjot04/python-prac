# In many card games, cards are either face up or face down. Add a new instance variable named faceup to the Card class to track this attribute of a card. Its default value is False. Then add a turn method to turn the card over. This method resets the faceup variable to its logical negation.

class Card:
    # A playing card.

    SUITS = ("Spades", "Hearts", "Diamonds", "Clubs")
    RANKS = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

    def __init__(self, suit, rank):
        # Creates a new card.
        if suit not in Card.SUITS:
            raise ValueError("Invalid suit: {}".format(suit))
        if rank not in Card.RANKS:
            raise ValueError("Invalid rank: {}".format(rank))
        self.suit = suit
        self.rank = rank
        self.faceup = False  # New instance variable to track if the card is face up

    def __str__(self):
        # """Returns a string representation of the card."""
        return "{} of {}".format(self.rank, self.suit)

    def turn(self):
        """Turns the card over."""
        self.faceup = not self.faceup


# Example usage
card = Card("Spades", "Q")
print(card)  # Output: Queen of Spades (initially face down)
card.turn()
print(card)  # Output: Queen of Spades (now face up)
