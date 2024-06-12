class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def is_palindrome(sub):
            return sub == sub[::-1]
        
        def dfs(start, path):
            if start == len(s):
                result.append(path)
                return
            for end in range(start + 1, len(s) + 1):
                if is_palindrome(s[start:end]):
                    dfs(end, path + [s[start:end]])
        
        result = []
        dfs(0, [])
        return result