# Leetcode - Replace Words

## Problem Description

In English, we have a concept called **root**, which can be followed by some other word to form another longer word - let's call this word a **derivative**. For example, when the root `"help"` is followed by the word `"ful"`, we can form the derivative `"helpful"`.

Given a `dictionary` consisting of many **roots** and a `sentence` consisting of words separated by spaces, replace all the derivatives in the sentence with the `root` forming them. If a derivative can be replaced by more than one **root**, replace it with the **root** that has **the shortest length**.

Return *the `sentence`* after the replacement.

**Constraints:**
- `1 <= dictionary.length <= 1000`
- `1 <= dictionary[i].length <= 100`
- `dictionary[i]` consists of only lowercase letters.
- `1 <= sentence.length <= 10^6`
- `sentence` consists of only lowercase letters and spaces.
- The number of words in `sentence` is in the range `[1, 1000]`
- The length of each word in `sentence` is in the range `[1, 1000]`
- Every two consecutive words in `sentence` will be separated by exactly one space.
- `sentence` does not have leading or trailing spaces.

## Solution

To solve this problem, efficiently replace derivatives in a sentence with their corresponding roots. The approach involves creating a structure to quickly find and replace words with their shortest root.


Imagine you have a list of short words (roots) like "cat," "bat," and "rat." Then you have a sentence like "the cattle was rattled by the battery." Your task is to replace any longer word that starts with one of the roots with that root. So, "cattle" would become "cat" because it starts with "cat," and "rattled" would become "rat."


Here are the steps:

1. **Build a Trie (Prefix Tree):**
   - A Trie is a tree-like data structure that makes it easy to store and retrieve words. We’ll use it to store all the roots.
   - Each node in the Trie represents a letter, and the path from the root to a node represents a prefix of some root word.

2. **Insert Roots into the Trie:**
   - Insert each root from the dictionary into the Trie. This will allow us to quickly check if any prefix of a word in the sentence is a root.

3. **Replace Words Using the Trie:**
   - For each word in the sentence, traverse the Trie to find the shortest root. If a root is found, replace the word with that root.


By building a Trie, we can efficiently replace each word in the sentence with its shortest root, if a corresponding root exists. This way, we ensure that the replacement is done quickly and correctly.


```python
class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        
```

## Usage

To use the solution, create an instance of the `Solution` class and call the `replaceWords` method with the list of roots (`dictionary`) and the `sentence` you want to process:

```python
solution = Solution()
dictionary = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
result = solution.replaceWords(dictionary, sentence)
print(result)  # Output: "the cat was rat by the bat"
```


[Link to detailed explanation on Medium](https://lenchen.medium.com/leetcode-648-replace-words-52b3800f9642)

[Link to detailed explanation on AlgoMonster](https://algo.monster/liteproblems/648)

## Check Out This Video

[![Video Explanation](https://img.youtube.com/vi/qFZSJl_7lV4/mqdefault.jpg)](https://youtu.be/qFZSJl_7lV4)

[![Video Explanation](https://img.youtube.com/vi/EFskdMa-eBg/mqdefault.jpg)](https://youtu.be/EFskdMa-eBg)

[![Video Explanation](https://img.youtube.com/vi/HdQeNCwE2tU/mqdefault.jpg)](https://youtu.be/HdQeNCwE2tU)

## Complexity Analysis

- **Time Complexity:** O(n * m + k), where `n` is the number of words in the dictionary, `m` is the average length of the words, and `k` is the length of the sentence. Building the Trie takes `O(n * m)`, and replacing words in the sentence takes `O(k)`.
- **Space Complexity:** O(n * m), as the Trie will store all the roots, and the space required depends on the total number of characters in all roots combined.