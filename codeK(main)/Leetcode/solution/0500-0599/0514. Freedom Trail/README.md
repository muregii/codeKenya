# Leetcode - Freedom Trail

## Problem Description

In the video game Fallout 4, the quest **"Road to Freedom"** requires players to reach a metal dial called the **"Freedom Trail Ring"** and use the dial to spell a specific keyword to open the door.

Given a string `ring` that represents the code engraved on the outer ring and another string `key` that represents the keyword that needs to be spelled, return the minimum number of steps to spell all the characters in the keyword.

Initially, the first character of the ring is aligned at the `"12:00"` direction. You should spell all the characters in `key` one by one by rotating `ring` clockwise or anticlockwise to make each character of the string key aligned at the `"12:00"` direction and then by pressing the center button.

At the stage of rotating the ring to spell the key character `key[i]`:

- You can rotate the ring clockwise or anticlockwise by one place, which counts as one step. The final purpose of the rotation is to align one of ring's characters at the "12:00" direction, where this character must equal `key[i]`.
- If the character `key[i]` has been aligned at the "12:00" direction, press the center button to spell, which also counts as one step. After the pressing, you could begin to spell the next character in the key (next stage). Otherwise, you have finished all the spelling.

## Solution

To solve this problem, we can use dynamic programming. We'll define a function `dp` to represent the minimum number of steps to spell all the characters in the keyword.

Here's how we can approach this problem:

1. Initialize a 2D array `dp` of size `(len(ring), len(key))`.
2. For each character in the ring, iterate through each character in the key.
3. For each character `key[i]`, find the minimum number of steps required to align it with the current character in the ring.
4. Use dynamic programming to calculate the minimum number of steps based on the previous steps.
5. Return the minimum number of steps required to spell all characters in the keyword.

By dynamically calculating the minimum number of steps for each character in the keyword, we can determine the overall minimum number of steps required.

## Usage

To use the solution, create an instance of the `Solution` class and call the `findRotateSteps` method with the input parameters `ring` and `key`:

```python
solution = Solution()
# Define the input strings ring and key
# ring = "godding"
# key = "gd"
# Call the findRotateSteps method
result = solution.findRotateSteps(ring, key)
print(result)
```

```python
# ring = "godding"
# key = "gd"
```

## Check Out this video

[![Video Explanation](https://img.youtube.com/vi/14h9OuYf2GA/mqdefault.jpg)](https://youtu.be/14h9OuYf2GA)

[![Video Explanation](https://img.youtube.com/vi/NOgnlTXidSs/mqdefault.jpg)](https://youtu.be/NOgnlTXidSs)

## Complexity Analysis

- **Time Complexity:** O(n^2 * m), where n is the length of the ring and m is the length of the key. We iterate through each character in the ring and key to calculate the minimum number of steps.
- **Space Complexity:** O(n * m), where n is the length of the ring and m is the length of the key. We use a 2D array to store intermediate results.