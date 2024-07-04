# Leetcode - Find Common Characters

## Problem Description

Given a string array `words`, return an array of all characters that show up in all strings within the `words` (including duplicates). You may return the answer in **any order**.

**Constraints:**
- `1 <= words.length <= 100`
- `1 <= words[i].length <= 100`
- `words[i]` consists of lowercase English letters.

## Solution

To find the common characters that appear in all strings within the `words` array, identify the frequency of each character in every string and then find the minimum occurrence of each character across all strings.


Imagine you have a bunch of friends, and each of them has a box of colored letters. You want to find out which letters all of your friends have in common and count how many of each letter they share. For example, if every friend has at least one red letter, you can say that red is common among them. If two friends have one green letter, but the other friend has three, green is still common, but only as many times as the least amount any friend has.



Here are the steps:

1. **Count Character Frequencies:**
   - Use a dictionary or a counter to count the occurrences of each character in each string.
   
2. **Find Minimum Occurrences:**
   - For each character, determine the minimum number of times it appears in all strings. This will give us the maximum number of times that character can appear in the result.

3. **Build the Result List:**
   - Add each character to the result list as many times as its minimum occurrence across all strings.


By counting the occurrences of each character in every string and then finding the minimum count for each character, we can build a list of characters that are common in all strings. Each character will appear in the result as many times as it appears in the string with the least occurrences of that character.


```python
class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
```

## Usage

To use the solution, create an instance of the `Solution` class and call the `commonChars` method with the list of words:

```python
solution = Solution()
words = ["bella", "label", "roller"]
result = solution.commonChars(words)
print(result)  # Output: ['e', 'l', 'l'], common characters in all words
```

[Link to detailed explanation on GeeksforGeeks](https://www.geeksforgeeks.org/common-characters-n-strings/)

[Link to detailed explanation on Medium](https://medium.com/leetcode-cracker/1002-find-common-characters-a80ed5f180ac)

[Link to detailed explanation on AlgoMonster](https://algo.monster/liteproblems/1002)

## Check Out This Video

[![Video Explanation](https://img.youtube.com/vi/QEESBA2Q_88/mqdefault.jpg)](https://youtu.be/QEESBA2Q_88)

[![Video Explanation](https://img.youtube.com/vi/lPx-Yz2_gIA/mqdefault.jpg)](https://youtu.be/lPx-Yz2_gIA)

[![Video Explanation](https://img.youtube.com/vi/0sMVPGsY84w/mqdefault.jpg)](https://youtu.be/0sMVPGsY84w)

## Complexity Analysis

- **Time Complexity:** O(n * m), where `n` is the number of strings and `m` is the average length of the strings. We iterate through all characters in all strings to count them.
- **Space Complexity:** O(1), as the number of possible characters is fixed (26 lowercase English letters), so the extra space for counters is constant.