#Assignment One: FizzBuzz LeetCode Challenge
#Problem Statement: Write a program that prints the numbers from 1 to n. 
#For multiples of three print "Fizz" instead of the number.
#For the multiples of five print "Buzz". 
#For numbers which are multiples of both three and five print "FizzBuzz".
#If not multiples of 3 or 5, convert the number to a string and append


# Define a function named Multiples that takes an integer n as input
def Multiples(n):
    # Create an empty list to store the output strings
    result = []

    # Loop from 1 to n (inclusive) using a for loop
    for i in range(1, n + 1):
        # Check if the current number is divisible by both 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")  # Append "FizzBuzz" to the list
        # Check if the number is divisible by 3 only
        elif i % 3 == 0:
            result.append("Fizz")  # Append "Fizz"
        # Check if the number is divisible by 5 only
        elif i % 5 == 0:
            result.append("Buzz")  # Append "Buzz"
        else:
            # If not divisible by 3 or 5, convert the number to a string and append
            result.append(str(i))
    
    # After the loop ends, return the final list of results
    return result

# Example: Call the function with n=3, n =5, and n = 15 and print the output
print(Multiples(3))
print(Multiples(5))
print(Multiples(15))
