from collections import Counter

class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand) % groupSize != 0:
            return False
        
        hand_count = Counter(hand)
        
        for card in sorted(hand):
            if hand_count[card] > 0:
                for i in range(card, card + groupSize):
                    if hand_count[i] == 0:
                        return False
                    hand_count[i] -= 1
        return True