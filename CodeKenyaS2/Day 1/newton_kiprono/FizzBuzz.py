def fizzbuzz(n):
  num_list = []
  for i in range(1, n+1):
    if (i % 15 == 0):  # i%3 == 0 and i%5 == 0
      num_list.append("FizzBuzz")
      continue
    if (i % 3 == 0):
      num_list.append("Fizz")
      continue
    if (i % 5 == 0):
      num_list.append("Buzz")
      continue
    num_list.append(str(i))

  return num_list


result = fizzbuzz(16)
print(result)
