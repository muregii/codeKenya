lst = [1,2,3,4,5,6]

def above_threshhold(lst, threshold):

    if not lst:
        return []
    head, *tail = lst

    if head > threshold:
        return [head] + above_threshhold(tail, threshold)
    else:
        return above_threshhold(tail, threshold)

print(above_threshhold(lst, 3))
    