# Climbing Stairs Leetcode ChallengeS
# You are given an integer n representing the number of steps to reach the top of a staircase. 
# You can climb with either 1 or 2 steps at a time.
# Return the number of distinct ways to climb to the top of the staircase.

def climb_stairs(n):
    if n <= 2:
        return n
    one, two = 2, 1
    for _ in range(3, n+1):
        one, two = one + two, one
    return one

# Example Usage
print(climb_stairs(5))

# Time Complexity: O(n)
# Space Complexity: O(1)

