list = [-1,2]

def count_negatives(lst):
    count = 0
    for num in lst:
        if num < 0:
            count += 1
    return count


print(count_negatives(list))



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