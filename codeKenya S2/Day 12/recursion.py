# recursion - a function that calls itself.

def print_hello_world(n): #5
    #1. Base Case
    if n <=0:
        print("Done")
        return

    #2 General case
    print("Hello, World!")
    return print_hello_world(n-1)

#print_hello_world(5)

#iteratively



def factorial(n):
    if n <= 1:
        return 1
    
    return n * factorial(n - 1)


def factorial2(n):
    result = 1
    while n > 1:
        result = result * n
        n-=1
    return result

#print(factorial2(3))

#1-1 + 1-2 = 0 + -1 = -1
# (2-1) + (2-2) = 1
def fibonacci(n):
    if n <= 0:
        print("Naah")
        return
    if n == 1 or n == 2:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2) #    2 + 1 = 3

print(fibonacci(-1))
    


