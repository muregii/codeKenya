# Leetcode - Fraction Addition and Subtraction

## Problem Description

Given a string `expression` representing an expression of fraction addition and subtraction, return the calculation result in string format.

The final result should be an **`irreducible fraction`**. If your final result is an integer, change it to the format of a fraction that has a denominator `1`. So in this case, `2` should be converted to `2/1`.


### Constraints:
- The input string only contains `'0'` to `'9'`, `'/'`, `'+'`, and `'-'`. So does the output.
- Each fraction in the input and output has the format `±numerator/denominator`. If the first input fraction or the output is positive, then `'+'` will be omitted.
- The input only contains valid **irreducible fractions**, where the **numerator** and **denominator** of each fraction will always be in the range `[1, 10]`. If the denominator is `1`, it means this fraction is actually an integer in a fraction format defined above.
- The number of given fractions will be in the range `[1, 10]`.
- The numerator and denominator of the final **result** are guaranteed to be valid and in the range of **32-bit** int.

## Solution

**Understanding the Problem:**
- We are asked to compute the result of a series of fraction additions and subtractions.
- Fractions are added or subtracted using a common denominator.
- The final result must be presented as an irreducible fraction, which means the greatest common divisor (GCD) is used to simplify the fraction.
  
**Breaking It Down:**
- **Fraction Arithmetic**: When adding or subtracting fractions, a common denominator is necessary. For two fractions `a/b` and `c/d`, the result of their sum or difference is calculated as:
  \[
  \frac{a}{b} \pm \frac{c}{d} = \frac{a \cdot d \pm b \cdot c}{b \cdot d}
  \]
- **Simplification**: Once the result is calculated, we simplify the fraction by dividing both the numerator and the denominator by their greatest common divisor (GCD).
  
**Key Concepts:**
- **LCM**: To find a common denominator, we use the least common multiple (LCM) of the denominators.
- **GCD**: To simplify a fraction, we divide both the numerator and denominator by their greatest common divisor.

**Steps to Solve:**
1. Parse the string `expression` to extract the numerators and denominators.
2. Use the least common multiple (LCM) to calculate a common denominator for the fractions.
3. Add or subtract the numerators accordingly.
4. Simplify the resulting fraction using the greatest common divisor (GCD).
5. Return the fraction in the format of `numerator/denominator`.

**Implementation Approach:**
- We first split the input string to identify the fractions and their signs.
- For each fraction, we convert it to a common denominator and perform the arithmetic operation (addition or subtraction).
- After the entire expression is evaluated, we simplify the resulting fraction by dividing the numerator and denominator by their GCD.

### Python Code

```python
class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        
```

### Example

```python
# Input
expression = "-1/2+1/2+1/3"

# Output
"1/3"
```

### Explanation:
1. We break down the expression into three fractions: `-1/2`, `1/2`, and `1/3`.
2. `-1/2 + 1/2 = 0`, so we are left with `0 + 1/3`.
3. The final result is `"1/3"`.

### Usage

To use the solution, create an instance of the `Solution` class and call the `fractionAddition` method with the input expression string:

```python
# Example usage
solution = Solution()
expression = "-1/2+1/2+1/3"
result = solution.fractionAddition(expression)
print(result)  # Output: "1/3"
```


[Link to detailed explanation on AlgoMonster](https://algo.monster/liteproblems/592)


### Complexity Analysis

- **Time Complexity:** O(n), where `n` is the length of the expression. We need to iterate through each character in the expression to parse and evaluate the fractions.
- **Space Complexity:** O(1), because we are only using a constant amount of space for storing intermediate variables such as the numerators, denominators, and the result.