
def combineArray(arr1, arr2):
    i = 0
    j = 0
    answer = []
    # [1, 2, 4] [3, 5, 6]
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            answer.append(arr1[i])
            i+=1
        else:
            answer.append(arr2[j])
            j+=1
    
    while i < len(arr1):
        answer.append(arr1[i])
        i+=1
    
    while j < len(arr2):
        answer.append(arr2[j])
        j+=1       
            
    return answer

# Test cases
test_cases = [
    ([1, 3, 5], [2, 4, 6]),
    ([1, 2, 3], [4, 5, 6]),
    ([], [1, 2, 3]),
    ([1, 2, 3], []),
    ([1, 4, 5, 8], [2, 3, 6, 7, 9])
]

# Testing the function
for index, (arr1, arr2) in enumerate(test_cases):
    result = combineArray(arr1, arr2)
    print(f"Test Case {index + 1}: combine({arr1}, {arr2}) = {result}")