def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # initialize empty list which will store the indexes
    mylist = []

    # loop through the elements in the array
    for i in range(len(nums)):
        # for each element in the array, compare its sum with other elements with the target 
        for x in range(len(nums)):
            if nums[i] + nums[x] == target and i != x:
                #append the indexes  if their sum eqauls target
                mylist.append(i)
                mylist.append(x)
                return mylist
