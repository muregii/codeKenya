# Approach
1. Two pointers


**LeetCode question 80, "Remove Duplicates from Sorted Array II,"** is a variant of the problem you mentioned earlier. This problem allows for up to two occurrences of each element in the final array, rather than strictly unique elements. The array is still sorted, which aids in the detection of duplicates.

### Here's the task in detail:

- **Input:** A sorted array `nums`.
- **Task:** You need to modify the array in-place to allow each element to appear at most twice and remove the extra occurrences of any element. This should be done in a way that maintains the relative order of the elements.
- **Output:** The function should return the new length of the array after the removal of extra duplicates.
- **Constraints:** As with the previous problem, the solution should be `O(n)` in time complexity and `O(1)` in space complexity.

The approach for this problem is similar to the previous one, but with a slight modification to accommodate the allowance of two occurrences of each element:

1. Use a counter `j` to keep track of the position in the array where the next element should be placed.
2. The first two elements can always stay as they are, so you can start iterating from the third element.
3. As you iterate through the array, compare the current element with the element at position `j-2`. If they are different, it means the current element can be placed at position `j` (because it will either be a unique element or the second occurrence of an element), and then increment `j`.

### Here's how you could implement this in Java:

```java
public class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length <= 2) {
            return nums.length;
        }

        int j = 2;
        for (int i = 2; i < nums.length; i++) {
            if (nums[i] != nums[j - 2]) {
                nums[j] = nums[i];
                j++;
            }
        }

        return j;
    }
}
