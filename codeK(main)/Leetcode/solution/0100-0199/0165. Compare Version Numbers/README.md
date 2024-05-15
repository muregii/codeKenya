# Leetcode - Compare Version Numbers

## Problem Description

Given two **version strings**, `version1` and `version2`, compare them. A version string consists of **revisions** separated by dots `'.'`. The **value of the revision** is its **integer conversion** ignoring leading zeros.

To compare version strings, compare their revision values in **left-to-right order**. If one of the version strings has fewer revisions, treat the missing revision values as `0`.

*Return the following:*

- If `version1 < version2`, return `-1`.
- If `version1 > version2`, return `1`.
- Otherwise, return `0`.

## Solution

To compare version numbers, we can split the version strings by dots '.' and compare each revision value from left to right.

Here's how we can approach this problem:

1. Split `version1` and `version2` strings into lists of integers using the dot '.' as a separator.
2. Iterate through each pair of revision values from both version strings.
3. If one of the version strings has fewer revisions, treat the missing revision values as 0.
4. Compare the corresponding revision values.
5. If the revision value in `version1` is smaller than that in `version2`, return -1.
6. If the revision value in `version1` is larger than that in `version2`, return 1.
7. If all revision values are equal, continue comparing the remaining revisions.
8. If all revisions are equal, return 0.

By comparing each revision value from left to right, we can determine the relationship between two version strings.

## Usage

To use the solution, create an instance of the `Solution` class and call the `compareVersion` method with the input parameters `version1` and `version2`:

```python
solution = Solution()
# Define the input version strings
# version1 = "1.0.1"
# version2 = "1"
# Call the compareVersion method
result = solution.compareVersion(version1, version2)
print(result)
```

```python
# version1 = "1.0.1"
# version2 = "1"
```

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/compare-two-version-numbers/)


## Check Out this video

[![Video Explanation](https://img.youtube.com/vi/CRbDvJorCF0/mqdefault.jpg)](https://youtu.be/CRbDvJorCF0)


[![Video Explanation](https://img.youtube.com/vi/MTSetP6kcRI/mqdefault.jpg)](https://youtu.be/MTSetP6kcRI)


[![Video Explanation](https://img.youtube.com/vi/Z4Af1_t7wzk/mqdefault.jpg)](https://youtu.be/Z4Af1_t7wzk)


## Complexity Analysis

- **Time Complexity:** O(n), where n is the maximum number of revisions in either version string. We iterate through each revision value once.
- **Space Complexity:** O(n), where n is the number of revisions in the longer version string. We use additional space to store the integer representations of the revisions.