def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    # dictionary to hold numbers' occurences
    count = {}
    # a list of lists with its values being the nummbers in nums
    # with their index being thier frequencies
    freq = [[] for i in range(len(nums) + 1)]

    # store the occurences in the dictionary
    for num in nums:
        count[num] = count.get(num, 0) + 1
    # map the occurences in the frequency lists
    for num, occ in count.items():
        freq[occ].append(num)

    # Iterate freq backwards until only k values are stored
    output = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            output.append(n)
            if len(output) == k:
                return output
