class PokerHand(object):

    RESULT = ["Loss", "Tie", "Win"]
    CARDS = ['1','2','3','4','5','6','7','8','9','10','J','Q','K','A']
    RANKS = {'A': 14,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,'T': 10,'J': 11,'Q': 12,'K': 13}

    def __init__(self, hand):
        self.hand = list(hand.replace(' ',''))
        
    def compare_with(self, other):
        other = list(other.replace(' ',''))

        def check_for_pairs(self):
        	pass
  
        return check_for_pairs(self)

i = PokerHand("6S JD 7H 4S AS")
print(i.compare_with("AH AC 5H 6H 7S"))