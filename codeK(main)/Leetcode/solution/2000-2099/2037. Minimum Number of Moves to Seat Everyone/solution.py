class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        # Sort seats and students to align closest seats to students
        seats.sort()
        students.sort()
        
        # Calculate the sum of absolute differences
        moves = 0
        for i in range(len(seats)):
            moves += abs(seats[i] - students[i])
            
        return moves