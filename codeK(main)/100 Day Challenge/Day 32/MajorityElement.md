# Majority Element Problem

## Problem Statement
Given an array `nums` of size `n`, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. It is assumed that the majority element always exists in the array.

## Concepts Involved
- Arrays
- HashTable
- Divide and Conquer
- Sorting
- Counting

## Solution Approach
A common and efficient way to solve this problem is to use the **Boyer-Moore Voting Algorithm**. This algorithm is particularly effective because it performs in O(n) time and O(1) space. The basic idea of this algorithm is to find a candidate for the majority element and then confirm whether it is actually the majority element.

## Implementation in Java

```java
public class Solution {
    public int majorityElement(int[] nums) {
        int count = 0;
        Integer candidate = null;

        for (int num : nums) {
            if (count == 0) {
                candidate = num;
            }
            count += (num == candidate) ? 1 : -1;
        }

        return candidate;
    }
}
