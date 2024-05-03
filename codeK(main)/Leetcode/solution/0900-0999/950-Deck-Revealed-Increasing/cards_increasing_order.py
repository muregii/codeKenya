class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        n = len(deck)
        deck.sort()
        queue = list(range(n))
        result = [0] * n

        for i in range(n):
            result[queue.pop(0)] = deck[i]
            if queue:
                queue.append(queue.pop(0))

        return result