'''
The FizzBuzz Challenge: Iterate 1 to 100.
If divisible by 3, print "Fizz".
If divisible by 5, print "Buzz".
If both, print "FizzBuzz".
'''

n = 100
fizz = 3
buzz = 5



for i in range (1, 101):
  output = ""
  
  if (i % fizz) == 0: output += "Fizz"
  if (i % buzz) == 0: output += "Buzz"
  
  print(f"{output} at {i=}")

  '''
  fizz_mod = (i % fizz)
  buzz_mod = (i % buzz)

  if fizz_mod + buzz_mod == 0:
    print(f"FizzBuzz at {i=}")
  elif fizz_mod == 0:
    print(f"Fizz at {i=}")
  elif buzz_mod == 0:
    print(f"Buzz at {i=}")
  else:
    pass
  '''

