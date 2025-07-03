list = [-1,2]

def count_negatives(lst):
    count = 0
    for num in lst:
        if num < 0:
            count += 1
    return count


print(count_negatives(list))