    def containsDuplicate(self, nums):
        # A dictionary to store the occurence of the numbers
        mydict = {}

        # Count occurrences of each number in nums
        for num in nums:

            # Get current count of num, default is 0, then add 1
            mydict[num] = mydict.get(num, 0) + 1

        # Check if any number appears more than once
        for _, value in mydict.items():
            if value > 1:
                return True
        return False
