from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)

        for word in strs:
            count = [0] * 26  # Frequency array for 'a' to 'z'
            for char in word:
                count[ord(char) - ord('a')] += 1
            anagram_map[tuple(count)].append(word)

        return list(anagram_map.values())


strs = ["act", "pots", "tops", "cat", "stop", "hat", "vile", "veil", "live", "evil"]


result = Solution().groupAnagrams(strs)
print(result)
