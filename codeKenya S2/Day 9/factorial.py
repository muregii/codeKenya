"""def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(3))

def sum_list(lst):

    if lst == []:
        return 0
    
    return lst.pop() +sum_list(lst)


lst = [1,2,3,4,5]
print(sum_list(lst))

def is_power_of_two(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 2 > 0:
        return False
    return is_power_of_two(n // 2)

print(is_power_of_two(1)) 

def is_power_of_two(n):
    if n <= 0 or n % 2 > 0:
        return False
    if n == 1:
        return True
    return is_power_of_two(n // 2)

print(is_power_of_two(1))
"""

def print_hello_world(n):
    if n <= 0:
        print("the end")
        return

    print("hello world")
    return print_hello_world(n-1)

print_hello_world(2)



