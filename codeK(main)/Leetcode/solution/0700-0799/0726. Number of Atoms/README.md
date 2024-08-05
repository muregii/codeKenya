# Leetcode - Number of Atoms

## Problem Description

Given a string `formula` representing a chemical formula, *return the count of each atom*.

The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

One or more digits representing that element's count may follow if the count is greater than `1`. If the count is `1`, no digits will follow.

- For example, `"H2O"` and `"H2O2"` are possible, but `"H1O2"` is impossible.

Two formulas are concatenated together to produce another formula.

- For example, `"H2O2He3Mg4"` is also a formula.

A formula placed in parentheses, and a count (optionally added) is also a formula.

- For example, `"(H2O2)"` and `"(H2O2)3"` are formulas.

Return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

The test cases are generated so that all the values in the output fit in a 32-bit integer.

**Constraints:**
- `1 <= formula.length <= 1000`
- `formula` consists of English letters, digits, '(', and ')'.
- `formula` is always valid.

## Solution

To solve this problem, parse the chemical formula and count the occurrences of each atom. 

1. **Understanding the Problem:**
   - Each element starts with an uppercase letter, followed by zero or more lowercase letters.
   - Digits following an element denote the count of that element.
   - Parentheses group elements, and a digit after the parentheses denotes how many times the group should be counted.
   - We need to handle nested parentheses and combine counts from all levels.

2. **Simulating the Process:**
   - Use a stack to handle nested parentheses.
   - Parse the formula character by character to extract elements, counts, and manage groups.
   - Keep track of counts using a dictionary.

3. **Algorithm Steps:**
   - Iterate through the formula:
     - If encountering '(', push the current count dictionary to the stack.
     - If encountering ')', pop the stack and multiply the popped dictionary by the following number.
     - If encountering an element, parse its count and add it to the current count dictionary.
   - Merge counts from nested levels.
   - Sort elements by name and format the output string.

### Example

Suppose you have:
- `formula = "K4(ON(SO3)2)2"`

1. Initialize a stack to manage nested groups.
2. Parse the formula and manage counts using dictionaries.
3. Merge counts from nested levels and format the output.

### Python Code

```python
class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        
```

### Usage

To use the solution, create an instance of the `Solution` class and call the `countOfAtoms` method with the `formula` string:

```python
# Example usage
solution = Solution()
formula = "K4(ON(SO3)2)2"
result = solution.countOfAtoms(formula)
print(result)  # Output: "K4N2O14S4"
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/726)

[Link to detailed explanation on Medium](https://medium.com/@mberkkellecioglu/my-leetcode-solutions-726-number-of-atoms-46d3cf869332)

### Check Out These Videos

[![Video Explanation](https://img.youtube.com/vi/iuK05gGBzJc/mqdefault.jpg)](https://youtu.be/iuK05gGBzJc)

[![Video Explanation](https://img.youtube.com/vi/NYLmQI0GkeM/mqdefault.jpg)](https://youtu.be/NYLmQI0GkeM)

### Complexity Analysis

- **Time Complexity:** O(n), where n is the length of the formula. We process each character once.
- **Space Complexity:** O(n), due to the use of a stack to manage nested groups and a dictionary to store counts.