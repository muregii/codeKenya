# recursion - a function that calls itself.

def print_hello_world(n): #5
    #1. Base Case
    if n <=0:
        print("Done")
        return

    #2 General case
    print("Hello, World!")
    return print_hello_world(n-1)

print_hello_world(5)

def factorial(n):
    if n <= 1:
        return 1
    
    return n * factorial(n - 1)

print(factorial(3))


