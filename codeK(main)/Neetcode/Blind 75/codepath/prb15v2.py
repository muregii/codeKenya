"""Problem 15: Count Evens
Write a function count_evens() that takes in a list of integers lst as a parameter. The function returns the number of even numbers in the list.

def count_evens(lst):
    pass
Example Usage:

lst1 = [1,5,7,9]
count1 = count_evens(lst1)
print(count1)

lst2 = [2,4,6,8]
count2 = count_evens(lst2)
print(count2)
Example Output:

0
4"""
def count_evens(lst):
    count = 0
    for num in lst:
        if num % 2 == 0:
            count +=1
    return count

print(count_evens([1,5,7,9]))

