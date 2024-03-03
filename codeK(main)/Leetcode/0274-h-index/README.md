# Problem 274: H-Index

## Problem Statement
Given an array of integers `citations` where `citations[i]` is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

## Solution Approach
The solution to this problem involves sorting the array of citations in descending order. Then, iterate through the sorted array and find the maximum value of h such that the researcher has published at least h papers that have each been cited at least h times.

## Usage
To use the provided solution script (`h_index_solution.py`), follow these steps:
1. Make sure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the `0274-h-index` folder.
4. Run the Python script.
5. If required, provide input data as per the problem statement.

## Explanation
The `h_index_solution.py` script contains a Python class `Solution` with a method `hIndex` that calculates the researcher's h-index based on the given array of citations. The approach involves sorting the citations in descending order and then finding the maximum value of h satisfying the conditions defined by the h-index.

## References
- Problem Source: [LeetCode - Problem 274: H-Index](https://leetcode.com/problems/h-index/)
