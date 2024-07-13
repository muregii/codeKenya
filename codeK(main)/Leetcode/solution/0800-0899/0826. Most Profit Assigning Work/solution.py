class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        
        max_profit = 0
        i = 0
        best = 0
        
        for ability in worker:
            while i < len(jobs) and ability >= jobs[i][0]:
                best = max(best, jobs[i][1])
                i += 1
            max_profit += best
            
        return max_profit