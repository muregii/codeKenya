class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        cycle_length = (n - 1) * 2
        time = time % cycle_length
        
        if time < n:
            return time + 1
        else:
            return cycle_length - time + 1