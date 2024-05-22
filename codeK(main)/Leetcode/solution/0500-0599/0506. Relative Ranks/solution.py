class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        # Create a sorted copy of the score list in descending order
        sorted_scores = sorted(score, reverse=True)
        
        # Create a dictionary to map scores to their ranks
        rank = {val: i for i, val in enumerate(sorted_scores)}
        
        # Create the answer list
        answer = []
        for s in score:
            place = rank[s]
            if place == 0:
                answer.append("Gold Medal")
            elif place == 1:
                answer.append("Silver Medal")
            elif place == 2:
                answer.append("Bronze Medal")
            else:
                answer.append(str(place + 1))
        
        return answer