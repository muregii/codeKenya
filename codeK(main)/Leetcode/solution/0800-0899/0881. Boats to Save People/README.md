# Leetcode - Boats to Save People

## Problem Description

You are given an array `people` where `people[i]` is the weight of the `ith` person, and an **infinite number of boats** where each boat can carry a maximum weight of `limit`. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most `limit`.

*Return the minimum number of boats to carry every given person.*

## Solution

To solve this problem, we can use a two-pointer approach.

Here's how we can approach this problem:

1. Sort the `people` array in non-decreasing order.
2. Initialize two pointers `left` and `right` at the beginning and end of the array, respectively.
3. Initialize a variable `boats` to track the number of boats required.
4. While `left <= right`:
   - If `people[left]` + `people[right]` <= `limit`, increment `left` and decrement `right` to pair the lightest person with the heaviest person within the weight limit.
   - Otherwise, only decrement `right` to pair the heaviest person with another person or travel alone if necessary.
   - Increment `boats` for each boat used.
5. Return the value of `boats`.

By using a two-pointer approach, we can efficiently pair people in boats while ensuring that the weight limit is not exceeded.

## Usage

To use the solution, create an instance of the `Solution` class and call the `numRescueBoats` method with the input parameters `people` and `limit`:

```python
solution = Solution()
# Define the input array people and the boat weight limit
# people = [3, 2, 2, 1]
# limit = 3
# Call the numRescueBoats method
result = solution.numRescueBoats(people, limit)
print(result)
```

```python
# people = [3, 2, 2, 1]
# limit = 3
```

[Link to detailed explanation](https://www.naukri.com/code360/library/boats-to-save-people)


[Link to detailed explanation](https://www.linkedin.com/pulse/leetcode-881-boats-save-people-efficiently-solving-mccullough-sxhke/)


[Link to detailed explanation](https://www.linkedin.com/pulse/understanding-time-complexity-big-o-notation-fiona-githaiga-jlv6f/)


## Check Out this video

[![Video Explanation](https://img.youtube.com/vi/GqT3BFKdh-I/mqdefault.jpg)](https://youtu.be/GqT3BFKdh-I)


[![Video Explanation](https://img.youtube.com/vi/XbaxWuHIWUs/mqdefault.jpg)](https://youtu.be/XbaxWuHIWUs)


[![Video Explanation](https://img.youtube.com/vi/bC_tuyiAEac/mqdefault.jpg)](https://youtu.be/bC_tuyiAEac)


## Complexity Analysis

- **Time Complexity:** O(n log n), where n is the number of people. Sorting the people array takes O(n log n) time, and the two-pointer traversal takes O(n) time.
- **Space Complexity:** O(1). We use only constant extra space for storing pointers and variables.