#Group Anagrams Leetcode Challenge
#Given an array of strings strs, group the anagrams together.
#You can return the answer in any order.    

from collections import defaultdict

def group_anagrams(strs):
    anagram_map = defaultdict(list)

    for word in strs:
        key = ''.join(sorted(word))
        anagram_map[key].append(word)

    return list(anagram_map.values())

# Example usage
if __name__ == "__main__":
    test_input = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = group_anagrams(test_input)
    print("Grouped Anagrams:", result)

