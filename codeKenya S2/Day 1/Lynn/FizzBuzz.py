#Assignment One: FizzBuzz LeetCode Challenge
#Problem Statement: Write a program that prints the numbers from 1 to n. 
#For multiples of three print "Fizz" instead of the number.
#For the multiples of five print "Buzz". 
#For numbers which are multiples of both three and five print "FizzBuzz".
#If not multiples of 3 or 5, convert the number to a string and append


# Define a function named Multiples that takes an integer n as input
def Multiples(n):
    result = []

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")  
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

print(Multiples(3))
print(Multiples(5))
print(Multiples(15))
