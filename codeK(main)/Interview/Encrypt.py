
from sympy import nextprime

# Since we're given the NetID, let's extract the two distinct letters and convert them to ASCII.
# The NetID provided is 'rmm100'. The first two distinct letters are 'r' and 'm'.

# Convert letters to ASCII values
ascii1 = ord('r')
ascii2 = ord('m')

# Calculate the ascii-th prime numbers
prime_p = nextprime(ascii1 - 1)  # '-1' since nextprime gives the next prime greater than the argument
prime_q = nextprime(ascii2 - 1)

ascii1, ascii2, prime_p, prime_q
