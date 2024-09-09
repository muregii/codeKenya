# Leetcode - Lemonade Change

## Problem Description

At a lemonade stand, each lemonade costs`$5`. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a `$5`, `$10`, or `$20` bill. You must provide the correct change to each customer so that the net transaction is that the customer pays `$5`.

Note that you do not have any change in hand at first.

Given an integer array `bills` where `bills[i]` is the bill the `ith` customer pays, return *`true` if you can provide every customer with the correct change, or `false` otherwise.
*
**Constraints:**
- `1 <= bills.length <= 10^5`
- `bills[i]` is either `5`, `10`, or `20`.

## Solution

**Understanding the Problem:**
   - The task is to ensure you can provide the correct change for each customer while managing limited resources of $5 and $10 bills as you collect them.
   - You need to handle each transaction by providing change for $10 and $20 bills using the minimum number of bills you already possess.

**Breaking It Down**
   - **$5 Bill:** No change is needed when a customer pays with a $5 bill since the lemonade costs exactly $5.
   - **$10 Bill:** If a customer pays with a $10 bill, you must provide $5 in change, which means you need to have at least one $5 bill available.
   - **$20 Bill:** If a customer pays with a $20 bill, you need to provide $15 in change. The optimal way to provide change is to give one $10 bill and one $5 bill (if available). If that’s not possible, you need to provide three $5 bills.

**Implementation Approach:**
   - Maintain two variables, one to track the count of $5 bills and another for $10 bills.
   - Iterate through the `bills` array and:
     - When a $5 bill is given, simply increase the count of $5 bills.
     - When a $10 bill is given, ensure you can give a $5 bill as change and adjust your counts accordingly.
     - When a $20 bill is given, try to give a $10 bill and a $5 bill as change, or three $5 bills if the former is not possible.
   - If at any point you can't provide the required change, return `False`. Otherwise, return `True` at the end.

**Algorithm Steps:**
   1. Initialize counters for $5 and $10 bills.
   2. Iterate over each customer’s payment in the `bills` array.
   3. Based on the payment:
      - Add $5 bills to the counter.
      - If a $10 bill is given, subtract one $5 bill.
      - If a $20 bill is given, subtract one $10 and one $5 bill (preferably), or three $5 bills.
   4. If you can’t provide change at any step, return `False`. Otherwise, return `True`.

### Python Code

```python
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        
```

### Example

```python
# Input
bills = [5, 5, 5, 10, 20]

# Output
True
```

### Explanation

- First customer pays $5, no change required.
- Second and third customers also pay with $5, no change required.
- Fourth customer pays $10, so we give $5 as change (one $5 bill remains).
- Fifth customer pays $20, we give one $10 bill and one $5 bill as change.
  
The result is `True` since you can successfully provide change to all customers.

### Usage

To use the solution, create an instance of the `Solution` class and call the `lemonadeChange` method with the `bills` array:

```python
# Example usage
solution = Solution()
bills = [5, 5, 5, 10, 20]
result = solution.lemonadeChange(bills)
print(result)  # Output: True
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/860)

[Link to detailed explanation on geeksforgeeks](https://www.geeksforgeeks.org/lemonade-stand-change-challenge/)


### Check Out These Video(s)

[![Video Explanation](https://img.youtube.com/vi/_hnQY74pnCA/mqdefault.jpg)](https://youtu.be/_hnQY74pnCA)

[![Video Explanation](https://img.youtube.com/vi/n_tmibEhO6Q/mqdefault.jpg)](https://youtu.be/n_tmibEhO6Q)

[![Video Explanation](https://img.youtube.com/vi/mSVAw0AUZgA/mqdefault.jpg)](https://youtu.be/mSVAw0AUZgA)



### Complexity Analysis

- **Time Complexity:** O(n), where `n` is the length of the `bills` array. Each element is processed once.
- **Space Complexity:** O(1), since we are only using a constant amount of extra space.