"""Example 3: Given two sorted integer arrays arr1 and arr2,
 return a new array that combines both of them and is also sorted."""
from typing import List

def merge_two_arrays(nums_a: List[int], nums_b: List[int]) -> List[int]:
    i = 0
    j = 0
    ans = []
    while i < len(nums_a) and j < len(nums_b):
        if nums_a[i] < nums_b[j]:
            ans.append(nums_a[i])
            i+=1
            #print(f"{nums_a[i]} was less than: {nums_b[j]} ")
        else:
            #print(f"{nums_a[i]} was greater than or equal to: {nums_b[j]} ")
            ans.append(nums_b[j])
            j+=1
        
    while i < len(nums_a):
            ans.append(nums_a[i])
            i+=1

    while j < len(nums_b):
            ans.append(nums_b[j])
            j+=1

    print(f"code exited with: 0")
    return ans

list_a = [1,2,3,4,5,6]
list_b = [3,4, 78]
result = merge_two_arrays(list_a, list_b)
print(result)

