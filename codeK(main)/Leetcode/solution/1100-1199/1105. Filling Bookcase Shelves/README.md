# Leetcode - Filling Bookcase Shelves

## Problem Description

You are given an array `books` where `books[i] = [thickness_i, height_i]` indicates the thickness and height of the `i`th book. You are also given an integer `shelfWidth`.

We want to place these books in order onto bookcase shelves that have a total width of `shelfWidth`.

- We choose some of the books to place on this shelf such that the sum of their thicknesses is less than or equal to `shelfWidth`.
- Then, we build another level of the shelf so that the total height of the bookcase increases by the maximum height of the books we just put down.
- We repeat this process until there are no more books to place.

Note that at each step of the above process, the order of the books we place is the same order as the given sequence of books.

- For example, if we have an ordered list of `5` books, we might place the first and second book onto the first shelf, the third book on the second shelf, and the fourth and fifth book on the last shelf.

Return *the minimum possible height that the total bookshelf can be after placing shelves in this manner*.

**Constraints:**
- `1 <= books.length <= 1000`
- `1 <= thickness_i <= shelfWidth <= 1000`
- `1 <= height_i <= 1000`

## Solution

**Understanding the Problem:**
   - We have a sequence of books with specific thicknesses and heights.
   - We need to place these books on shelves, ensuring that the sum of their thicknesses on each shelf does not exceed the `shelfWidth`.
   - The height of the bookshelf is determined by summing the maximum height of the books on each shelf.

**Breaking It Down**
   - **Dynamic Placement of Books:**
     - For each book, we have to decide whether to place it on the current shelf or start a new shelf.
     - The decision should minimize the overall height of the bookshelf.
     
   - **Dynamic Programming Approach:**
     - Use dynamic programming (DP) to keep track of the minimum height needed to place the first `i` books.
     - For each book, consider placing it on the current shelf or starting a new shelf. Update the DP array with the minimum height possible for each choice.

**Implementation Approach:**
   - Create a DP array where `dp[i]` represents the minimum height of the bookshelf after placing the first `i` books.
   - Initialize `dp[0] = 0` since no books result in zero height.
   - Iterate over each book, and for each possible placement, update the DP array with the minimum height calculated.
   - Finally, `dp[n]` will give the minimum height of the bookshelf after placing all the books.

**Algorithm Steps:**
   - **Initialize DP Array:** Start with a DP array where each value is set to infinity, except `dp[0]` which is `0`.
   - **Iterate Over Books:** For each book, calculate the minimum height for all possible placements.
   - **Update DP Array:** Update the DP array with the minimum height found for placing the books.
   - **Return Result:** The value at `dp[n]` gives the minimum height of the bookshelf.

### Python Code

```python
class Solution(object):
    def minHeightShelves(self, books, shelfWidth):
        """
        :type books: List[List[int]]
        :type shelfWidth: int
        :rtype: int
        """
        
```

### Example

```python
# Input
books = [[1, 3], [2, 4], [3, 2]]
shelfWidth = 6

# Output
4
```

### Explanation
1. **Book Placement:** 
   - Place the first two books on the first shelf. The total thickness is `1 + 2 = 3`, and the height is `max(3, 4) = 4`.
   - Place the third book on the second shelf. The thickness is `3`, and the height is `2`.
2. **Result:** The total height is `4 + 2 = 6`.

### Usage

To use the solution, create an instance of the `Solution` class and call the `minHeightShelves` method with the `books` array and `shelfWidth`:

```python
# Example usage
solution = Solution()
books = [[1, 3], [2, 4], [3, 2]]
shelfWidth = 6
result = solution.minHeightShelves(books, shelfWidth)
print(result)  # Output: 4
```

### Additional Resources

[Link to detailed explanation on Algo Monster](https://algo.monster/liteproblems/1105)

[Link to detailed explanation on Medium](https://medium.com/@shubhijain/1105-filling-bookcase-shelves-e8fe86ed21a3)

### Check Out These Video(s)

[![Video Explanation](https://img.youtube.com/vi/lFYPPPTp8qE/mqdefault.jpg)](https://youtu.be/lFYPPPTp8qE)

[![Video Explanation](https://img.youtube.com/vi/PPSlItuLFkA/mqdefault.jpg)](https://youtu.be/PPSlItuLFkA)

### Complexity Analysis

- **Time Complexity:** O(n^2), where `n` is the number of books. For each book, we consider all previous books to determine the optimal placement.
- **Space Complexity:** O(n), as we use a DP array to store the minimum height required for placing the first `i` books.