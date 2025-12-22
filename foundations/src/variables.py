'''
Python variables
'''

# Variable and Memory Address
print("\n*** Variable and Memory Address ***")
sample = 32
sample_address = id(sample)
print(f"\n{sample=}, {sample_address=}")

# Local and Global Variables
print("\n*** Local and Global Variables ***")

print("\nLocal variables can only be used in a method or classes that your specify.")
print("\nGlobal variables can be used in any part of the program without issue.")

# Global Variables
x = 6
print((f"After initalization: {x=}"))

def my_def(x):
  x = 8
  print((f"Inside function: {x=}"))  

  global y
  y = "hello"

my_def(x)
print((f"After making function call: {x=}"))

print(f"Calling global variable declared inside function: {y=}")
