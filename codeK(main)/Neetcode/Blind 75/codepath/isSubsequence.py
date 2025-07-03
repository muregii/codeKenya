def is_subsequence(lst, sequence):
    pointer = 0
    for num in lst:
        if pointer == len(sequence):
            break
        if num == sequence[pointer]:
            pointer +=1

    return pointer == len(sequence)
    
lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(is_subsequence(lst, sequence))