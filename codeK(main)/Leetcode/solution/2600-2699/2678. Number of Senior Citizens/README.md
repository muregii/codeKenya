# Leetcode - Number of Senior Citizens

## Problem Description

You are given a `0-indexed` array of strings `details`. Each element of `details` provides information about a given passenger compressed into a string of length 15. The system is such that:

- The first ten characters consist of the phone number of passengers.
- The next character denotes the gender of the person.
- The following two characters are used to indicate the age of the person.
- The last two characters determine the seat allotted to that person.

Return *the number of passengers who are **strictly more than 60 years old***.

**Constraints:**
- `1 <= details.length <= 100`
- `details[i].length == 15`
- ``details[i] consists of digits from '0' to '9'`.
- ``details[i][10] is either 'M', 'F', or 'O'`.
- The phone numbers and seat numbers of the passengers are distinct.

## Solution

**Understanding the Problem:**
   - We are given a list of passenger details where each detail is a string of length 15. The string contains information such as the phone number, gender, age, and seat number of a passenger.
   - Our goal is to count the number of passengers who are strictly more than 60 years old based on the provided details.

**Breaking It Down**
   - **Extracting Age:**
     - The age of the passenger is encoded in the 12th and 13th characters of the string (index 11 and 12 in 0-indexed format).
     - We need to extract these characters, convert them to an integer, and check if the age is greater than 60.
     
   - **Counting Seniors:**
     - Iterate through the list of details, extract the age for each passenger, and increment the count if the age is more than 60.
     - The result will be the total count of passengers who are seniors.

**Implementation Approach:**
   - Initialize a counter to keep track of the number of seniors.
   - Loop through each string in the `details` array, extract the age, and check if it exceeds 60.
   - If the age is greater than 60, increment the counter.
   - Return the counter as the final result.

**Algorithm Steps:**
   - **Initialize Counter:** Start with a counter set to zero.
   - **Iterate Through Details:** For each passenger detail:
     - Extract the age using string slicing.
     - Convert the age substring to an integer.
     - If the age is greater than 60, increment the counter.
   - **Return Result:** The counter now holds the number of passengers over 60 years old.

### Python Code

```python
class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        
```

### Example

```python
# Input
details = ["1234567890M6501", "0987654321F7002", "1122334455M5903"]

# Output
1
```

### Explanation
1. **Extracting Age:** 
   - For the first passenger, the age is 65.
   - For the second passenger, the age is 70.
   - For the third passenger, the age is 59.
2. **Counting Seniors:** The first and second passengers are seniors (age > 60), so the count is 2.

### Usage

To use the solution, create an instance of the `Solution` class and call the `countSeniors` method with the `details` array:

```python
# Example usage
solution = Solution()
details = ["1234567890M6501", "0987654321F7002", "1122334455M5903"]
result = solution.countSeniors(details)
print(result)  # Output: 2
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/2678)

[Link to detailed explanation on Medium](https://medium.com/@pranavrp16/leetcode-problem-2678-number-of-senior-citizens-dcc-01-08-24-af7368ba2dfc)

### Check Out These Video(s)

[![Video Explanation](https://img.youtube.com/vi/l6_wwKzFmVo/mqdefault.jpg)](https://youtu.be/l6_wwKzFmVo)

### Complexity Analysis

- **Time Complexity:** O(n), where `n` is the length of the `details` array. We iterate through each string in the array once.
- **Space Complexity:** O(1), as we only use a counter variable and do not require additional space relative to the input size.