class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()  # Sort the list in ascending order
        left, right = 0, len(people) - 1  # Pointers for the two ends
        boats_needed = 0  # Counter for the number of boats needed

        while left <= right:
            # If the heaviest person can be paired with the lightest person
            if people[left] + people[right] <= limit:
                left += 1  # Move the left pointer
            right -= 1  # Move the right pointer
            boats_needed += 1  # Increment the boat counter

        return boats_needed