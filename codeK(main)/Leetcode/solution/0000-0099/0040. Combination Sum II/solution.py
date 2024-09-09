class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(start, path, target):
            if target == 0:
                res.append(list(path))
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                path.append(candidates[i])
                backtrack(i + 1, path, target - candidates[i])
                path.pop()
        
        candidates.sort()
        res = []
        backtrack(0, [], target)
        return res