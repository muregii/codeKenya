
from heapq import *

heap = []

heappush(heap, 2)
heappush(heap, 1)
heappush(heap, 3) 

# [1, 2, 3]
#print(heappop(heap))

#print(len(heap))

#nums = [9,5,6,7,1,2,5,4]
#heapify(nums)
#print(nums)

students = [ 
    {"name": "Lynn", "score": 98},
    {"name" : "Ray", "score": 99},
    {"name" : "Tony", "score": 87},

]

top2 = nlargest(2, students, key = lambda s: s["score"])
print(top2)




