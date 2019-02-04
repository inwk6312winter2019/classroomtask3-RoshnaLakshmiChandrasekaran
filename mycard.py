lass card()
""" This creates a card object"""
        suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                    '8', '9', '10', 'Jack', 'Queen', 'King']

        def__init__(self,rank = 0, suite = 2 );
                self.rank = rank
                self.suite = suite
        return '%s of %s' % (Card.rank_names[self.rank],
                 Card.suit_names[self.suit])
