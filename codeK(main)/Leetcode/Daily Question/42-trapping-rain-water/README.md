# Leetcode - Trapping Rain Water

## Problem Description

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.


## Solution

"Imagine you have an elevation map represented by a series of bars. Now, when it rains, some areas between these bars can trap water.

Here's how we can calculate the amount of water trapped:

1. We start by iterating through the elevation map from left to right.
2. At each bar, we calculate the maximum height of bars to the left and to the right.
3. The amount of water that can be trapped at the current bar is the minimum of the maximum height to the left and to the right minus the height of the current bar.
4. We sum up the amount of water trapped at each bar to get the total amount of trapped water.

For example, if the elevation map is [0,1,0,2,1,0,1,3,2,1,2,1], the total amount of trapped water is 6 units.

Does this make sense? Great!"

![1_q64XKMICwlYIL06tOQrteg](https://github.com/muregii/codeKenya/assets/87364726/42ec84a0-519e-4b72-8ffe-8e90476d7074)
![1_8SkgEDMEMM6ClQH_rweYrw](https://github.com/muregii/codeKenya/assets/87364726/23610f2e-5778-43cc-98b1-f90be01187a0)
![1_0fL9cKIRNTCOkybt7zTNsw](https://github.com/muregii/codeKenya/assets/87364726/55d7e66d-b787-41d2-aa25-7b5849f66361)




## Usage

To use the solution, simply create an instance of the `Solution` class and call the `trap` method with the input list `height` representing the elevation map:

```python
solution = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
result = solution.trap(height)
print(result)
```


[Link to detailed explanation on Medium](https://medium.com/enjoy-algorithm/trapping-rain-water-a79938abf921)

[Link to detailed explanation on Geeksforgeeks](https://www.geeksforgeeks.org/trapping-rain-water/)


## Check Out this video

[![Video Explanation](https://img.youtube.com/vi/C8UjlJZsHBw/mqdefault.jpg)](https://youtu.be/C8UjlJZsHBw)





## Complexity Analysis

- **Time Complexity:** O(n), where n is the number of bars in the elevation map.
- **Space Complexity:** O(n), as we may use additional arrays to store the maximum heights to the left and to the right of each bar.

---
